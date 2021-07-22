package stack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;


public class stack05 {
    
    public static void main(String[] args) throws IOException {
    
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String line = bf.readLine(); //괄호
        Stack<Character> stack = new Stack<>();
        int num = 0;

        for(int i = 0 ; i < line.length(); i++) {
            char c = line.charAt(i);
           if(c == '('){
                stack.push(c);
           }else if(c == ')'){
               stack.pop();
               if(stack.contains('(')){
                   num *= 2;
               }
           }else if(c == '['){
               if(line.charAt(i-1) == ')'){
                   num + 
               }
               stack.push('[');
           }else if(c == ']'){
               stack.pop();
               if(stack.contains('[')){
                   num *=3;
               }
           }
        }
        System.out.println(num);
    }
}
