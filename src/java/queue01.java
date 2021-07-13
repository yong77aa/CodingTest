public class queue {
   static int people; 
   static int num;
   static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
   
   public static void main(String[] args) throws IOException {
      // TODO Auto-generated method stub
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      
      
      people = Integer.parseInt(br.readLine());
      num = Integer.parseInt(br.readLine());
      
      Queue<Integer> que = new LinkedList<>();

      for(int i = 1 ; i <= people; i++) {
         que.offer(i);
      }
      
      while(!que.isEmpty()) {
         for(int i = 1; i<= num-1; i++) {
            int val = que.poll();
            que.offer(val);
         }
      System.out.println(que.poll());
      
      }
      
   }
}