function solution(numbers, target) {
    var answer = 0;

    var dfs = function(numbers, target, index) {
            if (index == numbers.length) {
                //마지막이면
                var sum = numbers.reduce((a,b) => (a+b))

                if(sum == target) {
                    //target이랑 같으면
                    answer++
                }
                return
            }else{
                numbers[index] *= 1
                dfs(numbers, target, index+1)
    
                numbers[index] *= -1
                dfs(numbers, target, index+1)     
            }
    }
    dfs(numbers,target,0)
    
    return answer;
}