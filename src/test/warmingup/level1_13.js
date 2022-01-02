function solution(n, arr1, arr2) {
    var answer = [];
    var firstList = makeList(n,arr1);
    var secondList = makeList(n,arr2);
    
    for(let i = 0 ; i < n ; i++){
        let tempList = "";
        for(let j = 0; j < n; j++) {
            if((firstList[i][j] + secondList[i][j]) >= 1){
                tempList += '#'
            }else{
                tempList += ' '
            }
        }
         answer.push(tempList)
    }
    return answer;
}

function makeList(n, arr){
    var list = []; 
    for(let i = 0; i < arr.length; i++){
            var innerList = [];
            var num = arr[i]
            
            while(num > 0){
                innerList.unshift(num % 2)
                num = parseInt(num / 2)
            }
     
        while(innerList.length < n){
            innerList.unshift(0)
        }   
        list.push(innerList)
        
    }
    return list
}

