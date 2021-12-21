//두개 뽑아서 더하기
function solution(numbers) {
    var answer = [];
    
    for(let i = 0; i < numbers.length; i++){
        let a = numbers[i];
        for(let j = i+1; j < numbers.length; j++) {
            let b = numbers[j];
            answer.push(a+b)
        }
    }
    
    let newAnswer = [... new Set(answer)] //중복제거 외우기 ****
  
    newAnswer.sort(function(a,b){
        return a-b
    })
    
    return newAnswer;
}