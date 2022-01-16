function solution(strings, n) {
    strings.sort()
    
    strings.sort((a,b)=>{
        return a.charCodeAt(n) - b.charCodeAt(n);        
    })
    
    
    return strings;
}