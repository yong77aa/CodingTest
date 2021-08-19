package test.warmingup;

import java.util.*;


public class warmingup04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer[] countArray = new Integer[10];

        for(int i = 0; i<10 ; i++){
            int minusNum = sc.nextInt();
            int plusNum = sc.nextInt();
            if(i != 0){
                countArray[i] = countArray[i-1] + (-1*minusNum + plusNum);
            }else{
                countArray[i] = -1*minusNum + plusNum;
            }
           
        }
        
        Arrays.sort(countArray, Collections.reverseOrder());
        System.out.println(countArray[0]);
        
    }
}
