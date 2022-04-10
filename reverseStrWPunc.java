import java.util.*;
import java.util.Map.Entry;

class Main {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        String str = scan.nextLine();
        int l = str.length();
        StringBuilder rev = new StringBuilder();
        
        // TreeMap<Integer, Character> specials = new TreeMap<Integer, Character>();
        int j = 0;
        for(int i=0; i<l;i++){
            if((str.charAt(i)>='a' && str.charAt(i)<='z') | (str.charAt(i)<='Z' &&  str.charAt(i)>='A' ) ){
                rev.insert(j,str.charAt(i));
            }else{
                j = i+1;
                // specials.put(i, str.charAt(i));
                rev.insert(i,str.charAt(i));
            }
        }
        // for(Map.Entry<Integer,Character> e : specials.entrySet()){
        //     rev.insert(e.getKey(), e.getValue().toString());
        // }
        System.out.println(rev);
        scan.close();
    }
}
