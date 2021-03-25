package test;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class test4 {
	static int arr[][];
	static int total; //컴퓨터수
	static int line; //간선
	static boolean[] visited;
	static int count;
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		total = Integer.parseInt(br.readLine());
		line = Integer.parseInt(br.readLine());
		
		visited = new boolean[total+1];
		arr = new int[total+1][total+1];
		
		for(int i=0; i<line; i++) {
			String[] temp = br.readLine().split(" ");
			int a = Integer.parseInt(temp[0]);
			int b = Integer.parseInt(temp[1]);
			arr[a][b] = 1; 
			arr[b][a] = 1;
			
			
		}
		
		dfs(1);
		
		var answer = count;
	}
	
	public static void dfs(int k) {
		visited[k] = true;
		
		for(int i=1; i<=total; i++) {
			if(arr[k][i] == 1 && !visited[i]) {
				count++;
				dfs(i);
			}
		}
	}
}
