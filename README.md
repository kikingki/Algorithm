# Algorithm🌱
#### 20.12.26
  + ##### [BOJ 1259](../master/1259번.py)
    입력된 수가 팰린드롬 수인지 판단하는 문제. 
    input으로 0이 들어올 경우 break로 프로그램을 종료했고, 반복문으로 리스트를 앞과 뒤에서 순차적으로 비교하여 틀릴 경우 'no'를 출력했다.
  + ##### [BOJ 11004](../master/11004번.py)
    N개의 수를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 문제. 
    map 메소드로 입력된 수를 int형으로 변환하고 list 자료형으로 바꿨다. 그 후 sort 메소드를 사용해 정렬한 후 인덱스를 이용해 풀었다.
    + sort는 리스트 원본을 직접 수정하고, sorted는 정렬된 새로운 리스트를 반환한다.
    <br/>
#### 21.1.5
  + ##### [BOJ 17219](../master/17219번.py)
    가입한 사이트와 비밀번호를 저장하고, 비밀번호를 찾으려는 사이트 주소를 입력하면 해당 사이트의 비밀번호를 출력하는 문제. 딕셔너리 자료형을 이용해 풀었고, 첫 시도에 맞추긴 했지만 input을 사용했을 때 입력 값이 많다보니 시간이 너무 오래 걸린다는 단점이 있었다. readline 함수를 사용하니 속도가 훨씬 단축됐다.
  + ##### [BOJ 1978](../master/1978번.py)
    주어진 N개의 수 중 소수를 찾는 문제. 에라토스테너스의 체 알고리즘을 이용했다. 입력받은 리스트에서 가장 큰 값을 구해 에라토스테너스의 체로 소수 리스트를 만들고, 반복문을 돌려 소수 리스트 중 입력된 수의 개수만 더해 출력했다.
    + 소수를 찾는 반복문을 돌릴 때 √N까지만 확인하는 방법이 시간복잡도가 O(√N)으로 가장 효율적이다.
    <br/>
#### 21.1.13
  + #### [BOJ 1018](../master/1018번.py)
    MxN 크기의 보드판을 8x8크기로 잘라 체스판으로 사용하기 위해 바꿔 칠해야하는 최소 횟수를 구하는 문제. 브루트포스 알고리즘을 이용했다. 행과 열의 인덱스 합으로 조건문을 구성하여 쉽게 체크무늬인지 확인할 수 있었다. 첫 칸이 검은색일 경우 칠해야 하는 수와 첫 칸이 흰색일 경우 칠해야 하는 수를 각각 모두 세고 count_list에 추가한 후 최솟값을 출력했다.
    + 브루트포스 알고리즘은 시간과 자원을 아주 많이 소요된다는 점이 단점이지만 정확도는 100%이다.
    
    <br/>
#### 21.1.14
  + #### [BOJ 11399](../master/11399번.py)
    N명의 사람들이 ATM에서 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 문제. 그리디 알고리즘을 이용했다. 인출시간이 빠른 순서대로 인출하는 것이 그 순간의 최적 선택이므로 sort() 메서드로 정렬했다. 반복문으로 각 사람이 인출하는데 걸리는 시간을 sum에 누적시킨 후, time에 모두 더해 시간의 합을 구했다.
      (수정) min과 sum이 오버라이딩되므로 min을 t로, sum을 ac로 수정했고, map 객체를 리스트로 바꾸지 않고 sorted() 메서드로 바로 정렬하도록 수정했다.
    + 그리디 알고리즘은 그 순간에서 최적인 경우를 선택하는 것이므로 전체적으로 봤을 때 가장 최적이라고 할 수는 없다. 탐욕스러운 선택 조건, 최적 부분 구조 조건이라는 조건이 성립되면 그리디 알고리즘으로 가장 최적의 선택을 구할 수도 있다. 하지만 계산속도가 빨라 근사 알고리즘으로 사용하기 좋다.
    <br/>
#### 21.1.15
  + #### [BOJ 1110](../master/1110번.py)
    입력받은 수의 각 자리의 수를 더한 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙여 새로운 수를 만들고 이를 반복해 새로운 수가 처음 입력값과 같아질 때 까지 걸리는 횟수를 구하는 문제. 문자열의 슬라이싱을 이용해 주어진 수의 일의 자리 수와 새로운 수의 일의 자리 수를 이어 붙였고 이를 반복하다가 초기값과 새로운 수가 같으면 반복을 종료했다. 문자열로 풀었기 때문에 10 이하의 수이면 십의 자리에 '0'을 추가했다. 
      (수정) 슬라이싱을 사용해 풀었었는데 다른 풀이를 참고해보니 문자열로 변환하지 않고 %와 //를 활용하면 더 쉽게 풀 수 있음을 알게 됐다. int형이므로 n이 10이하일 경우를 고려해 코드를 추가하지 않아도 돼서 간단했다. 그리고 if문을 while문의 처음에 넣었을 때, 입력이 0일 경우에 무한반복에 걸려 오류가 나서 cycle이 1 이상이라는 조건을 추가했었다. 하지만 if문을 while문의 맨마지막에 작성하면 자연스럽게 cycle이 한번은 돌기 때문에 추가적인 조건을 덧붙이지 않아도 됨을 알게 됐다. 이 문제를 풀면서 코드의 순서 역시 중요하게 생각해야 함을 느꼈다.
