age = int(input("나이가 어떻게 되세요?"))
if age < 20 :
    print("청소년 할인 가능하세요~")
if age > 60 :
    print("경로 우대 가능하세요~")
else :
    print("할인은 따로 불가하세요~")
print("환영합니다~")

age = int(input("나이가 어떻게 되세요?"))
if age < 20 :
    print("청소년 할인 가능하세요~")
elif age < 60 :
    print("할인은 따로 불가하세요~")
else :
    print("경로 우대 할인 가능하세요~")
print("환영합니다~")
