#include <stdio.h>
#include <stdlib.h>

void get_count_triplets(int arr[],int n,int sum){
	int i=0,count = 0,j,k;
	
	for(i=0;i<n-2;i++){
		j=i+1;
		k=n-1;
		while(j<k){
			if(arr[i]+arr[j]+arr[k] >= sum){
				k--;
			}
			else{
				// if countSum<sum then all the pair of j with k will be smaller than sum
				count += (k-j);
				j++;
			}
		}
	}

	printf("Count is %d\n",count);
}

int comp (const void * elem1, const void * elem2) 
{
    int f = *((int*)elem1);
    int s = *((int*)elem2);
    if (f > s) return  1;
    if (f < s) return -1;
    return 0;
}
int main(){
	int arr[]= {5, 1, 3, 4, 7};
	int n = sizeof(arr)/sizeof(arr[0]);
	//stdlib method qsort to sort an array
	qsort (arr, n, sizeof(*arr), comp);
	int given_sum = 12;
	//After sorting get count of triplets
	get_count_triplets(arr,n,given_sum);
	return 0;
}
