#Adding solution for count inversion in O(n^3)
def count_inversion(arr,k):
	n=len(arr)
	count =0
	for i in range(0,n-k+1):
		for j in range(i+1,n-k+2):
			if arr[i]>arr[j]:
				for k in range(j+1,n):
					if arr[j]>arr[k]:
						count +=1
	print count

arr = [8,4,2,1]
k=3
count_inversion(arr,k)

#Solution in O(n^2)
def count_inversion_efficient(arr,k):
	n =len(arr)
	count =0
	for i in range(1,n):
		small = 0
		for j in range(i+1,n):
			if arr[j] < arr[i] :
				small +=1
		great =0
		for j in range(i-1,-1,-1):
			if arr[j] > arr[i]:
				great +=1
		count += small*great
	print count

arr = [8,4,2,1]
k=3
count_inversion_efficient(arr,k)



