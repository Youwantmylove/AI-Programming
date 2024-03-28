a, b, c = map(int,input("세 수를 입력하시오 :").split())
def mean3(a, b, c) :
        mean = (a + b + c) / 3
        return mean
def max3(a, b, c) :
    if a > b and a > c :
        return a
    elif b > a and b > c :
        return b
    else :
        return c
def min3(a, b, c) :
    if a < b and a < c :
        return a
    elif b < a and b < c :
        return b
    else :
        return c
print(a, b, c, "의 평균값은", mean3(a, b, c))
print(a, b, c, "의 최댓값은", max3(a, b, c))
print(a, b, c, "의 최솟값은", min3(a, b, c))
