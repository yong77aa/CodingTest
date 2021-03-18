function solution (n, computers) {
    var answer = 0;
    var isVisited = new Boolean[n]

    var DFS = function(computers, i) {
        
        if(isVisited[i]) {return} //이미 방문했으면 return
        
        //방문했음
        isVisited[i] = true

        for(let j = 0; j < computers.length; j++) {
            if(computers[i][j] == 1) {
                DFS(computers, j)
            }
        }
    }


    for(let i = 0; i < n; i++){
        if(!isVisited[i]) {
            //방문 안했으면 탐색 !!
            answer++
            DFS(computers, i)
        }
    }
}