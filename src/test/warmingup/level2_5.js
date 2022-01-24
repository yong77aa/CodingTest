function solution(rows, columns, queries) {
    var answer = [];
    let graph = [];
    let temp = [];
    for(let i = 0; i < rows * columns; i++){
        temp.push(i+1)
        if(temp.length == columns){
            graph.push(temp)
            temp = []; //초기화
        }
    }
    
   
    queries.forEach((item) =>{
        let [x1,y1,x2,y2] = item.map((value) => { return value - 1})
        
        let newGraph = [] //빈배열
        
        //1. 일단 1차원으로 해당 숫자들을 펴보자
        for(let i = y1; i < y2; i++){  
            newGraph.push(graph[x1][i])
        }
        for(let i = x1; i < x2; i++){
            newGraph.push(graph[i][y2])
        }
        
        for(let i = y2;  i > y1; i--){
            newGraph.push(graph[x2][i])
        }
        for(let i = x2; i > x1; i--){
            newGraph.push(graph[i][y1])
        }
        
        //2. 한칸씩 이동시키려면 맨뒤에 숫자를 맨 앞으로 보내면 된다.
        newGraph.unshift(newGraph.pop())
        
        //3. 그중에서 가장 작은 값을 배열에 넣어보자
        let min = Math.min(...newGraph)
        answer.push(min)
        //3. 그 배열들을 다시 graph에 넣어주자
        for(let i = y1; i < y2; i++){
            graph[x1][i] = newGraph.shift()
        }
        
        for(let i = x1; i < x2; i++){
            graph[i][y2] = newGraph.shift()
        }
        
        for(let i = y2; i > y1; i--){
            graph[x2][i] = newGraph.shift()
        }
        
        for(let i = x2; i > x1; i--){
            graph[i][y1] = newGraph.shift()
        }
        
        
    }) 
   
    
    return answer
}