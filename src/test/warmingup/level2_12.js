function solution(priorities, location) {
    var answer = 0;
    let arr = makeArrayWithLocation(priorities) //2차원 배열로 location을 포함하여 만듦
    let count = 0;
    while(arr.length > 0){
        //인쇄
        const a = arr.shift();
        const max = getMax(arr);
        
        if(a[1] >= max) {
            count++; //출력되었음.
        }else{
            arr.push(a)
        }
        
        if(a[0] == location) {
            answer = count;
        }
    }
    
    return answer;
    
}

function makeArrayWithLocation(priorities){
    let newArray = priorities.map((priority, index) => {
        return [index, priority]
    })
    return newArray;
}


function getMax(arr) {
    let max = 0;
    arr.forEach((item) => {
        max = Math.max(max, item[1])
    })
    return max
}