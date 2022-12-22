A, P = map(int, input().split())
nums = [A]
while True:
 tmp = 0
 for s in str(nums[-1]):
     tmp += int(s) ** P
 if tmp in nums:
     break
 nums.append(tmp)
print(nums.index(tmp))