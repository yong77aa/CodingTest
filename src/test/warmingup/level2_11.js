function solution(places) {
    places.forEach((item) => {
        let newList = makeList(item);
    
        newList.forEach((item, index , arr) => {
            let rowIndex = index;
            let array = arr;
            item.filter((value, index, arr) => {
                if(value === "P") {
                    console.log('index ==' + index + 'rowIndex == ' + rowIndex);
                    if(array[rowIndex+1][index+1]){
                        console.log(array[rowIndex+1][index+1])    
                    }
                    
                }
            })
        })
    })
    var answer = [];
    return answer;
}

function makeList(list){
    let newList = [];
    list.forEach((item) => {
        // let tempElement = item.split("")
        // newList.push(tempElement);
        let tempList = item.split("");
        newList.push(tempList)
    })
    return newList;
}

function inspectList(list){
    let tempList = [];
    list.filter((item, index, arr) => {
        if(item === "P"){
            tempList.push(index);
        }
    })
    return tempList
}