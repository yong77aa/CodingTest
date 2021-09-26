package test.warmingup;

import java.util.*;
import java.io.*;

public class warmingup14 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        int x = sc.nextInt();
        int y = sc.nextInt();
        int[] blockNumList = new int[x];

        for (int i = 0; i < x; i++) {
            int num = sc.nextInt();
            blockNumList[i] = num;
        }

        // 첫번째랑 마지막에는 물이 고일 수 없음..
        for (int i = 1; i < x - 1; i++) {
            int leftMax = 0;
            int rightMax = 0;
            int current = blockNumList[i];
            for (int j = i - 1; j >= 0; j--) {
                // 왼쪽에서 가장 높은 기둥의 높이를 구함
                if (blockNumList[j] > current) {
                    leftMax = Math.max(leftMax, blockNumList[j]);
                }
            }
            // 오른쪽에서 가장 높은 기둥의 높이를 구함
            for (int j = i + 1; j < x; j++) {
                if (blockNumList[j] > current) {
                    rightMax = Math.max(rightMax, blockNumList[j]);
                }
            }

            // 현재 벽보다 높은 벽이 양쪽에 있는 경우
            if (Math.min(leftMax, rightMax) > current) {
                sum += Math.min(leftMax, rightMax) - blockNumList[i];
            }
        }

        System.out.println(sum);

    }

}
