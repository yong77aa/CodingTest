function solution(str1, str2) {
    // 입력으로 str1, str2가 들어온다.
    const MULTI_NUM = 65536
    
    const newArray1 = makeNewArray(str1)
    const newArray2 = makeNewArray(str2)
    
    if(newArray1.length < 1 && newArray2.length < 1){
        return MULTI_NUM
    }
    
    //유사도 계산
    let a = newArray1.length >= newArray2 ? newArray1 : newArray2;
    let b = newArray2.length < newArray2 ? newArray2 : newArray1;
    console.log(a, b)
    let intersection = 0;
    let union = newArray1.length + newArray2.length;
    
    b.forEach((i) => {
        if(a.includes(i)){
            console.log(`igggg`)
            intersection++;
            a = a.splice(a.indexOf(i), 1)
        }
    })
    
    return Math.floor(intersection / union * MULTI_NUM);
}

//문자를 2개씩 자르는 함수
function makeNewArray(str){
    let newArray = str.split("").map((v,i,arr) => {
        if(i < arr.length -1){
            return v.toLowerCase() + arr[i+1].toLowerCase()
        }else{
            return ''
        }
    })
    newArray = newArray.slice(0, newArray.length-1)
    
    return validationCheck(newArray)
}

//validationCheck를 통해 새로운 array를 return함
function validationCheck(arr){
    let reg1 = /[`~!@#$%^&*()_|+\-=?;:'"<>\{\}\[\]\\\/ ]/gim;
    let reg2 = /[0-9]/gim;
    let newArray = arr.map((i) => i.replace(reg1,"").replace(reg2,"")).filter((i) => i.length === 2)
    return newArray
}


