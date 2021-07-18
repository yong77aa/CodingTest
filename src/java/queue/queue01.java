package queue;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;

public class queue01 {
   static int people;
   static int num;
   static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

   public static void main(String[] args) throws IOException {
      // TODO Auto-generated method stub
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

      people = Integer.parseInt(br.readLine());
      num = Integer.parseInt(br.readLine());

      Queue<Integer> que = new LinkedList<>();

      for (int i = 1; i <= people; i++) {
         que.offer(i);
      }

      while (!que.isEmpty()) {
         for (int i = 1; i <= num - 1; i++) {
            int val = que.poll();
            que.offer(val);
         }
         System.out.println(que.poll());

      }

   }
}