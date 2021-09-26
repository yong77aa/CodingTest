package test.warmingup;

import java.util.Scanner;

public class warmingup12 {

    static int max = Integer.MIN_VALUE;
    static int min = Integer.MAX_VALUE;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(); // 숫자의 갯수
        int[] numList = new int[n];
        int[] calcList = new int[4]; // 0 : 덧셈, 1: 뺄셈, 2: 곱섹, 3: 나눗셈

        // 계산 할 수 list 만들기
        for (int i = 0; i < n; i++) {
            numList[i] = sc.nextInt();
        }

        // 계산 연사자 list 만들기
        for (int i = 0; i < 4; i++) {
            calcList[i] = sc.nextInt();
        }

        dfs(numList, calcList, numList[0], 1);

        System.out.println(max);
        System.out.println(min);
    }

    public static void dfs(int[] numList, int[] calcList, int sum, int index) {
        if (index == numList.length) {
            // index 가 마지막 데이터 값을 넘어갈때
            max = Math.max(sum, max);
            min = Math.min(sum, min);
            return;
        }

        // 연산자 만큼 dfs 실행
        for (int i = 0; i < calcList.length; i++) {
            if (calcList[i] != 0) {
                // 연산자가 존재하면 한번 돌았으면 -값.
                calcList[i]--;

                switch (i) {
                    case 0: // 덧셈
                        dfs(numList, calcList, sum + numList[index], index + 1);
                        break;
                    case 1: // 뺄셈
                        dfs(numList, calcList, sum - numList[index], index + 1);
                        break;
                    case 2: // 곱셈
                        dfs(numList, calcList, sum * numList[index], index + 1);
                        break;
                    case 3: // 나눗셈
                        dfs(numList, calcList, sum / numList[index], index + 1);
                        break;

                }

                // dfs 종료 후 다시 돌리기.
                calcList[i]++;
            }
        }
    }
}