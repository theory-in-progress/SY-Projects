#include <stdio.h>
int main()
{
    int arr[]={7,0,7,2,0,3,0,4,2,3,0,3,2},i=0;
    int s0=-1,s1=-1,s2=-1,s3=-1;
    int miss=0,hit=0;
    for(i;i<13;i++){
        printf("%d\t%d\t%d\t%d\n",s0,s1,s2,s3);
        if(s3==-1){
            s3=arr[i];
            miss++;
            continue;
        }
        else if(s2==-1){
            if(s3==arr[i]){
                hit++;
                continue;
            }
            s2=s3;
            s3=arr[i];
            miss++;
            continue;
        }
        else if(s1==-1){
            if(s3==arr[i]){
                hit++;
                continue;
            }
            if(s2==arr[i]){
                hit++;
                int temp=s3;
                s3=s2;
                s2=temp;
                continue;
            }
            s1=s2;
            s2=s3;
            s3=arr[i];
            miss++;
            continue;
        }
        else if(s0==-1){
            if(s3==arr[i]){
                hit++;
                continue;
            }
            if(s2==arr[i]){
                hit++;
                int temp=s3;
                s3=s2;
                s2=temp;
                continue;
            }
            if(s1==arr[i]){
                hit++;
                int temp=s3;
                s3=s1;
                s1=s2;
                s2=temp;
                continue;
            }
            s0=s1;
            s1=s2;
            s2=s3;
            s3=arr[i];
            miss++;
            continue;
        }
        else if(arr[i]==s3){
            hit++;
            continue;
        }
        else if(arr[i]==s2){
            int temp=s3;
            s3=s2;
            s2=temp;
            hit++;
            continue;
        }
        else if(arr[i]==s1){
            int temp=s3;
            s3=s1;
            s1=s2;
            s2=temp;
            hit++;
            continue;
        }
        else if(arr[i]==s0){
            int temp=s3;
            s3=s0;
            s0=s1;
            s1=s2;
            s2=temp;
            hit++;
            continue;
        }
        else{
            int temp=s3;
            s3=arr[i];
            s0=s1;
            s1=s2;
            s2=temp;
            miss++;
            continue;
        }
    }
    printf("%d\t%d\t%d\t%d\nhit=%d\tmiss==%d",s0,s1,s2,s3,hit,miss);
    return 0;
}