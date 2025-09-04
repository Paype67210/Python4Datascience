def callLimit(limit: int):
    """ Limiter of another function execution."""
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwds):
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return None
            count += 1
            return function(*args, **kwds)
        return limit_function

    return callLimiter
