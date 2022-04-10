function solution(s) {
    let answer = [];
    let newArr = [];
    let tempArr = []
    const str = s.split(",").forEach((item, index) => { 
        console.log(item)
        // if(index != 0 && index != s.split("").length -1){
        //     if(item != "{" && item != "}" && item != ","){
        //         tempArr.push(item * 1)
        //     }else if(item == "}"){
        //         let newTempArr = [...tempArr]
        //         newArr.push(newTempArr)
        //         tempArr = [];
        //     }
        // }
    })
    
   const lengthArr = newArr.reduce((acc,item,index) => {
        return acc.concat(item.length)
   },[])
  
    // newArr.forEach((item) => {
    //     if(item.length === 1){
    //         answer.shift(item)
    //     }
    // })
    
    return answer;
}