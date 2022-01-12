function solution(record) {
    let tempList = [];
    let answer = [];
     let obj = {}
    record.forEach((item) =>{
       let list = item.split(" ")
        tempList.push(list)
        if(list[2]){ //leave일때는 없어서.. 없는걸 처리해주어야함
            obj[list[1]] = list[2]
        }
    })

    
    tempList.forEach((item) => {
        if(item[0] === "Enter"){
            answer.push(`${obj[item[1]]}님이 들어왔습니다.`)
        }else if(item[0] === "Leave"){
            answer.push(`${obj[item[1]]}님이 나갔습니다.`)
        }
    })
    
    
    return answer
}