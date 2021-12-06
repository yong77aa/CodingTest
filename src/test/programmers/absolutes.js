function solution(absolutes, signs) {
    var answer = 0;
    for(let i = 0 ; i < absolutes.length; i++) {
        let a = signs[i]
        if(a){
            answer += absolutes[i]
        }else{
            answer -= absolutes[i]
        }
    }
    return answer
}