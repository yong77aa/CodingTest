package test.warmingup;

import java.util.*;
import java.io.*;

public class candy {
    static int max = 1;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        char[][] candyList = new char[n][n];

        //리스트완성
        for(int i = 0; i < n ; i++) {
            String line = sc.next();
            for(int j = 0; j < n; j++) {
                candyList[i][j] = line.charAt(j);
            }
        }

        //바꾸고 캔디 먹기
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n-1; j++) {
                char temp = candyList[i][j];
                candyList[i][j] = candyList[i][j+1];
                candyList[i][j+1] = temp;
                eatCandy(candyList, n);
                candyList[i][j+1] = candyList[i][j];
                candyList[i][j] = temp;
            }
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n-1; j++) {
                char temp = candyList[i][j];
                candyList[j][i] = candyList[j+1][i];
                candyList[j+1][i] = temp;
                eatCandy(candyList, n);
                candyList[j+1][i] = candyList[j][i];
                candyList[j][i] = temp; 
            }
        }

        System.out.println(max);
    
    }


    public static void eatCandy(char[][] candyList, int n){
        
        //가로
        for(int i = 0 ; i < n; i++) {
            int temp = 1;
            for(int j = 0; j < n-1 ; j++) {
                if(candyList[i][j] == candyList[i][j+1]){
                    temp++;
                }else{
                    temp = 1;
                }
                max = Math.max(max, temp);
            }
        }

        //세로
        for(int i = 0; i < n; i++) {
            int temp = 1;
            for(int j = 0; j < n-1; j ++) {
                if(candyList[j][i] == candyList[j+1][i]){
                    temp++;
                }else{
                    temp = 1;
                }
            }
            max = Math.max(max, temp);
        }
    }
}
