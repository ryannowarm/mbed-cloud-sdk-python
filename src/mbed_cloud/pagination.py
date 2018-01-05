from itertools import islice


class PaginatedResponse(object):
    """Represents a sequence of results from the API

    To represent the potentially large number of results
    returned from an API query, the PaginatedResponse provides
    a lazily-evaluated generator which can be used to step through
    the full result set, fetching new pages of results as needed.

    response = PaginatedResponse(api_function)
    response.first()              {} first item
    response.all()                [{}, ...] all items
    list(response)                [{}, ...] all items from generator
    [item for item in response]   [{}, ...] iteration over generator
    """

    def __init__(self, func, lwrap_type=None, **kwargs):
        """Initialize wrapper by passing in object with metadata structure.

        :param lwrap_type: Wrap each response element in type
        :param init_data: Initialize pagination object with data
        """
        self._func = func
        self._lwrap_type = lwrap_type
        self._kwargs = {}
        self._kwargs.update(kwargs)
        self._kwargs.update(dict(include='total_count'))

        # Initial values, will be updated in first response
        self._total_count = None
        self._next_id = None
        self._has_more = True
        self._exhausted = False
        self._current_data_page = []
        self._current_count = 0
        self._limit = kwargs.get('limit')

    def to_dict(self):
        """Internal state"""
        return dict(
            data=list(self),
            has_more=self._has_more,
            total_count=len(self),
            limit=self._limit,
            after=self._kwargs.get('after'),
            order=self._kwargs.get('order', 'ASC')
        )

    def __iter__(self):
        return self

    def next(self):
        # Python 2 compatibility
        return self.__next__()

    def _get_next_page(self):
        query = {}
        query.update(self._kwargs)
        if self._next_id is not None:
            query.update(dict(after=self._next_id))

        resp = self._func(**query)

        for e in resp.data or []:
            self._current_data_page.append(self._lwrap_type(e) if self._lwrap_type else e)
        self._has_more = resp.has_more
        self._total_count = getattr(resp, 'total_count', None)
        if self._current_data_page:
            self._next_id = self._current_data_page[-1].id

    def _get_total_count(self):
        len_query = {}
        len_query.update(self._kwargs)
        len_query.update(dict(limit=2))
        resp = self._func(**len_query)
        return getattr(resp, 'total_count', 0)

    def all(self):
        """Returns the full query"""
        return PaginatedResponse(func=self._func, lwrap_type=self._lwrap_type, **self._kwargs)

    def first(self):
        """Returns the first item from the query, or None if there are no results"""
        query = PaginatedResponse(func=self._func, lwrap_type=self._lwrap_type, **self._kwargs)
        try:
            return next(query)
        except StopIteration:
            return None

    def __next__(self):
        """Get the next element"""
        if self._exhausted:
            # protect from list(p); list(p) where the second call returns an empty iterable
            raise IndexError('No more results, the paginator is already exhausted')

        if not self._current_data_page and self._has_more:
            self._get_next_page()

        if not self._current_data_page:
            self._exhausted = True
            raise StopIteration()

        self._current_count += 1
        return self._current_data_page.pop(0)

    def __len__(self):
        """Approximate number of results, according to the API"""
        if self._total_count is None:
            self._total_count = self._get_total_count()
        return self._total_count

    def __repr__(self):
        limit = 3
        some = list(islice(self.all(), limit + 1))
        return '<%s %s%s>' % (
            self.__class__.__name__,
            ','.join(str(s) for s in some[:limit]),
            '...' if len(some) > limit else ''
        )
