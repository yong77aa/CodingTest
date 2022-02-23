function solution(priorities, location) {
    var answer = 0;
    
    let result = getPriorityMapAndLocationLetter(priorities, location) //Letter, 
    
    let mapWithLetterAndIndex = result[0]; // letter + index map
    let locationLetter = result[1]; //location 에 해당하는 알파벳 글자
    
    //console.log('mapWithLetterAndIndex == ' + [...mapWithLetterAndIndex.keys()])
    
   let mapArray = [...mapWithLetterAndIndex.entries()]; //array로 반환 [알파벳, 중요도]
    let testArray = [];
    let max = ""
    while(mapArray.length > 0){
        //하나라도 남아있을 때는 이걸 해야함
        //비교해야해..
       let a = mapArray.shift(); //가장 앞에 있는 요소를 꺼냅니다.
        if(getMax(mapArray)[0]){
             max = getMax(mapArray)[0][1] //최대 값
        }
       if(a[1] >= max){
           //이거보다 중요도가 높은것이 없을 때
           testArray.push(a);
       }else{
           mapArray.push(a)
       }
    }
    
    console.log('testArray == ' + testArray);
}

function getPriorityMapAndLocationLetter(arr, location){
    let newMap = new Map();
    let locationLetter = "";
    for(let i = 65; i < 65 + arr.length; i++){
        let a = String.fromCharCode(i)
        // newMap.set(a, arr[i-65])
        newMap.set(a,arr[i-65])
        if(location == i-65){
            locationLetter = a
        }
    }
    
    return [newMap, locationLetter];
    
}

function getMax(arr){
    arr.sort((a,b) => {
        return b[1] - a[1]
    })
    return arr
}