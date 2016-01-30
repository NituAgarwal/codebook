arr = [3, 7, 90, 20, 10, 50, 40]
k = 3
curr_sum = 0
min_sum =0
i=0
res_index = 0
while i<k:
	curr_sum +=arr[i]
	i = i+1
min_sum = curr_sum
while i <len(arr):
	curr_sum += arr[i] - arr[i-k]
	if curr_sum < min_sum:
		min_sum = curr_sum
		res_index = i-k+1
	i = i+1
print "the resultant index is ",(res_index,res_index+k-1)
