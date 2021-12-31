function solution(sizes) {
    var answer = 0;
    var maxList = [];
    var minList = [];
    
    
    for(let i = 0; i < sizes.length; i++){
        maxList.push(Math.max(sizes[i][0], sizes[i][1]))
        minList.push(Math.min(sizes[i][0], sizes[i][1]))
    } //큰수는 큰수끼리, 작은수는 작은수끼리 모아보기
    
    maxList.sort((a,b)=> a-b)
    minList.sort((a,b)=> a-b)
    
    answer = maxList[maxList.length-1] * minList[minList.length-1]
    
    
    
    return answer;
}