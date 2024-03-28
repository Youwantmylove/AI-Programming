# 소수값에 가장 가까운 단위 분수를 찾는 함수 구현

p = float(input("1보다 작고 0보다 큰 소수를 입력하세요 :"))
def fraction(nums) :
    n = 1
    n0 = 1.0
    while True :
        n1 = abs(1/n - nums)
        if n1 < n0 :
            n0 = n1
        else :
            break
        n += 1
    return n - 1

a = fraction(p)
print("가장 가까운 단위 분수는 1/{}이며, 이 값은 {}입니다.".format(fraction(p), 1/a))
