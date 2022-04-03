import java.util.*;

class Main {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int s1 = 0, s2 = 0;
        for(int i = 1; i<Math.max(a, b);i++){
            if(a%i==0 && i!=a){
                s1 += i;
            }
            if(b%i == 0 && i!=b){
                s2 += i;
            }
        }
        if(s1 == b && s2 == a){
            System.out.println("Yes");
        }else System.out.println("No");
    }
}
