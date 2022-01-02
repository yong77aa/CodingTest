function solution(s) {
    var answer = '';
    
    if((s.length % 2) == 1){
        //2로 나누면 1이 생김
        answer = s[((s.length + 1)/2) - 1]
    }else{
        //나누어 떨어짐
        answer = s[s.length/2 - 1] + s[s.length / 2]
        console.log(s[s.length - 1] )
    }
    return answer;
}