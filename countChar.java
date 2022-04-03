import java.util.*;

class Main {
    public static void main(String args[]){
        String s = new Scanner(System.in).next();
        Map<Character, Integer> counts = new LinkedHashMap<>();
        for(char i:s.toCharArray()){
            if(counts.containsKey(i)){
                counts.replace(i, counts.get(i)+1);
            }else
            counts.put(i, 1);
        }
        int max = -999;
        char i = ' ';
        for(Map.Entry<Character, Integer> e : counts.entrySet()){
            if(e.getValue()>max){
                max = e.getValue();  
                i = e.getKey();  
            }
        }
        System.out.println(i);
    }
}
