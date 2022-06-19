##########################
##### assignment1.py #####
##########################

import time


# 재귀 함수를 이용한 피보나치 계산 함수로, 숫자값을 입력받습니다.
def Fibo(n):
    if n <= 1:
        return n

    return Fibo(n - 1) + Fibo(n - 2)


# 반복문을 이용한 피보나치 계산 함수로, 숫자값을 입력받습니다.
def IterFibo(n):
    a, b = 1, 1

    if n <= 1:
        return n

    for i in range(2, n):
        a, b = b, a + b

    return b


if __name__ == "__main__":
    def _main():
        while True:
            # 작업 대상인 숫자값을 입력받습니다.
            num = int(input("Enter a number: "))

            # 들어온 숫자가 음수면 프로그램을 종료합니다.
            if num < 0:
                break

            # 재귀 함수를 이용한 피보나치 계산을 수행합니다.
            timePoint = time.time()
            calculationResult = Fibo(num)
            timePoint = time.time() - timePoint

            # 재귀 함수를 이용한 피보나치 계산 수행 결과와 걸린 시간을 출력합니다.
            print("Fibo(%d) : %d, Estimated Time : %.6f" % (num, calculationResult, timePoint))

            # 반복문을 이용한 피보나치 계산을 수행합니다.
            timePoint = time.time()
            calculationResult = IterFibo(num)
            timePoint = time.time() - timePoint

            # 반복문을 이용한 피보나치 계산 수행 결과와 걸린 시간을 출력합니다.
            print("IterFibo(%d) : %d, Estimated Time : %.6f" % (num, calculationResult, timePoint))

    _main()
