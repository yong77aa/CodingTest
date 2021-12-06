function solution(new_id) {
    var answer = '';
    let newId = new_id.toLowerCase();
  for(let i = 0; i < newId.length; i++) {
     let a = newId[i]
     let eng = /[a-zA-Z]/g; 
     if(!Number.isInteger(parseInt(a)) && !eng.test(a) && a != '-' && a != '_' && a != '.'){
        newId = newId.replace(a,'')
        i--;
     }
  }
    
   while(newId.includes('..')){
        newId = newId.replace('..','.')
   } //3

   newId = removeDot(newId) //4

    if(!newId){
        newId = "a"
    } //5
    
    if(newId.length >= 16) {
        newId = newId.slice(0,15)
    }
    newId = removeDot(newId)
    
    while(newId.length<=2){
        newId = newId.concat(newId[newId.length - 1])
    }
    
    return newId;
}
function makeRightStr(str, banStr){
    while(str.includes(banStr)){
       str = str.replace(banStr,'');
    }
    return str
}

function removeDot(str) {
    if(str[0] == '.'){
        str = str.slice(1,str.length)
    }
    
    if(str[str.length-1] == '.'){
        str = str.slice(0, str.length -1)
    }
    
    return str
}