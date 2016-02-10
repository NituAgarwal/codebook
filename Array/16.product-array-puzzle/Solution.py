#Solution with div operator
def product_array(arr):
	prod_arr = 1
	for i in range(0,len(arr)):
		prod_arr *=arr[i]
	prod = []
	for i in range(0,len(arr)):
		prod.append(prod_arr/arr[i])
	print prod

arr =[10,3,5,6,2]
product_array(arr)

#Solution without division operator in O(n) time complexity and O(1) space
def product_array_check(arr):
	left = 1
	right =1
	prod =[]
	#Multipying left and creating left array
	for i in range(1,len(arr)):
		prod.append(left)
		left *=arr[i-1]
	prod.append(left)
	# multiply all right and parallely multiply with product array
	for i in range(len(arr)-2,-1,-1):
		prod[i+1] *= right 
		right *=arr[i+1]
	prod[0]= right
	print prod

arr =[10,3,5,6,2]
product_array_check(arr)

