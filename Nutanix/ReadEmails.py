nums = [1,1,0,0,1]
nums1 = [0,0]
def read_emails(nums):
  i = 0
  ans = 0
  while i < len(nums):
    count = 0
    if nums[i] == 1:
      while i < len(nums) and nums[i] == 1:
        count += 1
        i += 1
      ans += count + 1
    i += 1
  return ans - 1 if ans > 1 else ans

print(read_emails(nums))
print(read_emails(nums1))

