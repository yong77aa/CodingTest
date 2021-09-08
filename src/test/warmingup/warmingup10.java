package test.warmingup;

import java.util.ArrayList;
import java.util.Scanner;

public class warmingup10 {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        
        ArrayList array = new ArrayList<>();
        
        int num = 1;
        while(array.size() < b){
            for(int i = 1; i <= num; i++){
                array.add(num);
                if(array.size() >= b) {
                    break;
                }
            }
            num++;
        }

        int count = 0;
        for(int i = a-1; i<array.size(); i++) {
            count += Integer.parseInt(array.get(i).toString());
        }
        System.out.println(count);
    }

    
}
