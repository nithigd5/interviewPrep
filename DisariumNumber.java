import java.util.*;

class Main {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        int n = num;
        int i = 0, sum = 0;
        int a[] = new int[10];
        while(n!=0){
            a[i] = n%10;
            i ++;
            n = n/10;
        }
        int j = 1;
        for(int k = i-1;k>=0; k--){
            sum += Math.pow(a[k],j);
            j++;
        }
        if(sum == num){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }    
}
