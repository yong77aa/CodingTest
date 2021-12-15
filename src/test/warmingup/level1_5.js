//모의고사
function solution(answers) {
    let answer = [];
    
    let a = [1,2,3,4,5]
    let b = [2,1,2,3,2,4,2,5]
    let c = [3,3,1,1,2,2,4,4,5,5]
    
    let countList= [0,0,0]
    
    for(let i = 0; i < answers.length; i++) {
        let d = answers[i]
        
        let aNum = a[i % a.length]
        let bNum = b[i % b.length]
        let cNum = c[i % c.length]
        
        if(d === aNum){
            countList[0]++;
        }
        if(d === bNum){
            countList[1]++;
        }
        if(d === cNum){
            countList[2]++;
        }
    }

    let max = 0
    for(let i = 0; i<countList.length; i++) {
        max = Math.max(max, countList[i]);
    } //최대값 구하기
    
    for(let i = 0; i < countList.length; i++){
        if(countList[i] == max){
            answer.push(i+1);
        }
    }
    
    answer.sort(function(a,b){
        return a-b
    })
    
    
    return answer
}