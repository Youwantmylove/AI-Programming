nums = list(map(int,input("정수를 여러 개 입력하시오 :").split()))
mean = sum(nums) / len(nums)
mean1 = round(mean, 1)
print("평균값은", mean1)
print("최댓값은", max(nums))
print("최솟값은", min(nums))
