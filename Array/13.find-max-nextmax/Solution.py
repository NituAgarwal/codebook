#finding elements in O(n)+O(n) = O(n) time complexity
def find_max_nextMax(arr):
	maxVal = arr[0]
	nextMaxVal = arr[0]
	for i in range(1,len(arr)):
		if maxVal<arr[i]:
			maxVal = arr[i]
	for i in range(1,len(arr)):
		if nextMaxVal < arr[i] and nextMaxVal< maxVal and arr[i]!=maxVal:
			nextMaxVal = arr[i]
	print maxVal,nextMaxVal

arr = [2,13,5,7,9,14,12,11]
find_max_nextMax(arr)



#finding elements in O(n) time complexity
def find_max_nextMax(arr):
	maxVal = arr[0]
	nextMaxVal = arr[0]
	for i in range(1,len(arr)):
		if maxVal<arr[i]:
			nextMaxVal = maxVal # first store the maxVal in nextmaxVal
			maxVal = arr[i] #Update maximum value
	print maxVal,nextMaxVal

arr = [2,13,5,7,9,14,12,11]
find_max_nextMax(arr)
