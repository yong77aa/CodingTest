function solution(number, k) {
    var answer = '';
    var list = [];
    var numberList = number.split("")
    
    list[0] = number[0];
    
    for(let i = 1; i<numberList.length; i++){
       if(k > 0){
           while(parseInt(list[list.length-1]) < parseInt(numberList[i]) && k > 0){
               list.pop()  
               k--
           }
           list.push(numberList[i]);
           
       }else {
            list.push(numberList[i])
        }
    }
    
    return "".concat(...list);
}