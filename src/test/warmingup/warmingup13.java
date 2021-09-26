package test.warmingup;

import java.io.*;
import java.util.*;

public class warmingup13 {
        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));    
            BufferedWriter bw = new BufferedWriter(new PrintWriter(System.out));
            String line = br.readLine();
            
            
            bw.write(f(line) +"\n");
            bw.flush();
        }

        private static int f(String line){
        
            Stack<Character> stack = new Stack<>();
            int mul =1; //공통 곱하기 변수
            int sum =0; //더하는 변수
            int n =0; // ( 괄호의 개수를 셈
            int m =0; // [ 괄호의 개수를 셈
            int  len = line.length();
            
            for(int i=0; i<len; ++i){
                char a = line.charAt(i);
                if(a == '('){
                    n++;
                    stack.push(a);
                    mul *=2;
                    if(i+1 < len && line.charAt(i+1) == ')'){ 
                        sum +=mul;
                    }
                }
                
                else if(a == '['){
                    m++;
                    stack.push(a);
                    mul *=3;
                    if(i+1 < len && line.charAt(i+1) == ']'){
                        sum +=mul;
                    }
                }
                
                else if(a == ')'){
                    n--; // ( 괄호 개수 -1
                    stack.pop();
                    mul /=2; //닫으면 나눠줌
                }
                else if(a == ']'){
                    m--; // [ 괄호 개수 -1
                    stack.pop();
                    mul /=3;
                }
            }
            
            if(!stack.empty() || n !=0 || m !=0 ){ // (()] 같은 비대칭 쌍 방지
                return 0;
            }
            
            return sum;
        }
}
