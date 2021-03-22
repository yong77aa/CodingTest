function solution(begin, target, words){
    let answer = 51
    let visit = new Boolean[words.length]
    
    const bfs = (begin, target, words, count) => {
        if(begin === target) {
            if(answer > count) answer = count;
            return;
        }
        for(let i = 0 ; i<words.length; i++) {
            let notsame = 0
            if(visit[i]) continue;
    
            for(let j=0; j<begin.length; j++){
                if(begin[j] !== words[i][j]) {
                    notsame++
                }
            }
            if(notsame === 1){
                visit[i] = true;
                bfs(words[i], target, words, count + 1)
                visit[i] = false;
                }
            }
        }
    
    if(!words.includes(target)) return
    bfs(begin, target, words, 0);
    return answer === 51 ? 0 : answer;
        
}