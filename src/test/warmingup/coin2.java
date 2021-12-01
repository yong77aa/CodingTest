package test.warmingup;

import java.util.*;
import java.io.*;


public class coin2 {
    

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] coinList = new int[n];
        for(int i = 0; i<n; i++) {
            coinList[i] = sc.nextInt();
        }


        //사용한 동전 갯수
        int[] dp = new int[k+1];
        dp[0] = 1;
        int min = 0;

        for(int i = 0; i<coinList.length; i++){
            for(int j = coinList[i]; j <= k; j++){
                min = Math.min(dp[j], dp[j - coinList[i]]);
            }
        }
        System.out.println(min);

    }
}
