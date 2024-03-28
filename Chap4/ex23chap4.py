# 반지름을 통해 원의 넓이와 둘레를 한 번에 계산하기

phi = 3.14
r = 1
while r > 0 :
    r = int(input("반지름을 입력하시오 :"))
    if r < 1 :
        print("프로그램을 종료합니다.")
        break
    else :
        s = phi*(r**2)
        l = 2*phi*r
        print("원의 넓이 : {:7.3f}, 원의 둘레 : {:7.3f}".format(s, l))      # 전체 7칸 중에서 소수점 아래 3칸까지 출력
