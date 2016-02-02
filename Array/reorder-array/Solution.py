#Reorder elements in arr based on index array
def reorder_array(arr,index):
	for i in range(0,len(arr)):
		arr[index[i]],arr[i]=arr[i],arr[index[i]]
		index[index[i]],index[i]=index[i],index[index[i]]
	print arr
	print index

arr = [10, 11, 12];
index= [1, 0, 2];
reorder_array(arr,index)
