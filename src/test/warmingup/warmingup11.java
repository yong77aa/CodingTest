package test.warmingup;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class warmingup11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //n부터
        int n = sc.nextInt();
        //m까지
        int m = sc.nextInt();

        ArrayList<Integer> numList = new ArrayList<>();

        //10미만 1제외 자연수
        int[] naturalList = {2,3,4,5,6,7,8,9};
        int count = 0;
        for(int i = n; i <= m; i++) {

            //소수인지 check
            Boolean check = false;
            for(int j = 0; j < naturalList.length; j++) {
                if(i%naturalList[j] == 0){
                    check = true;
                }
            }
            if(!check) {
                numList.add(i);
                count += i;
            }
        }

        Collections.sort(numList);
        
      
        if(numList.size() > 0){
              //최소값
            int min = numList.get(0);
            System.out.println(count);
            System.out.println(min);
    
        }else{
            System.out.println("-1");
        }
      

    }
{}
   

}
