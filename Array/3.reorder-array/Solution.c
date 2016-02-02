#include <stdio.h>
#include <stdlib.h>

void reorder_array_using_auxiliary_array(int arr[],int index[],int n){
	int temp[n],i;

	for(i=0;i<n;i++){
		temp[index[i]] = arr[i];
	}

	for(i=0;i<n;i++){
		arr[i]=temp[i];
		printf("%d ",arr[i]);
	}
	printf("\n");

}

int main(){
	int arr[] = {10,11,12};
	int index[] = {1,0,2};
	int n = sizeof(arr)/sizeof(arr[0]);
	reorder_array_using_auxiliary_array(arr,index,n);
	int arr1[]   = {50, 40, 70, 60, 90};
    int index1[] = {3,  0,  4,  1,  2};
    n = sizeof(arr1)/sizeof(arr1[0]);
    reorder_array_using_auxiliary_array(arr1,index1,n);
}