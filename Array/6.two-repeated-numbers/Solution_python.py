#Solution 1 by Hashing- Count Array - O(n) time complexity and O(n) space
def get_two_repeated_numbers(arr,n):
	mapNumber = dict()
	for i in range(1,n+1):
		mapNumber[i] = 0
	for i in arr:
		if mapNumber[i]:
			print i
		else:
			mapNumber[i] = mapNumber[i] + 1

arr = [4, 4, 2, 5, 2, 3, 1]
n=5
get_two_repeated_numbers(arr,n)


#Second Solution By negating values - O(n) time complexity
def get_two_repeated_numbers_second(arr,n):
	for i in range(0,n+2):
		if arr[abs(arr[i])] > 0:
			arr[abs(arr[i])] = -arr[abs(arr[i])]
		else:
			# If arr[abs(arr[i])]<0 then it means it is already visited and thus the duplicate
			print abs(arr[i])

arr = [4, 4, 2, 5, 2, 3, 1]
n=5
get_two_repeated_numbers_second(arr,n)
