def pair_with_sum(arr,givenSum):
	arr.sort()
	left=0
	right = len(arr)-1
	flag = False
	while(left<right):
		if arr[left] + arr[right] == givenSum:
			print arr[left],arr[right]
			flag = True
			return
		if arr[left] + arr[right] >givenSum:
			right -=1
		else : 
			left +=1
	if flag == False:
		print "No Such Pair exist"

arr = [1, 4, 45, 6, 10, -8]
givenSum = 16
pair_with_sum(arr,givenSum)