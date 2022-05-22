import java.util.*;

class Main{
public static void main(String args[]){      
    int n = new Scanner(System.in).nextInt();
    int fact = 1;
    for (int i = 1; i <=n; i++)
    fact *= i;
    System.out.println(fact);
}}      