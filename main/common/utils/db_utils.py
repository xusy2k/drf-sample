import functools
import logging
import time

from django.db import connection
from django.db import reset_queries

log = logging.getLogger(__name__)


def debugger_queries(func):
    """Basic function to debug queries."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        reset_queries()

        start = time.time()
        start_queries = len(connection.queries)

        result = func(*args, **kwargs)

        end = time.time()
        end_queries = len(connection.queries)

        log.info(f">>> DEBUG QUERY - Function : {func.__qualname__}")
        log.info(f">>> DEBUG QUERY - Number of Queries : {end_queries - start_queries}")
        log.info(f">>> DEBUG QUERY - Finished in : {(end - start):.2f}s")
        log.info("")
        return result

    return wrapper


class QueryCountDebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        reset_queries()
        start_queries = len(connection.queries)
        start = time.perf_counter()
        response = self.get_response(request)
        end = time.perf_counter()
        end_queries = len(connection.queries)
        log.info(f">>> DEBUG QUERY - URI : {request.get_full_path()}")
        log.info(f">>> DEBUG QUERY - Number of Queries : {end_queries - start_queries}")
        log.info(f">>> DEBUG QUERY - Finished in : {(end - start):4f}s")
        log.info("")
        return response
