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
    
    const booleanArr = [];
    
    queryArr.forEach((conditions) => {
        
        console.log('conditions == ' + conditions)
        let count = 0;
        tempArr.forEach((personItem, personIndex) => {
            let isSatisfied = true
            personItem.forEach((personCondition, index) => {
                console.log('conditions[index] == ' + conditions[index] + 'personCondition == ' + personCondition)
                if(personItem.length -1 === index && isSatisfied){
                    conditions[index] <= personCondition ? isSatisfied = true : isSatisfied = false
                    console.log('conditions[index] <= personCondition ' + conditions[index] <= personCondition )
                    //if(isSatisfied) count++;
                }else if(isSatisfied && conditions[index] !== '-'){
                    personCondition === conditions[index] ? isSatisfied = true : isSatisfied = false
                }
                //console.log(conditions[index])
                // conditions.forEach((condition, index) => {
                // //조건 하나 씩
                //     console.log('personConditioin == ' + personCondition + 'condition == ' + condition)
                // })
            })
            console.log('isSatisfied == ' + isSatisfied)
           isSatisfied ? count++ : ''
            
        })
        
        arr.push(count)
    })
    console.log(arr)
    return arr;
}