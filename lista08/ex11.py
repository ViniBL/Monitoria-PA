def sum(lst):
    if not len(lst):
        return 0
    if isinstance(lst[0], list):
        return sum(lst[0]) + sum(lst[1:])
    return lst[0] + sum(lst[1:])
