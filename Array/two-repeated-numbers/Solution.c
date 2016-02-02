#include <stdio.h>
#include <stdlib.h>

void get_repeated_numbers(int arr[],int n){
	for(int i=0;i<n;i++){
		if(arr[abs(arr[i])] > 0){
			arr[abs(arr[i])]= -arr[abs(arr[i])];
		}
		else{
			//If arr[abs(arr[i])]<0 then it means it is already visited and thus the duplicate
			printf("%d ",abs(arr[i]));
		}
	}
}

int main(){
	int arr[] = {4, 4, 2, 5, 2, 3, 1};
	int n = sizeof(arr)/sizeof(arr[0]);
	get_repeated_numbers(arr,n);

	return 0;

}