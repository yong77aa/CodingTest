function solution(s) {
    let answer = [];
    let newArr = [];
    const str = s.split("").forEach((item) => {  
        if(item == "{"){
            item = "["
        }else if(item == "}"){
            item = "]"
        }
        newArr.push(item)
    })
   
    newArr = newArr.join("")
    
    console.log(Array.from(newArr))
    // newArr.forEach((item) => {
    //     if(item.length === 1){
    //         answer.shift(item)
    //     }
    // })
    
    console.log(answer)
    return answer;
}