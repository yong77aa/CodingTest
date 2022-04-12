function solution(n,a,b)
{
    let answer = 1;
    let firstPair = makePair(a)
    let secondPair = makePair(b)
    
    
    while(!secondPair.includes(getEvenNum(firstPair))){
        firstPair = makePair(getEvenNum(firstPair)/2)
        secondPair = makePair(getEvenNum(secondPair)/2)
        answer++;
    }
    
    return answer;
}

function makePair(number){
    return number % 2 === 0 ? [number-1, number] : [number, number + 1]
}

function getEvenNum(arr) {
    return Math.max(arr[0], arr[1])
}