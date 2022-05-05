import java.util.*;
import java.util.concurrent.TimeUnit;

class Sort{
    public static void main(String args[]) throws InterruptedException {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for (int i = 10000000; i>0; i--)
            arr.add(i);
        long start = System.currentTimeMillis();
        Collections.sort(arr);
        long end = System.currentTimeMillis();
        double endTime = (double)(end - start)/1000;
        System.out.print("Total Time taken: "+endTime+" seconds");
    }
}