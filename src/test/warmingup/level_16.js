function solution(s) {
    let answer = [];
    let newArr = [];
    
    const str = s.split("{").forEach((item, index, arr) => { 
        let tempArr = []
        item = item.replace(/}/gi,"")
        item.split(",").forEach((letter) => {
            if(letter != "}" && letter != "," && letter != ""){
                tempArr.push(parseInt(letter))
            }
        })
        if(tempArr.length > 0) newArr.push(tempArr)
    })
   console.log(newArr) //이중배열완성
    
    
   const lengthArr = newArr.reduce((acc,item,index) => {
        return acc.concat(item.length)
   },[])
  
    let newLengthArr = [...lengthArr]
    newLengthArr.sort((a,b) => a-b).forEach((item) => {
        const tempItem = newArr[lengthArr.indexOf(item)]
        answer.forEach((num) => {
            tempItem.splice(tempItem.indexOf(num),1)
        })
        tempItem.forEach((temp) =>{
            answer.push(temp)
        })
    })
    
    return answer;
}