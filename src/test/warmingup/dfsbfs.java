package test.warmingup;

import java.util.*;
import java.io.*;

public class dfsbfs {

    static int[] visited;
    static int[] bfsVisited;
    static int n;
    static int v;
    static int[][] graph;
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt(); //정점의 갯수
        v = sc.nextInt(); //간선의 갯수
        visited = new int[n+1]; //노드를 다 방문하면!
        bfsVisited = new int[n+1];
        int start = sc.nextInt(); //시작할 정점
        graph = new int[n+1][n+1];//인접행렬
       

        //간선의 개수는 연결되어 있다는 거니까.. for문으로 1넣어줌
        for(int i =1 ; i<=v; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        dfs(start);
    }

    public static void dfs(int start){
        visited[start] = 1;
        System.out.println(start + " ");
        if(start == graph.length){
            return;
        }
        
        for(int j = 1; j<graph.length; j++){
            if(graph[start][j] == 1 && visited[j] == 0){
                dfs(j);
            }
           
        }
    }

    public static void bfs(int start){
        bfsVisited[start] = 1;
        Queue<Integer> que = new LinkedList();
        que.add(start);
        bfsVisited[start] = 1;
        
        for(int j = 1; j<n; j++){
            
        }
    }

   
}
