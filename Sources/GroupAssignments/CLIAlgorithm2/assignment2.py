##########################
##### assignment2.py #####
##########################

import time
import random


# 선형 탐색 작업을 수행하는 함수로, 작업 대상과 찾아 낼 타겟을 받습니다.
def linearSearch(data, target):
    for pointer in range(len(data)):
        if data[pointer] == target:
            return pointer

    return None


# 재귀 함수를 이용한 이진 탐색 작업을 수행하는 함수로, 작업 대상, 탐색 시작 인덱스와 끝지점, 마지막으로 찾아 낼 타겟을 받습니다.
def binarySearch(data, lower, upper, target):
    if lower > upper:
        return None

    pointer = (lower + upper) // 2

    if data[pointer] == target:
        return pointer
    elif data[pointer] < target:
        return binarySearch(data, pointer + 1, upper, target)
    else:
        return binarySearch(data, lower, pointer - 1, target)


if __name__ == "__main__":
    def _main():
        # 탐색 대상인 리스트의 크기를 입력받습니다.
        sizeOfData = int(input("Enter the size of array: "))

        # 작업 대상인 리스트를 선언 후 아무 수를 집어넣습니다.
        data = []
        for i in range(sizeOfData):
            data += [random.randint(0, 99999)]

        # 리스트를 정렬합니다.
        data.sort()

        # 작업 대상에서 찾을 타겟을 설정합니다.
        target = data[random.randint(0, len(data) - 1)]

        # 선형 탐색 작업을 수행합니다.
        timePoint = time.time()
        calculationResult = linearSearch(data, target)
        timePoint = time.time() - timePoint

        # 선형 탐색 수행 결과와 걸린 시간을 출력합니다.
        if calculationResult is not None:
            print("Target is Found!, Data is Located at [%d], Estimated Time of Linear Search : %.6f" % (calculationResult, timePoint))
        else:
            print("Target is Not Found!, Estimated Time of Linear Search : %.6f" % timePoint)

        # 재귀 함수를 이용한 이진 탐색 작업을 수행합니다.
        timePoint = time.time()
        calculationResult = binarySearch(data, 0, len(data) - 1, target)
        timePoint = time.time() - timePoint

        # 재귀 함수를 이용한 이진 탐색 작업을 수행 결과와 걸린 시간을 출력합니다.
        if calculationResult is not None:
            print("Target is Found!, Data is Located at [%d], Estimated Time of Binary Search : %.6f" % (calculationResult, timePoint))
        else:
            print("Target is Not Found!, Estimated Time of Binary Search : %.6f" % timePoint)

    _main()
