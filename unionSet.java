import java.util.*;

class Main {
    public static void main(String args[]){
        SortedSet<Integer> intSet = new TreeSet<Integer>();
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();
        for(int i=0;i<n;i++)
           intSet.add(scan.nextInt());
        for(int i=0;i<m;i++)
           intSet.add(scan.nextInt());
        for( Integer e: intSet ){
            System.out.print(e+" ");
        }
    }
}
