package test;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class test4 {


	public static void main(String[] args) throws IOException {
		
		
		Scanner sc = new Scanner(System.in); // 선언
		
		int num = sc.nextInt(); // 이 숫자까지
		int k = sc.nextInt(); // 이 순서 숫자를 꺼낸다
		Queue que = new LinkedList<>();
		ArrayList list = new ArrayList<>();
		
		for(int i = 1; i <= num; i++) {
			que.offer(i);
		}
		
		while(!que.isEmpty()) {
			for(int i = 0; i < k ; i++) {
				que.poll();
				if(i == k-1) {
					list.add(que.poll());
				}
			}
			
		}
		
		System.out.println(list.toString());
	}
	
	
	
	
}
