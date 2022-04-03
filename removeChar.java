import java.util.*;

class Main {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        String c = scan.next();
        s = s.replace(c, "");
        System.out.println(s);
        System.out.println(c);
        scan.close();
    }
}
