import java.util.*;
class Main {
    public static void main(String args[]){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        Integer a[] = new Integer[n];
        for(int i=0;i<n;i++){
            a[i] = s.nextInt();
        }
        Arrays.sort(a,0,n);
        Arrays.sort(a,n/2,n, Collections.reverseOrder());
        for(int i = 0; i<n; i++) {
            System.out.print(a[i] + " ");
        }
    }
}
