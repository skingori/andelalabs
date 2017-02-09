def find_missing(l1, l2):
    if not l1 and l2:
        return 0

    diff = list(set(l1) ^ set(l2))
    if not diff:
        return 0
    return diff[0]
