n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
min_val = -1
for elem in nums[1:]:
        if nums.count(elem) == 1:
                if min_val < elem:
                        min_val = elem

print(f"{min_val}")


