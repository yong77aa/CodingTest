package test.warmingup;
import java.util.*;
import java.io.*;


public class adventure {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] peopleList = new int[n];
        for(int i = 0; i<n; i++) {
            peopleList[i] = sc.nextInt();
        }

        Arrays.sort(peopleList);

        int group = 0; //group 수
        int count = 0; //탐험가 수
        for(int i = 0; i<peopleList.length; i++) {
            count++;
            if(count >= peopleList[i]){
                group++;
                count=0;
            }
        }

        System.out.println(group);

    }
}
