package test.warmingup;

import java.util.*;
import java.io.*;
public class addNum {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt();
        int n = 0;
        for(int i = 1; s >= 0; i++){
            s = s-i;
            if(s > 0){
                n = i;
            }
        }
        System.out.println(n);
    }
}