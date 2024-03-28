three = int(input("세 자리 정수를 입력하세요:"))
h = three // 100
t = three % 100 // 10
o = three % 100 % 10 // 1
print("백의 자리:", h)
print("십의 자리:", t)
print("일의 자리:", o)
