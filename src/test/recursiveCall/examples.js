// recursion에서 자주쓰이는 식들을 정리함

// 정수를 2진법의 수로 바꾸기
// 자바스크립트에서 몫만 가져오려면 자바와 다르게 parseInt로 묶어주어야함 *** 중요
function printInBinary(num){
    let str = ""
    if(num < 2) str += num 
    else{
        printInBinary(parseInt(num/2))
        str += num%2 //마지막까지 깊게 들어간 시점부터 무언가 하고싶다면 순서를 재귀 먼저 그 이후에 어떤 작업을 넣으면 되더라.. (컴퓨터가 기본적으로 스택구조로 실행되기때문)
    }
    
    return str
}






