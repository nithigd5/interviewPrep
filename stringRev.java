import java.util.*;

class Main {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        String s[] = scan.nextLine().split(" ");
        for(int i=s.length-1; i>=0;i--){
            System.out.print(s[i]+" ");
        }
        
    }
}
