def merge_array(arr1,arr2,NA):
	arrLen = len(arr1)
	j=arrLen-1
	#Move elements of arr1 to end
	for i in range(arrLen-1,-1,-1):
		if arr1[i] != NA:
			arr1[j]=arr1[i]
			j -=1
	#Merge Array. Start i from len(arr2) as after this only all the values from arr1 will be available
	j=0
	i=len(arr2)
	for k in range(0,arrLen):
		if (i<arrLen and arr1[i]<arr2[j]) or j==len(arr2):
			arr1[k] = arr1[i]
			i +=1
		else:
			arr1[k] = arr2[j]
			j +=1
	print arr1

NA = -1
arr1=[2,NA,7,NA,NA,10,NA]
arr2= [5,8,12,14]
merge_array(arr1,arr2,NA)

arr1 =[2, 8, NA, NA, NA, 13, NA, 15, 20]
arr2 = [5, 7, 9, 25]
merge_array(arr1,arr2,NA)