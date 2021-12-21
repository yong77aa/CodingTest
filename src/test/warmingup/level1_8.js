//예산
function solution(d, budget) {
    var answer = 0;
    d.sort(function(a,b){
      return a-b  
    }) //오름차순정렬
    
    d.forEach((item) => {
        if(budget-item >= 0){
            budget = budget-item
            answer++;
        }
    })
    
    
    return answer;
}