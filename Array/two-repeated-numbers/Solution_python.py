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
