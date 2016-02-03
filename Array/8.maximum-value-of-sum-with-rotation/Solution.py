def max_sum_with_right_rotation(arr):
	n = len(arr)
	arr_sum = sum(arr)
	# Find sum of i*a[i] fro existing array
	current_rotation_sum = sum([i*arr[i] for i in range(0,len(arr))])
	max_sum = current_rotation_sum
	for i in range(1,n):
		current_rotation_sum = current_rotation_sum +arr_sum - n*arr[n-i]
		if max_sum < current_rotation_sum:
			max_sum = current_rotation_sum
	return max_sum

arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print max_sum_with_right_rotation(arr)
arr = [1,20,2,10]
print max_sum_with_right_rotation(arr)