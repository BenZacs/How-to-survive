def unique(list):
    """Return a list containing only the first occurence of each distint
       element in list.  That is, all duplicates are omitted.

    Arguments:
        list: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(["b","a","a","b","b","b","a","a"])
    ['b', 'a']
    >>> unique([])
    []
    >>> unique(["s",2,2,5,"s","b","s","b",5,5,3])
    ['s', 2, 5, 'b', 3]
    """
    new_list = []
    for element in list:
        if element not in new_list:
            new_list.append(element)
    return new_list

if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
