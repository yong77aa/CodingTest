package test.warmingup;

import java.util.*;

public class warmingup09 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int count = 0;

        for(int i = 0; i<n; i++){
            int number = sc.nextInt();
            Boolean result = checkNum(number);
            if(result) {
                count++;
            }
        }
        System.out.println(count);
        
    }

    static Boolean checkNum(int num){
        if(num == 1){
            return false;
        }
        ArrayList<Integer> numArray = new ArrayList<>();
        for(int i = 1; i <=9; i++){
            if(num % i == 0){
                numArray.add(num);
            }
        }
        if(numArray.size() > 2){
            return false;
        }else{
            return true;
        }
    }
}

