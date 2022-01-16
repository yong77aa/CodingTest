function solution(n) {
    let answer = ""
    let numObj = [4, 1, 2]
    
    while(n){ //n이 0 이상일때 까지
        answer = numObj[n % 3] + answer
        n = Math.floor((n-1) /3)
    }

   
  
    return answer.toString();
}