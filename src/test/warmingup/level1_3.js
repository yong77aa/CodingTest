//완주못한선수
function solution(participant, completion) {
    
    //participant 참여선수
    //completion 완주한선수
    participant.sort();
    completion.sort();
    
    console.log(participant)
    console.log(completion)
    
    let person
    
    for(let i = 0; i < completion.length; i++) {
        if(completion[i] != participant[i]){
            person = participant[i]
            break;
        }
    }
    
    if(!person) {
       person = participant[participant.length-1]
    }
    
    return person
  
}