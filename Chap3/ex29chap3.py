fir = 500
ten = 50
while ten >= 10 :
    men = int(input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오:"))
    fir += men
    ten = fir / 10
    if ten >=  10 :
        print('현재 탱크양은', fir, '입니다.')
        ten * 100
    elif ten < 10 :
        print('현재 탱크양은', fir, '입니다.')
        print('경고 : 연료가 10% 미만이니 충전하세요!')
        break
        
