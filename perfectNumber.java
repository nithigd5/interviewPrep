import java.util.*;

class Main {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int sum = 0;
        for(int i = 1; i<n; i++){
            if(n%i==0){
                sum += i;
            }
        }
        if(n==sum){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}
