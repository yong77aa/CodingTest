package greedy;

import java.io.*;
import java.util.*;


public class greedy04 {
    
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int[] pastas = new int[3];
        int[] juices = new int[2];
        for(int i = 0; i < 5; i++) {
            if(i <=2){
                pastas[i] = Integer.parseInt(bf.readLine());
            }else{
                juices[i-3] = Integer.parseInt(bf.readLine());
            }
        }

        //최소값 꺼내기
        Arrays.sort(pastas);
        Arrays.sort(juices);

        Double total = (pastas[0] + juices[0]) * 1.1;
        
        System.out.println(String.format("%.1f" , total));
    }
}
