function solution(progresses, speeds) {
    var answer = [];
    //1. 남은 작업량 구하기
    //2. 며칠 걸리는지 계산해서 배열에 넣기
    let leftDays = progresses.reduce(function(acc, item, index ,arr){
         // return acc.concat(100 - item)
        return acc.concat(Math.ceil((100 - item)/speeds[index]))
    }, []);
    
    
    let count = 1;
    let max = 0;
    while(leftDays.length > 0){
       max = Math.max(leftDays.shift(), max) //처음에 5들어감
         console.log(`max == ${max}, leftDays == ${leftDays[0]}`)
        if(max >= leftDays[0]){
            count++;
        }else{
            answer.push(count)
            count = 1;
        }
    }
    
    console.log(answer)
    return answer;
}