package test.warmingup;

import java.util.Scanner;

public class warmingup05 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] addList = new int[n+1];
        addList[0] = 0;
        addList[1] = 1;
        for(int i = 1; i< n; i++){
            addList[i+1] = addList[i] + addList[i-1];
        }
        System.out.println(addList[n]);
    }
}
