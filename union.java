import java.util.*;

class Main {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        Set<Integer> union = new TreeSet<Integer>();
        for(int i = 0; i<a; i++){
            union.add(scan.nextInt());
        }
        int com = 0;
        for(int i = 0; i<b; i++){
            if(!union.add(scan.nextInt())) com +=1;
        }
        if(com == 0) {
            System.out.print(-1);
            System.exit(0);
        }
        for(Integer i : union){
            System.out.print(i+" ");
        }
        scan.close();
    }
}
