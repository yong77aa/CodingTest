package test.greedy;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;



public class greedy01 {
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(bf.readLine());
        int[] array = new int[k];


        for(int i = 0; i < k; i++){
            array[i] = Integer.parseInt(bf.readLine());
        }
        Arrays.sort(array);

        int totaltime = 0;
        int personTime = 0;
        for(int i = 0; i<array.length; i++){
            personTime += array[i];
            totaltime += personTime;
        }

        System.out.println(totaltime);
    }
    
}
