package java.warmingup;


import java.util.ArrayList;
import java.util.Scanner;


public class warmingup01 {
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int numIndex = sc.nextInt();
        ArrayList numArray = new ArrayList<>();
        for(int i = 1; i<= num; i++){
            if(num % i == 0){
                numArray.add(i);
            }
        }
        
        System.out.println(numArray.get(numIndex-1));
    }
}