# 공백과 하이픈 제거 후 공백 없는 대문자로 저장, 문자 N 개수 나타내기

s1 = 'Kang Young Min'
s2 = '  Kang Young-Min'
s3 = 'Park Dong Min'
s4 = '  Park Dong-Yun'

s11 = s1.replace(" ", "")
s11 = s11.upper()

s22 = s2.strip()
s22 = s22.replace('-', '')
s22 = s22.replace(" ", "")
s22 = s22.upper()

s33 = s3.replace(" ", "")
s33 = s33.upper()

s44 = s4.strip()
s44 = s44.replace('-', '')
s44 = s44.replace(" ", "")
s44 = s44.upper()

print("{0}(은)는 {1}(으)로 수정됨".format(s1, s11))
print("{0}(은)는 {1}(으)로 수정됨".format(s2, s22))
print("{0}(은)는 {1}(으)로 수정됨".format(s3, s33))
print("{0}(은)는 {1}(으)로 수정됨".format(s4, s44))

print("{0} : {1} 개의 N이 나타남".format(s11, s11.count('N')))
print("{0} : {1} 개의 N이 나타남".format(s22, s22.count('N')))
print("{0} : {1} 개의 N이 나타남".format(s33, s33.count('N')))
print("{0} : {1} 개의 N이 나타남".format(s44, s44.count('N')))
