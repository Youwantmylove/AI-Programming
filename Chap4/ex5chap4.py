a = int(input("인치 값을 입력해 주세요.:"))
def inch2cm() :
    b = (a * 2.54) / 1
    return b
print(a, "inch는 cm로 변환하면", inch2cm(), "cm입니다.")
