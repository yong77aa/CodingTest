function solution(p) {
    var answer = '';
    
    if(p === '') return answer;
    let v = p.split("")
    recursion(v)
    return answer;
}

function recursion(v,str){
    if(v.length < 2){
        return
    }
    
    let a = v.shift()
    let u = [a]
    let count = a === '(' ? 1 : -1
    
    while(count != 0 && v.length > 0){
        let b = v.shift()
        b === '(' ? count++ : count--
        u.push(b)
    }
    
    //올바른 문자열 인지 체크하는 로직 추가(stack)
    
    recursion(v)
}