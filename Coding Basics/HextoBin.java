import java.util.*;

class HexToBin {
    public static void convert(String hex){
        long n = Long.parseLong(hex,16);
        String bin = "";
        while(n!=0){
            bin = n%2 + bin;
            n = n/2;
        }
        System.out.println(bin);
    }    
}
