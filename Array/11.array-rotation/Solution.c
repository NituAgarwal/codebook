#include <stdio.h>
#include <stdlib.h>

void array_rotation(int arr[],int d,int n){
	int i = 0,j=0;
	int temp[n];
	while(i<d){
		temp[i] = arr[i];
		i++;
	}
	for(i=0;i<n-d;i++){
		arr[i] = arr[i+d];
		printf("%d ",arr[i]);
	}
	while(i<n && j<d){
		arr[i] = temp[j];
		printf("%d ",arr[i]);
		i++;
		j++;
	}
}

int main(){
	int arr[] ={1,2,3,4,5,6,7};
	int n = sizeof(arr)/sizeof(arr[0]);
	int d=2;
	array_rotation(arr,d,n);
}