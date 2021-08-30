package test.warmingup;

import java.util.*;

public class warmingup07 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int min = getMin(a, b);
        int max = getMax(a, b, min);

        System.out.println(min + " " + max);

    }

    static Integer getMax(int a, int b, int min){
        return (a / min) * (b / min) * min;

    }
    static Integer getMin(int a, int b){
        
        ArrayList<Integer> aList = new ArrayList<>();
        ArrayList<Integer> bList = new ArrayList<>();

        for(int i = 1; i<= a; i++){
            if(a % i == 0){
                aList.add(i);
            }
        }

        for(int i = 1; i<=b; i++){
            if(b % i == 0){
                bList.add(i);
            }
        }
        
        ArrayList<Integer> commonList = new ArrayList<>();
        for(int i = 0; i<aList.size(); i++){
            for(int j = 0 ; j<bList.size(); j++) {
                if(aList.get(i) == bList.get(j)){
                    commonList.add(aList.get(i));
                    
                }
            }
        }
        Collections.sort(commonList, Collections.reverseOrder());
        return commonList.get(0);
    }
}
