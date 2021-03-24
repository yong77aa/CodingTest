package codingTest;
import java.util.*;
import java.io.*;

public class virus {
	static int a, b, result;
	static boolean[][] conn;	// 컴퓨터 간의 연결을 나타내기 위한 배열
	static boolean[] visited;	// 방문을 체크하기 위한 배열

	public static void main(String[] agrs) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		a = Integer.parseInt(br.readLine()); // 컴퓨터의 수
		b = Integer.parseInt(br.readLine()); // 연결되어있는 컴퓨터 쌍의 수

		conn = new boolean[a + 1][a + 1]; // 경로를 저장하기 위한 배열
		visited = new boolean[a + 1]; // 방문 여부 확인

		for (int i = 1; i <= b; ++i) {
			String str = br.readLine();
			StringTokenizer st = new StringTokenizer(str);
			int first = Integer.parseInt(st.nextToken());
			int second = Integer.parseInt(st.nextToken());
			// 첫번째와 두번째 모두 방문처리
			conn[first][second] = true;
			conn[second][first] = true;
		}

		dfs(1); // 첫번째부터 실행
		System.out.println(result); // 결과 출력

	}

	static void dfs(int start) {
		visited[start] = true;	// 방문 처리 
		for (int i = 1; i <= a; ++i) {	// 모든 컴퓨터를 돌면서 연결된 컴퓨터이면서 방문하지 않은 컴퓨터를 확인
			if (conn[start][i] == true && visited[i] == false) {
					result++;	// 조건에 해당되면 +1 
					dfs(i);		// 조건에 해당되는 컴퓨터를 기준으로 반복
			}
		}
	}
}
