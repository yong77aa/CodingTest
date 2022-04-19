function solution(info, query) {
    var answer = [];
    const arr = [];
    const queryArr = query.map((item) => {
        item = item.replace(/and /g, '')
        return item.split(" ")
    })
    
    const tempArr = info.map((item) => {
       return item.split(" ");
    })
    
    queryArr.forEach((conditions) => {
        let isSatisfied = false;
        let count = 0;
        conditions.forEach((condition, index) => {
            tempArr.forEach((personItem, personIndex) => {
                if(index === condition.length -1){
                   personItem[index] <= condition[condition.length - 1] ? isSatisfied = true : isSatisfied = false
                    //console.log(isSatisfied)
                }else if(index < condition.length - 1){
                    personItem.indexOf(condition) ? isSatisfied = true : isSatisfied = false;   
                   // console.log(isSatisfied)
                }
                
            })
          isSatisfied ? count++ : ''
        })
          arr.push(count)
    })
    console.log(arr)
    
    return answer;
}