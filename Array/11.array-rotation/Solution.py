def array_rotate(arr,d):
	for i in range(0,d):
		temp=arr.pop(0) # arr.pop(0) is equivalent to arr=arr[1:len(arr)]
		arr.append(temp)
	return arr

arr = [1,2,3,4,5,6,7]
print array_rotate(arr,2)