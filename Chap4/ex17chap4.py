a, b = map(int, input("정수 두 개를 입력하시오 :").split())
def range(a, b) :
    sum = 0
    i = a
    while i < b+1 :
        sum += i
        i += 1
    return sum

print("{0}에서 {1}까지의 정수의 합 : {2}".format(a, b, range(a,b)) )
