package codingTest;

public class targetNumber {

	public static void main(String[] args) {
		Solution s = new Solution();
		int result = s.solution(new int[] {1, 1, 1, 1, 1}, 3);
		System.out.println("결과 : " + result);
	}
	
	public static class Solution {
		public int solution(int[] numbers, int target) {
			int answer = 0;
			
			answer = dfs(numbers, target, 0, 0);
			
			return answer;
		}
	}
	
	public static int dfs(int[] numbers, int target, int sum, int i) {
		int result = 0;
		
		// 마지막까지 탐색하는 경우, target과 같다면 1 반환 (방법 수를 하나 늘리는 것임)
		if(i == numbers.length) {
			if(sum == target) {
				return 1;
			}
			else {
				return 0;
			}
		}
		
		// +1을 할때와 -1을 할때는 따로 탐색한다
		result += dfs(numbers, target, sum+numbers[i], i+1);
		result += dfs(numbers, target, sum-numbers[i], i+1);
		
		return result;
	}

}
