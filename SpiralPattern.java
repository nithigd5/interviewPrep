import java.util.*;

class Main {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        for(int i = 1; i<n*2;i++){
            for(int j = 1; j<n*2;j++){
                if(i>1&&i<n*2-1 && j>1 && j<n*2-1)
                System.out.print(n-1 + " ");
                else
                System.out.print(n + " ");
            }  
            System.out.println();
        }
        scan.close();
    }
}
