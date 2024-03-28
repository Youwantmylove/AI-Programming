a = list(map(int, input("숫자를 입력하시오 :").split()))
def my_sort() :
    a.sort()            # 리스트 오름차순 정렬
    return a
print(my_sort())
