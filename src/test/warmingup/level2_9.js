function solution(p) {
    let str = "";
    if(p === '') return str;
    let v = p.split("")
    recursion(v)
    
    
    function recursion(v){
        if(v.length == 0){
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

        if(u[0] != "("){
             u = u.map((i)=>{
            return i === "(" ? ")" : i === ")" ? "(" : ""
            })
            u[0] = "("
            u[u.length-1] = ")"
        }
        str += u.join("")
        recursion(v)
    }
    
 
    return str;
}

