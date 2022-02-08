function solution(p) {
    //입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if(p === '') return '';
    
    let v = p.split("")
    return split(v);
}
    // u, v 를 분리함 
    // u는 균형잡힌 괄호 분자열로 더이상 분리할 수 없어야하며
    // v는 빈 문자열이 될 수 있음.
    function split(arr){
        console.log(`arr == ${arr}`)
       let str = ""
        if(arr.length == 0){
            return ""
        }
        let a = arr.shift()
        let v = []
        let u = [a]
        let count = a === '(' ? 1 : -1
        
        while(count != 0 && arr.length > 0){
            let b = arr.shift()
            b === '(' ? count++ : count--
            u.push(b)
        }
        v = [...arr]
        
        if(isCorrect(u)){
            console.log('isCorrect u ' + u + ' v == ' + v)
            str += u.join("") + split(v)
        }else{
            console.log('is not correct')
            let emptyStr = ""
            emptyStr += "("
            console.log('before split v== ' + v)
            emptyStr += split(v)
            emptyStr += ")"
            u = u.slice(1, u.length-1)
            u = u.map((v) => {
               return v === "(" ? ")" : "("
            }).join("")
            emptyStr += u
            return emptyStr
        }
        
        return str
    }

//0이면 correct한거임..
    function isCorrect(arr) {
        let tempArr = arr.map((v) => v)
        let stack = [tempArr.shift()];
        for(let value of tempArr) {
            let a = stack.pop(); //비교할 요소
            if(value === '(') { // )이면 안됨..!!!!!!
                stack.push(a)
                stack.push(value)
            }else{
                stack.pop()
            }
        }
        return stack.length === 0
    }
