function solution(numbers) {
    let answer = 0;    
    const newNumbers = numbers.split("")
    
    let n = 1 //1부터
    let visited = new Array(numbers.length).fill(0)
    
    const getPermutations = (array, selectNumber) => {
          const results = [];
          if (selectNumber === 1) {
            return array.map((element) => [element]);
          }
          array.forEach((fixed, index, origin) => {
            const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
            const permutations = getPermutations(rest, selectNumber - 1);
            const attached = permutations.map((permutation) => [fixed, ...permutation]);
            results.push(...attached);
          });
          return results;
    };
    
    const numberList = [];
    while(n <= numbers.length){
        //n으로돌때
        const numberString = getPermutations(newNumbers, n).filter((arr) => {
            numberList.push(arr.join(""))
        })
        // console.log(numberString)
        // console.log(isPrime(parseInt(numberString)))
        n++;
    }
    
   let newNumberList = numberList.map((item) => {
        return parseInt(item)
    })
   const tempSet = new Set(newNumberList) //중복제거
   newNumberList = [...tempSet]
    
    newNumberList.forEach((item) => {
        console.log(item)
        console.log(parseInt(item))
        isPrime(parseInt(item)) === true ? answer++ : ""
    })
   return answer
}


function isPrime(number){
    for(let i = 2; number > i; i++) {
        if(number % i === 0) { 
        return false;
    }
  }
 return number > 1;
}