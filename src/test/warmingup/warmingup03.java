package test.warmingup;

import java.util.Arrays;
import java.util.Scanner;

public class warmingup03 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] array = new int[n];
        for(int i = 0 ; i<n; i++){
            array[i] = sc.nextInt();
        }
        Arrays.sort(array);
        int max = array[n-1];
        int min = array[0];

        System.out.println(min + " " + max);
    }
}
