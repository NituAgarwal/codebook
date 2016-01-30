def get_count_triplets(arr,n,checkSum):
	#sort the array
	arr.sort()
	count = 0  # to track count of triplets
	i=0
	while i < n-2:
		j=i+1
		k=n-1
		while j<k:
			#check if sum of arr[i],arr[j],arr[k] is greater or equal to checkSum
			if arr[i]+arr[j]+arr[k] >= checkSum:
				k = k -1 #decrement k if triplet sum greater than k as it is sorted array
			else:
				count = count + (k-j)
				j = j+1
		i = i +1
	print "count is ",count

arr = [5, 1, 3, 4, 7]
givenSum = 12
get_count_triplets(arr,len(arr),givenSum)