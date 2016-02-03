#Solution in O(n) space and O(n) time 
def majority_element(arr):
	arr_length = len(arr)
	count={}
	for i in arr:
		if i in count:
			count[i] +=1
		else:
			count[i] = 1
	for i in count:
		if count[i] > arr_length/2:
			print i
			return
	print "Majority Element does not exist"

arr= [3,3,4,2,4,4,2,4,4]
majority_element(arr)

#Solution in O(n) time

def majority_element_solution(arr):
	count = 1
	maj_index = 0
	for i in range(1,len(arr)):
		if arr[i] ==arr[maj_index]:
			count +=1
		else :
			count -=1
		if count== 0:
			maj_index = i
			count +=1
	if arr.count(arr[maj_index]) > len(arr)/2:
		print arr[maj_index]
	else:
		print "Majority Element does not exist"

arr= [3,3,4,2,4,4,2,4,4]
majority_element_solution(arr)
