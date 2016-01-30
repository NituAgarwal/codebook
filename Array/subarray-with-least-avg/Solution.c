#include <stdio.h>
#include <stdlib.h>

void findMinSubArray(int arr[],int n,int k){
	int res_index=0;
	int i,min_sum =0;
	int sum;

	if(n<k){
		return;
	}
	for(i=0;i<k;i++){
		min_sum += arr[i];
	}
	sum = min_sum;

	for(i=k;i<n;i++){
		sum += arr[i] - arr[i-k];
		if(sum<min_sum){
			min_sum = sum;
			res_index = i-k+1;
		}
	}
	double avg = (double)min_sum/k;
	printf("The resultant index is [%d, %d]", res_index ,res_index+k-1);
	printf("Minimum average is %f ", avg);
}

int main(){
	int arr[] = {3, 7, 90, 20, 10, 50, 40};
	int k;
	printf("Enter Subset\n");
	scanf("%d",&k);
	int n = sizeof(arr)/sizeof(arr[0]);
	findMinSubArray(arr,n,k);
	return 0;
}