#########################
##### assignment.py #####
#########################

def Solution1(num):
    result = 0

    while num != 0:
        result += (num % 10)
        num //= 10

    return result


def Solution2(arr):
    keys = list(set(arr))
    counter = dict()

    for key in keys:
        counter.update({key: 0})

    for elementOfArr in arr:
        counter[elementOfArr] += 1

    result = list()
    maxValue = max(counter.values())

    for key in keys:
        if counter[key] == maxValue:
            result.append(key)

    if len(result) != len(counter):
        return result
    else:
        return []


if __name__ == "__main__":
    print(Solution1(5923))
    print(Solution2([1, 2, 3, 4, 5, 5]))
