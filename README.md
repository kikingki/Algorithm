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
    가입한 사이트와 비밀번호를 저장하고, 비밀번호를 찾으려는 사이트 주소를 입력하면 해당 사이트의 비밀번호를 출력하는 문제. 딕셔너리 자료형을 이용해     풀었고, 첫 시도에 맞추긴 했지만 input을 사용했을 때 입력 값이 많다보니 시간이 너무 오래 걸린다는 단점이 있었다. readline 함수를 사용하니 속도가     훨씬 단축됐다.
  + ##### [BOJ 1978](../master/1978번.py)
    주어진 N개의 수 중 소수를 찾는 문제. 에라토스테너스의 체 알고리즘을 이용했다. 입력받은 리스트에서 가장 큰 값으로 소수 리스트를 만들고, 반복문을     돌려 소수 리스트 중 입력된 수의 개수만 더해 출력했다.
    + 소수를 찾는 반복문을 돌릴 때 √N까지만 확인하는 방법이 시간복잡도가 O(√N)으로 가장 효율적이다.
    <br/>
#### 21.1.13
  + #### [BOJ 1018](../master/1018번.py)
    MxN 크기의 보드판을 8x8크기로 잘라 체스판으로 사용하기 위해 바꿔 칠해야하는 최소 횟수를 구하는 문제. 브루트포스 알고리즘을 이용했다. 행과 열의 인덱스 합의 홀짝에 따라 체크무늬인지 확인할 수 있으므로 바꿔야 하는 색의 수를 모두 센 후 최솟값을 출력했다.
    <br/>
