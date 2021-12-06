function solution(lottos, win_nums) {
    
    var answer = [];
    var zeroCount = 0;
    var rightCount = 0;
    lottos.filter((item) => {
        if(item == 0){
            zeroCount++;
        }
        
        if(win_nums.indexOf(item) >= 0){
            rightCount++;
        }
    })
    
    console.log('zerocount == ' + zeroCount)
    console.log('rightCount == ' + rightCount)
    
    
    answer.push(getWinNumber(rightCount + zeroCount))
    answer.push(getWinNumber(rightCount));
    return answer; 
}

function getWinNumber(count){
    let num = 0;
    switch(count){
        case 0 : num = 6; break;
        case 1 : num = 6; break;
        case 2 : num = 5; break;
        case 3 : num = 4; break;
        case 4 : num = 3; break;
        case 5 : num = 2; break;
        case 6 : num = 1; break;
    }
    return num;
}