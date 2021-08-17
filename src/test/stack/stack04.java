package test.stack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class stack04 {
    public static void main(String[] args) throws IOException {
    
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(bf.readLine()); // 몇개 받는지
        Stack<Integer> stack = new Stack<>();
        
        for(int i = 0; i<k; i++){
         int n = Integer.parseInt(bf.readLine());
            if(n == 0) {
                //0
                stack.pop();
            }else{
                stack.add(n);
            }
        }

        int count = 0;
        while(!stack.isEmpty()){
            count += stack.pop();
        }

        System.out.println(count);
    }
}
