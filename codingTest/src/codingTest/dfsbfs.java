package test;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class dfsbfs {
	static int n,m;
	static int arr[][];
	static boolean[] visited;
	static int start;
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in))
				
		String[] temp = br.readLine().split(" ");
		n = Integer.parseInt(temp[0]); //정점의 개수
		m = Integer.parseInt(temp[1]); //간선의 개수
		start = Integer.parseInt(temp[2]); //탐색을 시작할 정점의 번호
		
		arr = new int[n+1][n+1]; //빈 그래프 생성
		
		for(int i=0; i<m; i++) {
			String[] temp2 = br.readLine().split(" ");
			int a = Integer.parseInt(temp2[0]);
			int b = Integer.parseInt(temp2[1]);
			
			arr[a][b] = 1; 
			arr[b][a] = 1; //양방향임. 그래프완성
			
		}
		
		visited = new boolean[n+1];
		dfs(start);
	}
	
	public static void dfs(int k) throws IOException {
		 //방문했으니 트루 
		visited[k] = true;
		bw.write(k + " ");
		
		
		//노드 수 대로.
		for(int i=1; i<=n; i++) {
			//k는 해당 노드, i는 해당 노드와 연결되어있는지 알아볼 노드
			if(arr[k][i] == 1 && !visited[i]) {
				dfs(i);
			}
		}
	}
	
	
}
