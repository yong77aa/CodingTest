function solution(numbers) {
   
    var count = 0;
    var total = 0;
    for(let i = 0; i < 10; i++){
        total += i
    }
    numbers.filter((item) => {
        count += item
    })
    
    
    return total - count;
}