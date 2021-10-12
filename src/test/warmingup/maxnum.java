package test.warmingup;
import java.util.*;
import java.io.*;

public class maxnum {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String s = sc.nextLine();
        int[] numArray = new int[s.length()];

        int count = 1;

        for(int i = 0; i<s.length(); i++) {
            numArray[i] = Integer.parseInt(s.substring(i, i+1));
        }

        for(int i = 1; i < numArray.length; i++) {
            
            if(numArray[i-1] <= 1 || numArray[i] <= 1){
                if(i == 1){ 
                    count = 0;
                    count = numArray[0] + numArray[1];
                }else{
                    count += numArray[i];
                }
            }else{
                if(i == 1){
                    count = 1;
                    count = numArray[0] * numArray[1];
                }else{
                    count *= numArray[i];
                }
            }
        }

        System.out.println(count);

    }
}
