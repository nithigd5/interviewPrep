import java.util.*;

class Main {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        Long n = scan.nextLong();
        scan.close();
        String bin = "";
        while(n!=0){
            bin = n%2 + bin;
            n = n/2;
        }
        System.out.println(bin);
    }    
}
