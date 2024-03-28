m, n = map(int,input("변수 두 개를 입력해 주세요.").split())
def max2(m, n):
    if m > n :
        return m
    else :
        return n

def min2(m, n):
    if m < n :
        return m
    else :
        return n

print('100과 200 중 큰 수는 :', max2(m, n))
print('100과 200 중 작은 수는 :', min2(m, n))
