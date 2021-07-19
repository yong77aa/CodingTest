package stack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class stack02 {

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine()); //몇개의 정수가 나올 것인가
        Stack<Integer> stack = new Stack<>();

        while(k > 0) {
            k--;
            int num = Integer.parseInt(br.readLine());
            if(num == 0) {
                stack.pop();
            }else{
            
                stack.push(num);
            }
        }
     
        int total = 0;
        
        //0일 경우
        if(stack.isEmpty()) {
            System.out.println(0);
            return;
        }
       
        while(!stack.isEmpty()){
            total += stack.pop();
        }
        System.out.println(total);
       

    }
}