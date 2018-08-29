import os

import dotenv

from mbed_cloud import utils
from mbed_cloud.sdk import constants


class Config(object):
    _tried_dotenv = False
    api_key = None
    host = None

    def __init__(self, **kwargs):
        self._set_defaults(**kwargs)
        if not self.api_key and not Config._tried_dotenv:
            dotenv.load_dotenv(
                dotenv.find_dotenv(usecwd=True, raise_error_if_not_found=True)
            )
            self._set_defaults()
            # mark dotenv load complete, so we don't have to do it again
            Config._tried_dotenv = True

    def _set_defaults(self, **updates):
        self.update(updates)
        self.api_key = (
            self.api_key or os.getenv(constants.ENVVAR_API_KEY) or constants.DEFAULT_API_KEY
        )
        self.host = self.host or os.getenv(constants.ENVVAR_HOST) or constants.DEFAULT_HOST
        self.user_agent = utils.get_user_agent()

    def update(self, *updates, **kwargs):
        for update in updates:
            self.update(**update)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def items(self):
        return ((k, v) for k, v in vars(self).items() if not k.startswith("_"))
