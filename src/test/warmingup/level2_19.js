function solution(info, query) {
    const arr = [];
    const queryArr = query.map((item) => {
        item = item.replace(/and /g, '')
        return item.split(" ")
    })
    
    const tempArr = info.map((item) => {
       return item.split(" ");
    })
    
    queryArr.forEach((conditions) => {
        let count = 0;
        tempArr.forEach((personItem, personIndex) => {
            let isSatisfied = true
            personItem.toString().split(",").forEach((personCondition, index) => {
                if(!isSatisfied) return
                const personItemIndex = (personItem.toString().split(",").length -1)
                if(personItemIndex == index){
                    parseInt(conditions[index]) <= parseInt(personCondition) ? isSatisfied = true : isSatisfied = false
                }else if(conditions[index] !== '-'){
                    personCondition === conditions[index] ? isSatisfied = true : isSatisfied = false
                }
            })
            isSatisfied ? count++ : ''  
        })
        arr.push(count)
    })
    return arr;
}