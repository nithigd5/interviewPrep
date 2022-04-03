import java.util.*;

class Main {
    static int[] decimalToBinary(int num){
        int bin[] = new int[100];
        int i = 0;
        while(num!=0){
            int r = num%2;
            num = num/2;
            bin[i] = r;
            i++;
        }
        return bin;
    }
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        int bits[] = decimalToBinary(num);
        int s = 0;
        for(int b : bits){
            if(b==1) s += 1;
        }
        System.out.println(s);
    }
}
