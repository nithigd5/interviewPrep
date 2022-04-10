import java.util.*;

class Main{
    static boolean isPrime(int n){
        for(int i=2;i<n;i++){
            if(n%2==0) return false;
        }
        return true;
    }
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        HashMap<Integer, Integer> factors = new LinkedHashMap<>();
        int i = 2;
        while(num>1){
            if(isPrime(i)){
                if(num%i==0){
                    num /=i;
                    if(factors.containsKey(i)){
                        factors.replace(i, factors.get(i)+1);
                    }else factors.put(i,1);
                }else{
                    i++;
                }
            }else{
                i++;
            }
        }
        for(Map.Entry<Integer, Integer> e: factors.entrySet()){
            for(int j = 0; j<e.getValue(); j++)
            System.out.print(e.getKey() + " ");
        }
        scan.close();
    }
}