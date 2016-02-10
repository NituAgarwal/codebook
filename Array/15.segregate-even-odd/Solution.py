#Solution in O(n)
def segregate_even_odd(arr):
	i=0
	j=len(arr)-1
	while i<=j:
		if arr[i]%2 ==0:
			i +=1
		elif arr[j]%2 !=0 : 
			j -=1
		else:
			arr[i],arr[j] = arr[j],arr[i] 
	print arr

arr = [12, 34, 45, 9, 8, 90, 3]
segregate_even_odd(arr)