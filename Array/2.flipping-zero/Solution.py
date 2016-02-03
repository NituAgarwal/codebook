def flipping_zeros(arr,num):
	arr_length = len(arr)
	left = 0
	right = left
	zerocount = 0
	countSum =0
	maxSum =0
	totalzerocount = arr.count(0)
	if num>=totalzerocount:
		print "All zeros can be flipped"
		for i in range(0,arr_length):
			if arr[i]==0:
				print i
		return
	while right<arr_length:
		if zerocount<num and arr[right]==0:
			zerocount +=1
			right +=1
		if zerocount==num and arr[right]==0 :
			zerocount -=1
			left +=1
		if (right-left) > maxSum:
			maxSum = right-left
			indexleft = left
			indexright = right
		if right < arr_length and arr[right]==1:
			right +=1
	for i in range(indexleft,indexright):
		if arr[i]==0:
			print i

arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
m=1
flipping_zeros(arr,m)