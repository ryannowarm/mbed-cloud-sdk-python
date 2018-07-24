# This file is autogenerated, do not modify manually. See scripts\generate_ci_config.py for instructions.

#
# Build
#

FROM python:3.6.3-alpine3.6 as PY_SDK_BUILDER

# don't cache any pip downloads
ENV PIP_NO_CACHE_DIR=false
# pipenv puts new virtual env in current working directory
ENV PIPENV_VENV_IN_PROJECT=true
# fake api key for testing
ENV MBED_CLOUD_SDK_API_KEY=abc123
# set 'CI' to replicate CI server environments
ENV CI=yes

# set the working directory (explicit mkdir needed for docker <= 1.9.1 i.e. circleci)
RUN mkdir -p /build
WORKDIR /build

# install system-level dependencies
RUN apk update
RUN apk add git

RUN python -m pip install -U setuptools==40.0.0 pip==10.0.1 pipenv==11.10.0

# add bare minimum files to survive a pip install
COPY scripts scripts
COPY src/mbed_cloud/_version.py src/mbed_cloud/_version.py
COPY setup* ./
COPY README.rst ./
COPY requirements.txt ./
COPY Pip* ./

# install the project (with dev dependencies)
RUN pipenv install --dev

# load the entire project from local checkout as build context
COPY . .

# version the codebase
# we must be told the testrunner version that will be used to test this build
ARG TESTRUNNER_VERSION
RUN pipenv run auto_version --config=scripts/auto_version.toml --news --bump=patch "TESTRUNNER_VERSION='${TESTRUNNER_VERSION}'"
RUN pipenv run python -c "import mbed_cloud; print(mbed_cloud.__version__)"
RUN pipenv run python scripts/generate_news.py

# run smoke tests
RUN pipenv run pytest --durations=3 tests/unit

# run static analysis
RUN pipenv run pytest --durations=3 tests/static

# build the documentation
RUN pipenv run sphinx-apidoc src/mbed_cloud -o docs/built_api -e -M
RUN pipenv run sphinx-build -a -b html -c docs/ docs/ built_docs

# check the package file is good
RUN pipenv run python setup.py check -r -s

# generate a package
RUN pipenv run python setup.py clean --all bdist_wheel

# generate a release package
RUN pipenv run auto_version --config=scripts/auto_version.toml --release
RUN pipenv run python setup.py clean --all --dist-dir release-dist bdist_wheel


#
# Minimal
#

# minimal image for future work. this should come out 'smallish' ~ 160MB
FROM python:3.6.3-alpine3.6 as PY_SDK_LITE
# working dir
WORKDIR /build

COPY --from=PY_SDK_BUILDER build/ ./


# previously, next line also had --no-deps, but we can sanity-check that the venv has everything we need:
RUN source .venv/bin/activate && pip install --no-cache-dir --no-index --find-links dist mbed_cloud_sdk

CMD source .venv/bin/activate && python -c "import mbed_cloud; print(mbed_cloud.__version__)"
