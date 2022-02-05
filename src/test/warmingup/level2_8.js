function solution(numbers) {
    var answer = '';
    //greedy 인거 같음..
    //일단 1. 첫번째 인덱스에 있는 숫자가 가장 큰 애를 처음으로 세우자..
    //2. 첫번째 인덱스 숫자가 같으면, 길이가 더 긴 숫자중에서 두번째 있는 숫자가 더 큰 애를 앞으로 세우자..


    numbers.sort().reverse()
    console.log(numbers)
    
    //0만 있을 때
    let zeroCount = 0;    
    answer = numbers.reduce((acc, v, i, arr) => {
        if(v == 0) zeroCount++;
    
        if(String(v)[String(v).length - 1] == 0 && arr[i+1]){
            v = arr[i+1]
            arr[i+1] = arr[i]
        }
        return acc + v
    }, "")
    
    
    return answer.length != zeroCount ? answer : "0" ;
    
}