# 피보나치 수열 재귀함수로 나타내기

n = int(input("fibo(n)의 n을 입력하세요 :"))
def fibo(n) :
    if n == 1 or n == 0 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)
print('fibo({0}) = {1}'.format(n, fibo(n)))
