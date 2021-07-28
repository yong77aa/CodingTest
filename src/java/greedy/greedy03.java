package greedy;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class greedy03 {
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String s = bf.readLine();
        String[] str = s.split("\\-"); //-를 기준으로 나눔

        int answer = 0;
        for(int i=0; i<str.length; i++){
            String[] plusStr = str[i].split("\\+");
            int calc = 0;
            for(String item : plusStr){
                calc += Integer.parseInt(item);
            }
            if(i == 0){
                answer += calc;

            }else{
                answer -= calc;
            }
        }

    }
}
