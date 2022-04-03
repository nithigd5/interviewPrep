import java.util.*;

class Main {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();
        SortedSet<Integer> l = new TreeSet<Integer>();
        for(int i=0;i<(n+m-1); i++){
            l.add(scan.nextInt());
        }
        for(Integer i: l){
            System.out.print(i+" ");
        }
        scan.close();
    }
}
