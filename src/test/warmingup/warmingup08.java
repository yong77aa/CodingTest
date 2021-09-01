package test.warmingup;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class warmingup08 {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] result = new int[n];
        
        
        for(int i = 0; i < n; i++){
            Integer[] list = new Integer[10];
            for(int j = 0 ; j < 10; j++) {
                list[j] = sc.nextInt();
            }
            Arrays.sort(list, Collections.reverseOrder());
            result[i] = list[2];
        }

        for(int i = 0; i<result.length; i++) {
            System.out.println(result[i]);
        }
        
    }
}
