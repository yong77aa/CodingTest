package codingTest;

public class network {

	public static void main(String[] args) {
		Solution s = new Solution();
		int result = s.solution(3, new int[][] { {1,1,0}, {1,1,0}, {0,0,1}});
		System.out.println("결과 : " + result);
	
	}
	
	public static class Solution {
		public int solution(int n, int[][] computers) {
			int answer = 0;
			boolean visited[] = new boolean[n];
			
			for(int i=0; i < n; i++) {
				if(!visited[i]) { // 방문하지 않은 노드만
					dfs(i, computers, visited); // 깊이탐색 실행
					answer++;	
				}
			}
			return answer;
		}
		
		public void dfs(int n, int[][] computers, boolean[] visited) {
			visited[n] = true; // 해당 노드를 방문한 것으로 변경
			
			for(int i=0; i < computers.length; i++) { // 해당 배열의 갯수만큼 반복
				// 방문하지 않았고, 해당 노드가 연결되어 있으면
				if(!visited[i] && computers[n][i] == 1) {
					dfs(i, computers, visited); // 그 노드로 이동해서 dfs 실행 (네트워크가 연결되어 있는지 확인하기 위해)
				}
			}
		}
	}
}