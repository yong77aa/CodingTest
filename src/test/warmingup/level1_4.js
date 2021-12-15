function solution(array, commands) {
    let numList = [];
    for(let i = 0; i < commands.length ; i++) {
       let start = commands[i][0]
       let end = commands[i][1]
       let num = commands[i][2]
       let newArray = array.slice(start-1, end)
       newArray.sort(function(a,b) {
           return a-b //compare function 안쓰면 오류
       })
       let tempNum = newArray[num-1];
        if(tempNum){
            numList.push(tempNum)
        }
    }
    return numList
}