package greedy;

import java.util.*;


import java.io.*;


public class greedy07 {
    

    public static void main(String[] args) throws Exception{
        
        Scanner sc = new Scanner(System.in);
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int k = Integer.parseInt(bf.readLine()); //토핑 종류
        int doughPrice = sc.nextInt(); //도우가격

        int topingPrice = sc.nextInt(); //토핑가격

        int doughKcal = Integer.parseInt(bf.readLine());//도우칼로리

        int ans = doughKcal / doughPrice; //1달러당 도우 최초 칼로리
        Integer[] topKcalList = new Integer[k];

        for(int i = 0; i<k; i++){
            topKcalList[i] = Integer.parseInt(bf.readLine());
        }

        //가격 입력받은거 내림차순으로 정렬.
        Arrays.sort(topKcalList, Collections.reverseOrder());
        
        int tempKcal = doughKcal;
        int tempPrice = doughPrice;

        //토핑 가격당 칼로리가 가장 높아야됨!!!
        for(int i = 0 ; i<topKcalList.length; i++){
            tempKcal += topKcalList[i];
            tempPrice += topingPrice;
            int tempAns = tempKcal/tempPrice;

            if(ans > tempAns){
                // 그 전에 합한게 더 크면 break
                break;
            }else{
                ans = tempAns;
            }

        }
        System.out.println(ans);

    }
}
