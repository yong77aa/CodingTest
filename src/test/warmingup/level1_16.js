function solution(arr, divisor) {
    var answer = [];
    
    answer = arr.filter((item) => {
        if(item % divisor == 0){
            return item
        }
    })
    answer.sort((a,b) => a-b) //정렬
    
    return answer.length > 0 ? answer : [-1];
}