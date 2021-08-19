package test.greedy;

import java.util.Scanner;

public class greedy02 {
    
    public static void main(String[] args) throws Exception{
        
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int totalAmount = sc.nextInt();
        int count = 0; //동전갯수
        int[] array = new int[k];

        for(int i = 0; i<k; i++){
            array[i] = sc.nextInt();
        }
        
        for(int i = k-1; i>0; i--){
           if(array[i] <= totalAmount){
               count += totalAmount / array[i];//입력받은 값을 동전 값으로 나누면 동전의 개수
               totalAmount = totalAmount % array[i]; //그 나머지는 다시 만들어야 할 값으로,,
           }
        }

        System.out.println(count);

    }
}
