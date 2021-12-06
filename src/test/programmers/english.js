function solution(s) {
    var answer = 0;
    var arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for(let i = 0; i < arr.length; i++){
        while(s.includes(arr[i])){
           s = s.replace(arr[i], i)
        }
    }
    
    return parseInt(s);
}