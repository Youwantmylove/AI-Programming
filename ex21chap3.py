n = int(input("숫자를 입력하세요 :"))
m = True
for i in range(2, n) :
    if n % i == 0 :
        m = False
if m == False :
    print(n, "은 소수가 아닙니다.")
else :
    print(n, "은 소수입니다.")
