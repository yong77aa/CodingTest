function solution(numbers) {
    var answer = '';
    //greedy 인거 같음.. -> 아니고 정렬이었음..
    //sort메서드 잘 알아보고 쓰기..


    let newNumbers = numbers.map((v) => {
        return v+""
    }).sort().reverse().sort((a,b) => {
        let tempA = a + b
        let tempB = b + a
        return parseInt(tempB) - parseInt(tempA)
    })
  
    
    
    return newNumbers.join("")[0] == "0" ? "0" : newNumbers.join("");
    
}