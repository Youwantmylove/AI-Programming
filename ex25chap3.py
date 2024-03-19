# 하루 종일 올라가면 7, 밤중 휴식하는 동안 -5
snail = 0
day = 0
while snail <= 30 :
    snail += 7
    day += 1
    print("Day", day, "달팽이의 위치:", snail, "미터")
    if snail <= 29 :
        snail -= 5
print("우물을 탈출하는 데 걸린 날은", day, "일입니다.")
