import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.Stream;
class Main {
    public static void main(String args[]){
        Set<Character> l = new LinkedHashSet<>();
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        for(Character e: s.toCharArray()){
            l.add(e);
        }
        for(Character e: l){
            System.out.print(e);
        }
    }
}
