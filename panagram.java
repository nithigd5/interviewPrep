import java.util.*;

class Main{
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        char alphabets[] = new char[26];
        s= s.toUpperCase();
        int j =  0;
        for(char e: s.toCharArray()){
            int i = (int)e - 65;
            if(i>=0 && i<26 && alphabets[i]==0){
                alphabets[i] = 1;
                j +=1;
            }
        }
        if(j>=24){
            System.out.println("TRUE");
        }else{
            System.out.println("FALSE");
        }
        scan.close();       
    }
}