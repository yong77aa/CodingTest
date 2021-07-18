package queue;

import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class queue03 {
	public static void main(String[] args) throws IOException {

		Scanner sc = new Scanner(System.in); // 선언

		int n = sc.nextInt(); // 1 ~ n 까지의 정수
		Queue que = new LinkedList<>();

		for (int i = n; i <= n; i--) {
			que.add(i);
		}

		while (!(que.size() > 1)) {
			que.poll();
			que.offer(que.poll());
		}

		System.out.println(que.poll());

	}
}