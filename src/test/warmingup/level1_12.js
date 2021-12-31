function solution(price, money, count) {
    var answer = money;
    
    for(let i = 1; i <= count; i++) {
        answer = answer - i * price 
    }
    
    if(answer >= 0){
        answer = 0    
    }

    
    return Math.abs(answer);
}