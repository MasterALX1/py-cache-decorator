import collections
from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key not in cached_results:
            print("Calculating new result")
            cached_results[key] = func(*args, **kwargs)
            return cached_results[key]
        print("Getting from cache")
        return cached_results[key]

    return wrapper
