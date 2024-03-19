# 친화수는 서로의 약수를 합해 서로가 나오는 수를 말한다.
# 친화수 찾는 함수 정의

for n in range(2, 20000) :
    i = 2     # 1을 제외한 약수 후보 숫자
    m = 1     # 1부터 시작하는 n의 total 값
    while i < n :
        if n % i == 0 :
            m += i
        i += 1    # i가 n보다 같아지기 전까지 증가

# m에서 합이 같은 숫자 찾기

    i = 2    # 짝을 이루는 값을 찾기 위한 약수 후보 숫자
    t = 1    # 1부터 시작하는 n의 total 값
    while i < m :
        if m % i == 0 :
            t += i
        i += 1
    if t == n :
        if m == n :
            print(m, '은 완전수입니다.')
        else :
            print(m, "의 친화수", n)
