l = [2, 4, 9, 13, 19, 42, 84, 93, 102]
target = 42


def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    middle = (low + high) // 2

    if l[middle] == target:
        return middle
    elif l[middle] > target:
        return binary_search(l, target, low, middle-1)
    elif l[middle] < target:
        return binary_search(l, target, middle+1, high)


print(binary_search(l, target))
