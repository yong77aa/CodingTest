package test.greedy;

import java.util.Scanner;

public class greedy05 {
    
    public static void main(String[] args) throws Exception{
        
        Scanner scanner = new Scanner(System.in);
        int k = scanner.nextInt(); //작은 수 
        int n = scanner.nextInt(); //큰수

        int difference = n-k; // 초기화
        int count = 0;

        while(difference >= 10){
            difference = difference - 10;
            count++;
           
        }
        
        while(difference >= 5) {
            difference = difference - 5;
            count++;
           
        }


        count += difference;

        System.out.println(count);
    }
}
