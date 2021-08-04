package greedy;

import java.util.Scanner;

public class greedy06 {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int money = sc.nextInt();
        int[] currency = {50000, 10000, 5000, 1000, 500, 100, 50, 10};
        int count = 0;
        for(int i = 0; i<currency.length; i++) {
            while(money - currency[i]>= 0){
                money -= currency[i];
                count++;
            }
        }

        System.out.println(count);
    }
}
