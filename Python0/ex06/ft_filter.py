def ft_filter(function, iterable):
    """
    Construct an iterator from those elements of iterable for which function returns true.
    ft_filter(function, iterable) --> filter object
    """
    return (item for item in iterable if function(item))
