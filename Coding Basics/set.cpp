#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    unordered_set<int> set;
    for(int i = 0; i<10000000; i++){
        set.insert(i);
    }
    cout<<sizeof((*set.begin()))*set.size();
    int size = 0;
}