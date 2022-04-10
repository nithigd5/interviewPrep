import java.util.*;

class Main {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int doorNos[] = {9,90,99,900,909,999,9000,9009,9099,9999,90000,90009,
            90099,99999,900000 ,900009, 900099, 900999,909999, 999999};
        for(int i = 0; i<doorNos.length; i++){
            if(doorNos[i]%n==0){
                System.out.println(doorNos[i]);
                break;
            }
        }
    }
}
