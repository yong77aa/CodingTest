package test.stack;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class stack03 {
    
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String bar = bf.readLine(); //입력받은 괄호
        Stack<Character> stack = new Stack<>();
    
        int answer = 0;

        for(int i = 0; i<bar.length(); i++) {
            //괄호가 () 일경우 stack 사이즈만큼 증가.
            //괄호가 ')' (닫힘) 일 경우 +1, 그리고  pop (스택에 쌓이면 안됨)
            //괄호가 '(' (열림) 일 경우 stack에 넣기

            if(bar.charAt(i) == ')') {

                if(bar.charAt(i-1) == '('){
                    stack.pop(); //열린게 아니고 레이저니까 pop해주고
                    answer += stack.size(); // stack 사이즈만큼 더해주기
                }else{
                    stack.pop(); //닫힌거는 pop 해주고 무조건 1 더하기
                    answer++;
                }
            }else if(bar.charAt(i) == '('){
                stack.add('(');
            }
        }

        System.out.println(answer);

    }
}
