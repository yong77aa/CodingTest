package codingTest;

public class wordChange {
	
	public static void main(String[] args) {
		Solution s = new Solution();
		int result = s.solution("hit", "cog", new String[] {"hot", "dot", "dog", "lot", "log", "cog"});
		System.out.println("결과 : " + result);
	}
	
	public static class Solution {
		boolean[] visited;
		int answer;
		
		public int solution(String begin, String target, String[] words) {
			answer = 51; // 50개까지의 단어가 있으므로
			visited = new boolean[words.length];
			
			for(int i=0; i < words.length; i++) {
				if(!words[i].contains(target)) { // words에 target이 존재하지 않는 경우
					answer = 0; // 0 리턴
				}
			}
			
			dfs(begin, target, 0, words);
			
			return answer;
		}
		public void dfs(String begin, String target, int count, String[] words) {
			
			if(begin.equals(target)) { // 현재 단어와 타겟 단어가 같은 경우
				if(51 > count) { // count가 총 단어의 개수보다 적으면
					answer = count;
					return;
				}
				else {
					answer = 51; // 총 단어의 개수 + 1 만큼 반환
				}
			}
			for(int i=0; i < words.length; i++) { // 단어의 개수만큼 반복
				if(!visited[i] && check(begin, words[i])) { // 방문하지 않았고, 한글자 차이가 나는 단어를 찾음
					visited[i] = true; // 해당 단어는 방문한 것으로 변경
					dfs(words[i], target, count+1, words); // 탐색 실행
					visited[i] = false;
				}
			}
		}
		
		public boolean check(String str, String compare) { // 현재 단어와 비교할 단어가 한글자 차이인지 확인
			int count = 0; // 글자 차이
	        boolean result = false;
	        
	        for(int i=0;i<str.length();i++){
	            if(str.charAt(i)!=compare.charAt(i)) // 두 단어의 해당 인덱스 단어가 다른 경우
	                count++; // 카운트 증가
	        }
	        if(count == 1) { // 한글자 차이면
	            result= true;
	        }
	        else { // 한글자 차이가 아니면
	           result= false;
	        }
	        return result;
		}
	}
}
