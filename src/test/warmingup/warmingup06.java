package test.warmingup;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

import javax.print.event.PrintJobListener;

public class warmingup06 {
    
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
       
        int n = 9;
        ArrayList<Integer> heightList = new ArrayList<>();
        int total = 0;
        
        for(int i = 0; i<n; i++) {
            heightList.add(Integer.parseInt(bf.readLine()));
            total += heightList.get(i);
        }
       
        boolean check = false;

        for(int i = 0; i<heightList.size(); i++){
           if(check) break;
            for(int j = 0; j<heightList.size(); j++) {
                if(i != j) {
                int count = total - heightList.get(i) - heightList.get(j);
                    if(count == 100) {
                        heightList.set(i, 0);
                        heightList.set(j, 0);
                        check = true;
                       break;
                    }
                }
            }
        }
        
        Collections.sort(heightList);

        for(int i = 0; i<heightList.size(); i++) {
            if(heightList.get(i) != 0) {
                System.out.println(heightList.get(i));
            }
        }
    }
}
