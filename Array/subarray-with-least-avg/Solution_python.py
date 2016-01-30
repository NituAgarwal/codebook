def find_min_sub_array(arr,n,k):
	if n<k:
		return
	curr_sum = sum(arr[:k]) # add first k items of array
	min_sum = curr_sum
	res_index=0
	i=k
	while i<n:
		# Add current item arr[i] and remove first item of the sub array
		curr_sum += arr[i] - arr[i-k]
		if curr_sum< min_sum:
			min_sum = curr_sum
			res_index = i-k+1
		i= i+1
	print "the resultant index is ",(res_index,res_index+k-1)

arr = [3, 7, 90, 20, 10, 50, 40]
k = 3
find_min_sub_array(arr,len(arr),k)