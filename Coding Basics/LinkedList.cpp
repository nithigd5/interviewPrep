#include<iostream>
using namespace std;

struct node {
    int data;
    struct  node* next;
};

int main(){
    struct node head;
    head.data = 4;
    printf("%d", sizeof(head));
}