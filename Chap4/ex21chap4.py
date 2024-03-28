# 주민등록번호 생년월일 날짜로 출력하기

six = int(input("주민등록번호 첫 6숫자 형식 입력 :"))
a = six // 10000
b = six % 10000 // 100
c = six % 10000 % 100 // 1
if a > 50 :
    print("19{0}년 {1}월 {2}일".format(a, b, c))
elif a < 10 :
    print("200{0}년 {1}월 {2}일".format(a, b, c))
else :
    print("20{0}년 {1}월 {2}일".format(a, b, c))
