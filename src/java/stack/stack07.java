package stack;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Stack;


//틀렸으니까 다시풀기
public class stack07 {

    public static void main(String[] args) throws Exception{
        
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String s = bf.readLine();
        ArrayList<Character> list = new ArrayList<>();
        Stack<Character> stack = new Stack<>();

        for(int i = 0; i<s.length(); i++) {
            if(s.charAt(i) != '(' && s.charAt(i) != ')'){
                if(s.charAt(i) == '*' || s.charAt(i) == '-' || s.charAt(i) == '+' || s.charAt(i) == '/'){
                    stack.add(s.charAt(i));
                }else{
                    list.add(s.charAt(i));
                }
            }         
        }
        
        //isempty 써야됨 그게 정확함!!!!!!!!
        while(!stack.isEmpty()){
            list.add(stack.pop());
        }
        
        String string = "";
        for (int i = 0 ; i < list.size(); i++) {
            string += list.get(i);
        }
        
        System.out.println(string);
        
    }
    
}
