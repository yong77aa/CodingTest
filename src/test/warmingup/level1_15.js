function solution(arr)
{
    var answer = [];

    arr.forEach((item) => {
        if(answer.length === 0){
            answer.push(item)
        }else{
            let a = answer.pop()
            let b = item
            if(a == b){
                answer.push(b)
            }else{
                answer.push(a)
                answer.push(b)
            }
        }
        
    })
    return answer;
}