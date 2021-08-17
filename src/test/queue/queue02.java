package test.queue;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class queue02 {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int testCase = sc.nextInt();

		int totalCount;// 문서 갯수

		int targetIndex;// 특정 문서 index

		int count = 0;

		for (int i = 0; i < testCase; i++) {
			totalCount = sc.nextInt();
			targetIndex = sc.nextInt();
			Queue<int[]> que = new LinkedList<>();

			for (int j = 0; j < totalCount; j++) {
				// 중요도 입력
				que.add(new int[] { j, sc.nextInt() });

				while (!que.isEmpty()) {
					int[] now = que.poll();
					boolean able = true;

					for (int[] q : que) {
						if (q[1] > now[1]) {
							able = false;
						}
						if (able) {
							count++;
							if (now[0] == targetIndex)
								break;
						} else
							que.add(now);
					}
					System.out.println(count);
				}
			}
		}
	}
}