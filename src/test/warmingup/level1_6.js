//폰켓몬
function solution(nums) {
    
    let limitNumber = nums.length/2

    let newNums = [... new Set(nums)] //중복제거를 이렇게하는구나..신기함


    return newNums.length > limitNumber ? limitNumber : newNums.length;
}