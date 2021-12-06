function solution(board, moves) {
    var answer = 0;
    var solutionList = [];
    for(let i = 0; i < board.length; i++) {
        let newList = [];
        for(let j = 0; j < board.length; j++) {
            if(board[j][i] != 0){
                 newList.push(board[j][i]) //0이 아닐때만 넣기
            }
        }
        solutionList[i] = newList;
    }
 
    console.log(solutionList);
    
    let tempList = [];
    //moves에 해당하는 수 꺼내기
    for(let i = 0 ; i < moves.length; i++) {
        let a = solutionList[moves[i]-1].shift()
      console.log('a == ' + a)
        if(a){
            if(tempList.length>0 && tempList[tempList.length - 1] == a){
                tempList.pop();
                answer = answer++;
            }else{
                tempList.push(a)
            }
        }
    }
    
    return answer;
}