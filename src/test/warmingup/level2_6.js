// 문제 설명
// 레스토랑을 운영하던 스카피는 코로나19로 인한 불경기를 극복하고자 메뉴를 새로 구성하려고
// 고민하고 있습니다. 기존에는 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서
//새로운 메뉴를 제공하기로 결정했습니다. 어떤 단품메뉴들을 조합해서 코스요리 메뉴로 구성하면 좋을 지
// 고민하던 스카피는 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다.
// 단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다. 또한, 최소 2명 이상의 손님으로부터
//주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.

// 예를 들어, 손님 6명이 주문한 단품메뉴들의 조합이 다음과 같다면,
//(각 손님은 단품메뉴를 2개 이상 주문해야 하며, 각 단품메뉴는 A ~ Z의 알파벳 대문자로 표기합니다.)

// 손님 번호	주문한 단품메뉴 조합
// 1번 손님	A, B, C, F, G
// 2번 손님	A, C
// 3번 손님	C, D, E
// 4번 손님	A, C, D, E
// 5번 손님	B, C, F, G
// 6번 손님	A, C, D, E, H
// 가장 많이 함께 주문된 단품메뉴 조합에 따라 스카피가 만들게 될 코스요리 메뉴 구성 후보는 다음과 같습니다.

// 코스 종류	메뉴 구성	설명
// 요리 2개 코스	A, C	1번, 2번, 4번, 6번 손님으로부터 총 4번 주문됐습니다.
// 요리 3개 코스	C, D, E	3번, 4번, 6번 손님으로부터 총 3번 주문됐습니다.
// 요리 4개 코스	B, C, F, G	1번, 5번 손님으로부터 총 2번 주문됐습니다.
// 요리 4개 코스	A, C, D, E	4번, 6번 손님으로부터 총 2번 주문됐습니다.

// 문제
// 각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, 스카피가 추가하고 싶어하는 코스요리를
//구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때, 스카피가 새로 추가하게 될 코스요리의 메뉴 구성을
//문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

// 제한사항
// orders 배열의 크기는 2 이상 20 이하입니다.
// orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
// 각 문자열은 알파벳 대문자로만 이루어져 있습니다.
// 각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.
// course 배열의 크기는 1 이상 10 이하입니다.
// course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
// course 배열에는 같은 값이 중복해서 들어있지 않습니다.
// 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
// 배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
// 만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
// orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.

// # 입출력 예

// orders	course	result
// [“ABCFG”, “AC”, “CDE”, “ACDE”, “BCFG”, “ACDEH”]	[2,3,4]	[“AC”, “ACDE”, “BCFG”, “CDE”]
// [“ABCDE”, “AB”, “CD”, “ADE”, “XYZ”, “XYZ”, “ACD”]	[2,3,5]	[“ACD”, “AD”, “ADE”, “CD”, “XYZ”]
// [“XYZ”, “XWY”, “WXA”]	[2,3,4]	[“WX”, “XY”]

// 생각해보자..
// orders의 배열의 크기는 2이상 20이하 이다.
//

function solution(orders, course) {
  var answer = [];
  order(orders); //orders 를 정렬 함
  //1. 순서가 상관없는 조합은 정렬을 처음에 해주는게 좋다. -> 정렬하기
  //2. 재귀로 조합을 실행시키고, Hashmap에 메뉴와, 메뉴 카운트를 센다.
  //3. 많이 카운트 된 메뉴들을 answer에 넣는다
  //4. answer을 sort한다.

  let map = new Map();

  const combination = (order, others, count) => {
    // 1. order = 현재까지 조합된 string
    // 2. others = 남아있는 알파벳
    // 3. 추가해야하는 알파벳 수
    //종료조건
    if (count === 0) {
      console.log(order);
      if (map.has(order)) {
        map.set(order, map.get(order) + 1);
      } else {
        map.set(order, 1);
      }
      return;
    }

    others.forEach((v, i) => {
      combination(order + v, others.slice(i + 1), count - 1);
    });
  };

  course.forEach((count, i) => {
    orders.forEach((v, i) => {
      combination("", v.split(""), count);
    });

    let max = Math.max(...map.values());

    map.forEach((value, key, map) => {
      console.log(`value == ${value} , key == ${key}`);
      if (max > 1 && max === value) {
        answer.push(key);
      }
    });
    //map clear

    map.clear();
  });

  return answer.sort();
}

function order(list) {
  for (let i = 0; i < list.length; i++) {
    list[i] = list[i]
      .split("")
      .sort()
      .reduce((a, r) => {
        return a + r;
      }, "");
  }
}
