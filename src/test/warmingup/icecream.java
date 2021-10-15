package test.warmingup;

import java.util.*;
import java.io.*;

public class icecream {
    static int n;
    static int m;
    static int[][] graph = new int[1000][1000];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 세로길이 (길이랑 index는 다름 index는 길이 -1)
        n = sc.nextInt();
        // 가로길이
        m = sc.nextInt();

        // 그래프 만들기
        for (int i = 0; i < m; i++) {
            String s = sc.nextLine();
            for (int j = 0; j < s.length(); j++) {
                graph[i][j] = s.charAt(j) - '0';
            }
        }

        int result = 0;
        // 모든 노드에서 dfs를 해야하니까.. for문으로
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.println("처음for 문 " + " i == " + i + " j == " + j);
                if (dfs(i, j)) {
                    result++;
                }
            }
        }

        System.out.println(result);

    }

    public static boolean dfs(int x, int y) {
        System.out.println("dfs 시작 x = " + x + " y = " + y);
        if (x < 0 || x >= n || y < 0 || y >= m) {
            return false;
        }

        if (graph[x][y] == 0) {
            graph[x][y] = 1;
            dfs(x, y + 1);// 상
            dfs(x, y - 1);// 하
            dfs(x - 1, y);// 좌
            dfs(x + 1, y);// 우
            return true;
        } else {
            return false;
        }

    }
}