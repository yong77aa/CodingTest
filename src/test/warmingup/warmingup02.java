package test.warmingup;

import java.util.*;
import java.io.*;

public class warmingup02 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int testCaseNum = sc.nextInt();
        for(int i = 0; i<testCaseNum; i ++){
            int num = sc.nextInt();
            Queue<Integer> que = new LinkedList<>();
            String s = "";
            while(num >=1){
                int n = num % 2;
                num = num / 2;
                que.add(n);
            }
            int count = 0;
            while(!que.isEmpty()){
                if(que.poll() == 1){
                    s += count + " ";
                }
                count++;
            }
            System.out.println(s);
        }
    }
}
