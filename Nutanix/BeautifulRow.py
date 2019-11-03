from bisect import bisect_left

def lis(arr):
	stack = [arr[0]]
	len_stack = 1
	lis_arr = [1] * len(arr)
	for i, num in enumerate(arr[1::]):
		if stack and num > stack[-1]:
			stack.append(num)
			len_stack += 1
		else:
			idx = bisect_left(stack, num)
			stack[idx] = num
		lis_arr[i+1] = len_stack
	return lis_arr

def beautiful_row(arr):
	left_lis = lis(arr)
	right_lis = lis(arr[::-1])
	right_lis = right_lis[::-1]
	max_beautiful = 0
	for i in range(len(arr)):
		beautiful_len = left_lis[i] + right_lis[i] - 1
		max_beautiful = max(max_beautiful, beautiful_len)
	return len(arr) - max_beautiful

assert(beautiful_row([3,17,4,12,5,6,2,1]) == 2), 'test 1 failed'
assert(beautiful_row([1,2,100,99]) == 0), 'test 2 failed'
