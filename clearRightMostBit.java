import java.util.*;

class Main {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();
        int i = 0, k = 1;
        while(i==0){
            i = n&k;
            k = k<<1;
        }
        k = k>>1;
        int res = n&(~k);
        System.out.println(res);
    }    
}
