function solution(s){
    var answer = true;
    var pNum = 0
    var yNum = 0
    var newString = s.toLowerCase();
     
    newString.split("").forEach((item) => {
        console.log(item)
        if(item == 'p'){
            pNum++
        }else if(item == 'y'){
            yNum++
        }
    })
 
     if(pNum == 0 && yNum == 0){
         answer = true
     }else if(pNum != yNum){
         answer = false
     }else {
         answer = true
     }
 
     return answer;
 }