#include<stdio.h>

int main(){
    int num;
    scanf("%d",&num);
    char bin[100];
    int i = 0;
    while(num!=0){
        int r = num%2;
        num = num/2;
        *(bin + i) = (char)r + '0';
        i++;
    }
    printf("%s",bin);
    return 0;
}