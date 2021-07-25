package stack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Stack;

public class starck06 {
    
    public static void main(String[] args) throws Exception {
        //Exception throws 꼭 해주기!!! ***** 

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(bf.readLine()); //괄호
        String s = bf.readLine();

        HashMap<Character, Integer> map = new HashMap<>();
        char ch = 'A';
        for(int i = 0; i < k; i++) {
            //map 에 넣기 (짝지어야할때 필수로 생각하기)
            //신기함..알파벳도 이렇게 되는구나
            map.put(ch++, Integer.parseInt(bf.readLine()));
        }

        Stack<Double> stack = new Stack<>();
       
        for(int i = 0 ; i<s.length(); i++) {
            ch = s.charAt(i);
            if('A' <= ch && ch <= 'Z'){
                //알파벳 해당하는 숫자 넣기
                
                stack.push((double)map.get(ch));
            }else{
                    double b = stack.pop(); //나중에 넣은 값이 b 가 되는거~
                    double a = stack.pop(); //먼저 넣은 값은 a가 되는거~~
                    switch (s.charAt(i)) {
                        case '+':
                            double n = a + b;
                            stack.push(n); // 계산 한 값을 다시 push 해주어야함 *** 
                            break;
                        case '-':
                            n = a - b;
                            stack.push(n);
                            break;
                        case '*' :
                            n = a * b;
                            stack.push(n);
                            break;
                        case '/' :
                            n = a / b;
                            stack.push(n);
                            break;
                    }
                  
              
            }
        }
        System.out.println(stack.pop());
    }
}
