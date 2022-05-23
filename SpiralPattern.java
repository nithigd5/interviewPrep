import java.util.*;

class Main {
    static int min(int num1, int num2, int num3, int num4){
        int e = num1>num2?num2:num1;
        int f = num3>num4?num4:num3;
        return e>f?f:e;
    }
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        for(int i = 0; i<n*2-1;i++){
            for(int j = 0; j<n*2-1;j++){
                int x = min(i, j, (n*2-2)-i, (n*2-2)-j);
                System.out.print((n-x)+" ");
            }  
            System.out.println();
        }
        scan.close();
    }
}
