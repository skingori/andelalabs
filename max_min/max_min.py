list=[1,3,232,7,-7]
def find_max_min(number):
    mn = min(number)
    mx = max(number)

    if mn == mx:
        return number
    elif mn <= 0:
        return ("Negative not allowed")
    else:
        return [mn, mx]


print (find_max_min(list))
