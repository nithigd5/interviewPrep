#include<stdio.h>

void EiffleTower(){
    int n;
    scanf("%d",&n);
    
    for(int i = 0; i<n; i++){
        for(int j = 0; j< n - i; j++){
            for(int k = 0; k <= i*1 + i; k++ ){
                printf("%d",i+1);
            }
            printf("\n");
        }
    }

}