function solution(numbers, target) {
    var answer = 0;
    
    let dfs = function(numbers, target, index){
        
        if(index == numbers.length){
            let sum = numbers.reduce((acc, value) =>{
                return acc += value
            }, 0)
            if(sum == target){
                answer++
            }
            return;
        }
       
        numbers[index] *= 1
        dfs(numbers, target, index+1)
        numbers[index] *= -1
        dfs(numbers, target, index+1)
    }
    
    dfs(numbers, target, 0)
    
    return answer;
}