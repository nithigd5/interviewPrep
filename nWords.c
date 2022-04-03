#include <stdio.h>
#include<string.h>

int wordsN()
{
    char string[100];
    scanf("%s",string);
    char c[10][10];
    int nums[10];
    int m[10] = {0}, n=0;
    int num = 0;

    for(int i=0;i<strlen(string);i++){
        if(string[i]>='A' && string[i]<='z'){
            if(num!=0){
                nums[n] = num;
                num = 0;
                n++;    
            }
            c[n][m[n]] = string[i];
            m[n]++;
            c[n][m[n]] = '\0';
        }else if(string[i]>='0' && string[i]<='9'){
            num = num*10 + (int) string[i] - '0';       
        }
    }
    if(num!=0){
        nums[n] = num;
        num = 0;
        n++;    
    }
    for(int i = 0; i<n; i++){
        for(int j = 0; j<nums[i]; j++)
            printf("%s\n",c[i]);
    }
    return 0;
}