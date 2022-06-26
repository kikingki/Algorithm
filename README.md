# Algorithm🌱
#### 20.12.26
  + ##### [BOJ 1259](../master/1259번.py)
    입력된 수가 팰린드롬 수인지 판단하는 문제. 
    input으로 0이 들어올 경우 break로 프로그램을 종료했고, 반복문으로 리스트를 앞과 뒤에서 순차적으로 비교하여 틀릴 경우 'no'를 출력했다.
  + ##### [BOJ 11004](../master/11004번.py)
    N개의 수를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 문제. 
    map 메소드로 입력된 수를 int형으로 변환하고 list 자료형으로 바꿨다. 그 후 sort 메소드를 사용해 정렬한 후 인덱스를 이용해 풀었다.
    + sort는 리스트 원본을 직접 수정하고, sorted는 정렬된 새로운 리스트를 반환한다.

#### 21.1.5
  + ##### [BOJ 17219](../master/17219번.py)
    가입한 사이트와 비밀번호를 저장하고, 비밀번호를 찾으려는 사이트 주소를 입력하면 해당 사이트의 비밀번호를 출력하는 문제. 딕셔너리 자료형을 이용해 풀었고, 첫 시도에 맞추긴 했지만 input을 사용했을 때 입력 값이 많다보니 시간이 너무 오래 걸린다는 단점이 있었다. readline 함수를 사용하니 속도가 훨씬 단축됐다.
  + ##### [BOJ 1978](../master/1978번.py)
    주어진 N개의 수 중 소수를 찾는 문제. 에라토스테너스의 체 알고리즘을 이용했다. 입력받은 리스트에서 가장 큰 값을 구해 에라토스테너스의 체로 소수 리스트를 만들고, 반복문을 돌려 소수 리스트 중 입력된 수의 개수만 더해 출력했다.
    + 소수를 찾는 반복문을 돌릴 때 √N까지만 확인하는 방법이 시간복잡도가 O(√N)으로 가장 효율적이다.

#### 21.1.13
  + #### [BOJ 1018](../master/1018번.py)
    MxN 크기의 보드판을 8x8크기로 잘라 체스판으로 사용하기 위해 바꿔 칠해야하는 최소 횟수를 구하는 문제. 브루트포스 알고리즘을 이용했다. 행과 열의 인덱스 합으로 조건문을 구성하여 쉽게 체크무늬인지 확인할 수 있었다. 첫 칸이 검은색일 경우 칠해야 하는 수와 첫 칸이 흰색일 경우 칠해야 하는 수를 각각 모두 세고 count_list에 추가한 후 최솟값을 출력했다.
    + 브루트포스 알고리즘은 시간과 자원을 아주 많이 소요된다는 점이 단점이지만 정확도는 100%이다.

#### 21.1.14
  + #### [BOJ 11399](../master/11399번.py)
    N명의 사람들이 ATM에서 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 문제. 그리디 알고리즘을 이용했다. 인출시간이 빠른 순서대로 인출하는 것이 그 순간의 최적 선택이므로 sort() 메서드로 정렬했다. 반복문으로 각 사람이 인출하는데 걸리는 시간을 sum에 누적시킨 후, time에 모두 더해 시간의 합을 구했다.
    
    
    (수정) min과 sum이 오버라이딩되므로 min을 t로, sum을 ac로 수정했고, map 객체를 리스트로 바꾸지 않고 sorted() 메서드로 바로 정렬하도록 수정했다.
    + 그리디 알고리즘은 그 순간에서 최적인 경우를 선택하는 것이므로 전체적으로 봤을 때 가장 최적이라고 할 수는 없다. 탐욕스러운 선택 조건, 최적 부분 구조 조건이라는 조건이 성립되면 그리디 알고리즘으로 가장 최적의 선택을 구할 수도 있다. 하지만 계산속도가 빨라 근사 알고리즘으로 사용하기 좋다.

  #### 21.1.15
  + #### [BOJ 1110](../master/1110번.py)
    입력받은 수의 각 자리의 수를 더한 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙여 새로운 수를 만들고 이를 반복해 새로운 수가 처음 입력값과 같아질 때 까지 걸리는 횟수를 구하는 문제. 문자열의 슬라이싱을 이용해 주어진 수의 일의 자리 수와 새로운 수의 일의 자리 수를 이어 붙였고 이를 반복하다가 초기값과 새로운 수가 같으면 반복을 종료했다. 문자열로 풀었기 때문에 10 이하의 수이면 십의 자리에 '0'을 추가했다. 
    
    
    (수정) 슬라이싱을 사용해 풀었었는데 다른 풀이를 참고해보니 문자열로 변환하지 않고 %와 //를 활용하면 더 쉽게 풀 수 있음을 알게 됐다. int형이므로 n이 10이하일 경우를 고려해 코드를 추가하지 않아도 돼서 간단했다. 그리고 if문을 while문의 처음에 넣었을 때, 입력이 0일 경우에 무한반복에 걸려 오류가 나서 cycle이 1 이상이라는 조건을 추가했었다. 하지만 if문을 while문의 맨마지막에 작성하면 자연스럽게 cycle이 한번은 돌기 때문에 추가적인 조건을 덧붙이지 않아도 됨을 알게 됐다. 이 문제를 풀면서 코드의 순서 역시 중요하게 생각해야 함을 느꼈다.

#### 21.1.19
  + #### [BOJ 2798](../master/2798번.py)
    N장의 카드에서 3개의 카드를 골라 그 합이 M과 가장 가까운 값을 구하는 문제. 브루트포스 알고리즘을 이용해 풀었다. for문을 중첩해 모든 카드의 합을 구하면서 M보다 작은 값 중 최댓값을 구했다.

#### 21.1.20
  + #### [BOJ 10866](../master/10866번.py)
    정수를 저장하는 덱(Deque)을 구현한 다음, 입력으로 주어지는 프로그램을 작성하는 문제. Deque 클래스를 만들고 8가지 명령을 리스트의 insert(), append(), pop() 메서드를 사용해 함수로 만들었다. 그리고 main에서 Deque 객체를 만들고 입력을 받아 조건에 맞는 함수를 불러왔다. 다양한 리스트 함수를 정확히 활용할 수 있게 됐고, 리스트를 끝에서부터 불러오고 싶으면 인덱스로 -n을 사용해서 간결히 해결할 수 있음을 알게 됐다.
    + 리스트로 deque를 구현했는데, insert() 메서드는 모든 요소가 메모리에서 이동될 수 있어 최악 경우 시간복잡도가 O(N)이므로 비효율적이라고 한다. 파이썬에서 제공하는 collections 패키지의 deque 모듈은 이중 연결 리스트로 구현하여 O(1) 시간에 연산이 가능하다. 

#### 21.1.22
  + #### [BOJ 2941](../master/2941번.py)
    입력한 단어에서 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력하는 문제. 처음엔 크로아티아 알파벳을 croa 리스트에 저장하고, word 변수에 입력 값을 저장했다. 이 리스트로 반복문을 돌고, if문으로 word 안에 크로아티아 알파벳이 있으면 count 값을 증가하는 방법으로 풀었다. 이렇게 푸니 'dz=' 알파벳의 경우 'z='와 중복돼 count가 2번 증가하는 문제가 발생했다. 그래서 replace() 메서드를 이용해 크로아티아 알파벳을 공백 문자로 치환한 다음 len(word)를 출력해 해결했다. 리스트를 순차적으로 순회하기 때문에 리스트에 'z='가 'dz='보다 앞 순서이면 'dz='가 'd '로 치환되는 문제가 있을 수 있으니 순서를 유의해야할 것 같다.

#### 21.1.24
  + #### [BOJ 1427](../master/1427번.py)
    한줄로 입력받을 수를 내림차로 정렬한 후 출력하는 문제. sorted(reverse=True)로 내림차순 정렬을 했다. 문자열을 리스트로 분할하는 split() 메서드는 많이 사용해봤는데, 반대로 리스트를 문자열로 합치는 join() 메서드는 처음 사용해봤다.
    + sorted(reverse=True)는 기준에 따라 내림차순 정렬을 하는 것이고, reverse()는 단순히 리스트의 순서를 뒤집는 것이므로 잘 구분해야 한다.
  + #### [BOJ 10828](../master/10828번.py)
    정수를 저장하는 스택(Stack)을 구현한 다음, 입력으로 주어지는 프로그램을 작성하는 문제. Stack 클래스를 만들고 pop(), append() 메서드를 사용해 함수를 구현했다. 스택은 배열의 끝에서만 데이터에 접근이 가능한 LIFO 구조이기 때문에 시간복잡도가 모두 O(1)이다. 
    + 스택은 깊이 우선 탐색(DFS)에서 유용하게 사용된다.

#### 21.1.27
  + #### [BOJ 1260](../master/1260번.py)
    그래프를 깊이 우선 탐색(DFS)로 탐색한 결과와 너비 우선 탐색(BFS)로 탐색한 결과를 출력하는 문제. DFS는 스택, BFS는 큐를 사용하여 구현했다. 큐와 스택이 혼합된 구조인 collections 모듈의 deque를 사용했다. 생성한 deque 객체를 반복하며 방문하지 않은 정점일 경우 visited 리스트에 추가했다. 방문할 수 있는 정점이 여러개인 경우, 정점 번호가 작은 것을 방문하는 것이 조건이므로 stack은 내림차순 정렬, queue는 오름차순 정렬을 했다. 그리고 visited 리스트를 문자열로 변환한 뒤 반환했다. main에선 간선의 개수만큼 x,y를 입력받은 후, key의 value가 이미 있을 경우 append()로 value를 추가하고, 아닐 경우 딕셔너리 쌍을 추가했다. 또한, 양방향 연결이므로 x,y와 y,x를 모두 연결했다.
    + 백준에 제출해보니 런타임에러(KeyError)가 떠서 찾아보니 딕셔너리에 해당하는 key가 없을 때 발생하는 오류라고 한다. 각 함수에 조건문 if key in dict를 추가해 해결했다.
    
#### 21.1.28
  + #### [BOJ 2606](../master/2606번.py)
    웜 바이러스에 걸린 1번 컴퓨터를 통해 감염된 컴퓨터의 수를 출력하는 문제. 1번 컴퓨터와 연결된 모든 경로를 확인해야 할 경우 깊이 우선 탐색(DFS)이 적합하므로 dfs를 구현해 풀었다. bfs 메서드에서 감염된 컴퓨터 수를 세는 cnt 변수에서 1번 컴퓨터를 제외해야 하므로 cnt-1을 반환했다.
    + 너비 우선 탐색(BFS)은 일반적으로 목표지점까지의 최단 경로를 찾을 때 사용한다.

#### 21.1.29
  + #### [BOJ 2748](../master/2748번.py)
    n번째 피보나치 수를 구하는 다이나믹 프로그래밍 문제. 처음에 재귀 호출을 이용하여 풀었을 때, 시간초과가 발생했다. 이유를 찾아봤더니 재귀함수를 사용할 경우 중복되는 연산이 많아 시간복잡도가 O(2^n)이며, stack overflow 문제가 발생한다. 반복문을 사용할 경우 시간복잡도가 O(n)이라고 하여 반복문을 n번 돌려 피보나치 수를 구했다.
    + 다이나믹 프로그래밍은 큰 문제를 한 번에 해결하기 힘들 때 작은 여러 개의 문제로 나누어서 푸는 기법이다. 작은 문제로 나눴을 때 중복되는 연산이 발생하는데, 계산 값을 저장해두어 같은 문제는 다시 계산하지 않도록 한다.

#### 21.1.30
  + #### [BOJ 2217](../master/2217번.py)
    정보가 주어진 각 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구하는 문제. 리스트에 로프의 최대 중량을 입력받았다. k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 로프를 병렬로 연결하면 "각 로프에는 w/k만큼의 동일한 중량"이 걸리고, 모든 로프를 사용할 필요가 없다는 점이 포인트다. 입력받은 리스트를 최대 중량이 큰 순서대로(역순) 정렬한 후, 1번 로프가 견딜 수 있는 중량 x 1, 1번 로프와 2번 로프가 견딜 수 있는 중량 x 2 ... 식으로 반복해 최댓값을 리턴하는 함수를 작성했다. 
    + 첫 시도가 성공은 했지만 시간이 너무 오래걸려 readline() 메서드를 사용해보니 3948ms에서 140ms으로 시간이 크게 단축됐다. 로프의 갯수의 범위가 (1 ≤ N ≤ 100,000)이라는 큰 수이기 때문에 차이가 크다는 것을 느꼈다.

#### 21.1.31
  + #### [BOJ 2839](../master/2839번.py)
    Nkg의 설탕을 3kg 봉지와 5kg 봉지로 정확히 Nkg이면서 또 최소한인 봉지의 개수를 출력하는 문제. 반복문을 사용하지 않고 한번에 나눗셈과 나머지 연산을 실행했더니 3kg 봉지로만 정확히 나누어 떨어지는 경우에도 -1이 출력이 됐다. 방법을 바꿔 5kg의 배수로 딱 나뉘어 떨어질 때까지 설탕의 무게를 3kg씩 빼고 봉지의 개수를 1씩 더하는 것을 반복하다가 설탕의 무게가 5kg의 배수가 되면 5kg 봉지의 개수를 더한 후 봉지 개수의 총합을 출력했다. 또한 설탕의 무게가 음수가 되면 정확히 나누어지지 않는 것이므로 -1을 출력했다.

#### 21.2.2
  + #### [BOJ 14495](../master/14495번.py)
    자연수 n을 입력받아 n번째 피보나치 비슷한 수열을 구하는 다이나믹 프로그래밍 문제. 리스트를 사용했다는 점을 제외하면 피보나치 수열을 푸는 방법과 유사했다. 반복문으로 주어진 점화식을 이용해 해결했다.


    (수정) 코드를 좀 더 깔끔하게 약간 바꿨다.

#### 21.2.3
  + #### [BOJ 1463](../master/1463번.py)
    정수 N이 주어졌을 때 세가지 연산을 적절히 사용해 1을 만드는 연산 횟수의 최솟값을 구하는 문제. 어제 푼 문제보다 좀 더 난이도가 있는 다이나믹 프로그래밍 문제였다. 1을 뺀 경우, 2로 나눈 경우, 3으로 나눈 경우를 각각 리스트에 저장한다. 최솟값을 구하는 것이므로 기존의 1을 뺄 경우의 수와 비교해 최솟값일 때만 리스트에 저장했다.
    ```python
    dp[N] = min(dp[N-1], dp[N//2] , dp[N//3]) + 1
    ```
#### 21.2.4
  + #### [BOJ 11053](../master/11053번.py)
      가장 긴 증가하는 부분 수열을 구하는 문제. 'LIS: Longest Increasing Subsequence'라고 한다. 다이나믹 프로그래밍을 사용하는 대표적인 알고리즘 문제 중 하나이다. 수열을 입력받는 배열 arr와 LIS의 길이를 저장하는 배열 dp을 생성했다. 중첩 for문으로 원소를 하나 선택해 이전 원소들과 비교하여 현재 값이 이전 값보다 크고, 현재 원소의 이전 dp 값보다 dp[j]+1의 값이 더 클 경우 dp[i]에 dp[j]+1 값을 저장했다.
      + LIS 문제의 풀이 방법은 동적 프로그래밍과 이분 탐색이 있다. 동적 프로그래밍은 시간복잡도가 O(N^2)이고, 이분 탐색은 시간복잡도가 O(NlogN)으로 훨씬 빠르다. 하지만 이분탐색은 정답 수열을 알 수 없어 모든 LIS 문제에 사용할 순 없다.
  + #### [BOJ 11722](../master/11722번.py)
      가장 긴 감소하는 부분수열을 구하는 문제. 현재 원소와 이전 원소들을 비교하는 부등호만 반대이고, 최장 증가 부분수열을 구하는 코드와 동일하게 풀었다.

#### 21.2.5
  + #### [BOJ 1929](../master/1929번.py)
      M 이상 N 이하의 소수를 모두 출력하는 문제. M과 N의 범위가 (1 ≤ M ≤ N ≤ 1,000,000)로 매우 크므로 단순히 이중 for문을 사용할 경우 시간초과로 실패한다. 그래서 에라토스테네스의 체 알고리즘을 사용해 풀었다. 순회하는 수 i가 소수이면 i의 배수는 모두 합성수이므로 모두 False로 제외하다보면 점점 제외하는 수가 줄어든다. 그래서 에라토스테네스의 체도 이중 for문을 쓰지만 시간복잡도는 O(NloglogN)로 아주 빠르다.

#### 21.2.7
  + #### [BOJ 5543](../master/5543번.py)
    3개의 햄버거와 2개의 음료 가격을 입력받아 가장 싼 세트 메뉴의 가격을 출력하는 문제. 햄버거와 음료 리스트를 각자 따로 만들어 min() 함수를 사용해 가장 싼 세트 가격을 구했다.
  + #### [BOJ 16394](../master/16394번.py)
    특정 년도가 주어졌을 때, 1946년에 개교한 홍익대학교의 개교 몇 주년인지 출력하는 문제. 입력받은 숫자에서 1964를 빼서 출력하면 되는 간단한 문제였다.

#### 21.2.10
  + #### [BOJ 2579](../master/2579번.py)
    계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력하는 문제. 이 문제 역시 다이나믹 프로그래밍 문제이다. 도착 계단을 무조건 밟아야 하는 것이 규칙이므로 도착 계단을 밟은 상태에서 이전에 어떤 계단을 밟고 올라왔을 지 생각하는 편이 더 쉽다. 그렇다면 도착 계단의 전 계단을 밟지 않은 경우와 도착 계단의 전 계단을 밟은 경우의 두가지 경우가 있다. 즉, 이 문제의 점화식은 이렇게 도출된다. 수식에 n-3이 있으므로 반복의 범위를 3~n까지로 해주고 dp[0]~dp[2]에는 값을 직접 넣어준다. 
    
    
    (수정) n 값을 입력받아 stair 리스트와 dp 리스트를 n까지만 0으로 초기화해도 문제없는데 백준 사이트에서 IndexError가 발생한다. 그래서 문제에서 제시한 계단의 최대 개수 300까지 초기화해봤더니 통과되었다. -> n까지 초기화하는 경우 n이 0 또는 1일 때, stair[0]~stair[2]의 하드코딩 과정에서 IndexError가 발생하기 때문임을 알게 되었다.
    ```python
    dp[n] = max(dp[n-2] + stair[i], dp[n-3] + stair[i] + stair[i-1])
    ```

#### 21.2.17
  + #### [BOJ 1874](../master/1874번.py)
    임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 판단하고, 가능할 경우 push와 pop 연산 순서를 출력하는 문제. while문을 이용해 입력받은 num 값과 count 값이 같을 때까지 stack에 push하고 count를 1씩 더해준다. 반복이 끝나면 stack의 마지막 값과 num의 값을 비교해 동일할 경우 stack을 pop한다. 동일하지 않을 경우 입력된 수열을 만드는 것이 불가능하므로 가능 여부를 나타내는 temp 변수를 False로 선언한 후 break로 반복을 끝낸다. temp가 False이면 NO를 출력하고, 아니면 push와 pop 연산 순서를 담은 result 리스트를 출력한다.

#### 21.2.18
  + #### [BOJ 15649](../master/15649번.py)
    자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 문제. 백트래킹(Backtracking) 알고리즘을 이용해 풀었다. 중복을 체크하는 리스트 visited와 수열을 담는 리스트 num_list를 선언했다. n까지 반복을 돌며 visited[i]가 True면 이미 탐색을 한 지점이므로 중복이다. 이 경우 continue로 다음 반복을 시작한다. 탐색을 하지 않은 경우, 탐색점 visited[i]를 true로 변경해 재귀로 dfs를 호출하며, 깊이가 m과 동일해졌을 때 num_list를 출력하고 함수를 즉시 종료한다. 탐색이 다 끝난 경우 순열 문제이므로 탐색점을 다시 False로 변경해주고 이전 연산의 요소를 제거한다.
    + 백트래킹은 DFS 방식을 기반으로 하며, 불필요한 경우를 배제하며 원하는 답을 찾을 때까지 탐색하는 알고리즘이다. 불필요한 경우를 배재하는 '가지치기(Pruning)' 코드의 차이에 따라 속도 차이가 크다.
    + 함수에서 return이 있는 경우와 return이 없는 경우 어떤 차이가 있는지 헷갈려서 구글링을 해봤다. no return & no result의 경우엔 code block을 모두 실행한 다음 None을 반환하고 종료하고, return (no result)의 경우엔 함수를 즉시 종료한다고 한다.그래서 이 문제의 경우 return을 넣지 않는 경우 불필요한 반복이 계속되므로 꼭 넣어줘야 한다.
    + list가 비문자열일 경우 join() 메서드는 map() 메서드를 사용해 문자열로 바꿔줘야 한다. 이 때, '*array'를 사용하면 띄어쓰기를 기준으로 구분해 값을 반환해준다.
    + 파이썬의 내장함수 permutations를 사용해 순열을 찾는 방법도 있다.
    ```python
    from itertools import permutations

    n, m = map(int, input().split())
    num_list = [str(i) for i in range(1, n+1)]
    for i in permutations(num_list, m):
        print(' '.join(i))
    ```
  + #### [BOJ 15650](../master/15650번.py)
    자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 문제. 이 문제 역시 백트래킹 알고리즘을 이용해 풀었다. 15649번 문제와의 차이점은 고른 수열이 오름차순이어야 한다는 조건이 추가되었기 때문에 순열이 아닌 조합 문제이다. 즉, 탐색의 시작점인 visited[i]를 제외하고 그 이후의 값부터 False로 변경해주면 풀리는 문제이다.
    + 이 문제도 파이썬의 내장함수 combinations를 사용해 조합을 찾는 방법이 있다.
     ```python
    from itertools import combinations

    n, m = map(int, input().split())
    num_list = [str(i) for i in range(1, n+1)]

    for i in combinations(num_list, m):
        print(' '.join(i))
    ```
#### 21.2.23
  + #### [BOJ 7576](../master/7576번.py)
    하루가 지나면 상,하,좌,우의 토마토가 익는 상자에서 토마토가 모두 익는 최소 날짜를 출력하는 문제. 토마토의 한쪽 방향으로 쭉 익는 것이 아니라, 주변의 토마토가 익는 것이므로 BFS로 구현하는 것이 적합하다. n,m 크기의 이차원 배열을 입력받고, 이중반복문으로 처음부터 익어있는 토마토의 위치 좌표를 queue에 push한다. bfs 메서드에서 queue를 순회하며 익은 토마토의 좌표 값을 꺼내 dx와 dy 값에 더하며 상하좌우를 검사한다. 순회가 끝나고 박스 안의 안익은 토마토가 있는지 확인하여 있을 경우 -1을 리턴하고, 없을 경우 days 변수를 출력한다.

#### 21.5.22
  + #### [BOJ 9251](../master/9251번.py)
    주어진 두 수열의 부분 수열 중 가장 긴 것을 찾는 문제. LCS(Longest Common Subsequence) 문제도 다이나믹 프로그래밍을 사용하는 알고리즘이다. 두 문자열을 받고, LCS 길이를 저장할 배열 dp를 생성했다. 중첩 for문으로 첫 번째 문자열 str1을 기준점으로 잡고, 두 번째 문자열 str2의 문자를 하나씩 늘려가면서 비교했다. 끝 문자열이 동일할 경우와 끝 문자열이 다를 경우 이 2가지의 재귀적 관계를 갖고 있다.
    + 다이나믹 프로그래밍은 최적 부분 구조를 갖고, 재귀적으로 구현했을 경우 심각한 중복 호출이 발생할 때 사용한다.
    ```python
        if (str1[i-1]==str2[j-1]):
            dp[i][j] = dp[i-1][j-1]+1
        
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    ```

#### 21.7.16
  + #### [BOJ 1546](../master/1546번.py)
    최고점을 기준으로 성적을 계산해 새로운 평균을 구하는 문제. 반복문으로 시험 점수들을 '점수/최고점*100'으로 계산해 대입해준 후, 새로운 평균을 출력해주면 되는 간단한 문제였다. 
  + #### [BOJ 1157](../master/1157번.py)
    알파벳 대소문자로 된 단어가 주어졌을 때 단어에서 가장 많이 사용된 알파벳이 무엇인지 출력하는 문제. 첫번째 코드는 딕셔너리를 사용해 word 문자열의 각 문자마다 사용 횟수를 세고, 이 딕셔너리를 순회하며 가장 많이 사용된 알파벳을 갱신하는 방식으로 풀었다. 통과는 했지만 단어의 길이가 길어질수록 수행시간이 이와 비례하게 커졌다. 그래서 두번째 코드는 알파벳 문자열을 이용했다. 알파벳 문자열을 이용해 각 알파벳의 사용 횟수를 count() 메서드로 리스트에 추가해주면 무조건 26번의 반복이면 된다. 그리고 가장 많이 사용한 알파벳의 사용 횟수와 인덱스 변수를 만들어주어 가장 많이 사용된 알파벳이 여러 개일 경우도 확인해줄 수 있었다. 이 코드는 처음 코드보다 수행시간이 크게 단축됐다.

#### 21.7.29
  + #### [BOJ 1789](../master/1789번.py)
    서로 다른 N개의 자연수의 합 S을 알 때, 자연수 N의 최댓값을 구하는 문제. 중복을 허용하지 않으므로 가장 작은 자연수 1부터 1씩 증가한 값을 더한다. 합계가 S보다 커졌을 때 반복을 끝내고 i-2값을 출력해주면 N의 최댓값을 알 수 있다. 합계가 동일할 경우도 주의해야 하는 문제였다.

#### 21.8.6
  + #### [BOJ 9012](../master/9012번.py)
    입력받은 괄호문자열이 VPS인지 판단하는 문제. 스택(Stack)을 이용해서 풀었다. 각 괄호 문자열에서 for문으로 문자를 하나씩 검사한다. 왼쪽 괄호이면 스택에 push하고, 오른쪽 괄호는 pop을 수행해 짝을 맞춘다. 문자가 오른쪽 괄호인데 스택이 비어있는 상태이면 VPS가 아닌 문자열이므로 스택에 문자를 추가한 후 반복을 종료한다. 반복을 끝내고 stack이 empty 상태면 VPS, 아니면 VPS가 아닌 문자열이다.

#### 22.3.8
  + #### [프로그래머스 완주하지 못한 선수](../master/완주하지못한선수.py)
    마라톤에 참여한 선수들의 이름이 담긴 배열과 완주한 선수들의 이름이 담긴 배열이 주어질 때, 완주하지 못한 선수의 이름을 return하는 문제. 동명이인을 고려하려면 딕셔너리 자료형을 사용해야 한다. 선수의 이름을 key 값으로 하고, 해당 선수의 value 값을 1씩 증가시켰다. 선수가 완주를 했을 경우에 1을 감소시키면 value 값이 0이 아닌 선수가 완주하지 못한 선수이다.
    + 다른 사람의 풀이를 참고하여 collections 모듈의 Counter() 함수를 알게 되었다. Counter() 함수는 데이터 값의 개수가 딕셔너리 형태로 반환되고, Counter 객체 간 산술연산도 가능하여 훨씬 간결한 코드 작성이 가능했다.
    ```python
        from collections import Counter

        def solution(participant, completion):
            answer = Counter(participant) - Counter(completion)
            return list(answer.keys())[0]
    ```

#### 22.3.9
  + #### [프로그래머스 전화번호 목록](../master/전화번호목록.py)
    전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하는 문제. 처음엔 이중 for문 사용해 모든 전화번호를 비교했더니 시간복잡도가 O(n^2)가 되어 코드의 효율성이 너무 떨어졌다. 리스트 정렬을 이용하면 근접한 문자열만 검사해주면 되기 때문에 시간복잡도가 O(nlogn)로 줄어들어 성공했다. 하지만 해시 사용을 요구하는 문제이기에 딕셔너리 자료형을 사용해 다시 풀었다. 딕셔너리 자료형은 탐색의 시간 복잡도가 O(1)이고, 이중 for문을 사용해도 전화번호의 길이가 20자 제한이므로 시간복잡도는 O(n)가 된다.

#### 22.3.11
  + #### [프로그래머스 기능개발](../master/기능개발.py)
    먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return하는 문제. FIFO 방식으로 배포가 이루어지므로 deque를 사용했다. for문을 한 번 돌면 하루의 작업에 대한 진도가 deque에 새로 업데이트된다. 첫번째 작업이 100%를 넘을 경우, 진도가 100%인 기능들을 모두 queue에서 제거한 후 완료된 기능의 수를 answer 리스트에 추가한다.

#### 22.3.23
  + #### [프로그래머스 프린터](../master/프린터.py)
    중요도가 높은 문서를 먼저 인쇄하는 프린터에서 내가 요청한 문서의 인쇄 순서를 리턴하는 문제. deq의 가장 중요도가 높은 문서의 value와 첫번째 문서의 value 비교, 첫번째 문서가 가장 중요도가 높을 때 인쇄(cnt값 1 증가) 이 때, 인쇄되는 문서의 index와 location이 동일하면 요청한 문서가 인쇄되는 것이므로 반복을 종료하고 cnt 값을 리턴한다.
    + enumerate 함수를 사용하면 index와 원소를 튜플 형태로 저장하여 파이썬다운 for문을 작성할 수 있다.

#### 22.6.6
  + #### [BOJ 2292](../master/2292번.py)
    육각형의 벌집에서 입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력하는 문제. 벌집이 육각형이므로 한 바퀴의 범위가 6의 배수로 증가한다. n이 end보다 적거나 같으면 해당 범위에 n이 있으므로 room을 출력한다.

#### 22.6.7
  + #### [BOJ 2751](../master/2751번.py)
    N개의 수를 오름차순으로 정렬하는 문제. 범위가 1 ≤ N ≤ 1,000,000이므로 시간복잡도가 중요했다. 파이썬의 기본정렬함수의 시간복잡도가 O(nlogn)이므로 sorted 함수를 사용해도 되지만, 동일하게 시간복잡도가 O(nlogn)인 merge sort 방식을 구현해서 풀어봤다. 입출력 시간을 줄이기 위해 realine 함수를 사용했고, 문자열 변수를 만들어서 출력했다.
    + divide & conquer 방식은 문제를 즉각 해결할 수 있을 때까지 재귀적으로 분할하고, 그 분할된 결과를 이용해 해결하며 다시 위로 거슬러 올라가는 방식

#### 22.6.8
  + #### [BOJ 10250](../master/10250번.py)
    호텔 손님을 순서대로 빈 방에 배정하는 문제. 방 배정의 규칙성을 찾아보면 층 수는 n%h이고, 호 수는 n//h+1이 된다. n이 h의 배수일 경우를 따로 고려해서 코드를 작성했다.
  + #### [BOJ 7568](../master/7568번.py)
    사람의 덩치를 키와 몸무게의 값을 입력받아 덩치의 등수를 매기는 문제. N의 범위가 2 ≤ N ≤ 50로 좁은 범위이므로 n명의 키와 몸무게를 모두 비교하는 브루트포스 알고리즘을 적용해서 풀었다.
  + #### [BOJ 1181](../master/1181번.py)
    N개의 알파벳 단어를 길이가 짧은 것부터, 길이가 같으면 사전순으로 정렬하는 문제. list를 set 형변환으로 중복을 제거한다. 정렬의 순서가 중요하여 sort() 메소드로 사전순 정렬을 한 후, 인자로 key=len 값을 넣어 길이순으로 정렬한다. 출력할 때 반복문을 사용하지 않고, join 함수를 사용하면 list를 문자열로 변환할 수 있다.

#### 22.6.9
  + #### [BOJ 1003](../master/1003번.py)
    fibonacci(n)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 문제. 피보나치 수열은 대표적인 다이나믹 프로그래밍 문제이다. 0과 1의 호출횟수는 zero[i의 호출횟수] = zero[i-1의 호출 횟수] + zero[i-2의 호출 횟수]으로 피보나치 수열의 점화식과 동일하다.
  + #### [BOJ 9095](../master/9095번.py)
    정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 문제. 방법의 수를 나열해보니 n의 방법의 수는 n-1~n-3의 방법의 수를 모두 더한 것과 같다. 그로써 dp[i] = dp[i-1] + dp[i-2] + dp[i-3]의 점화식이 도출되었다. 재귀호출을 사용하는 Top-Down 방식을 사용해서 풀었다.
  + #### [BOJ 11726](../master/11726번.py)
    2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 문제. 재귀호출 방식으로 풀었지만 시간초과로 실패하여 dp를 n+1만큼 초기화한 후 작은 문제로 큰 문제의 답을 구하는 Bottom-Up 방식으로 다시 풀었다.

#### 22.6.10
  + #### [BOJ 11047](../master/11047번.py)
    k원을 만드는데 필요한 동전 개수의 최솟값을 출력하는 문제. Ai는 A(i-1)의 배수라는 조건때문에 그리디 알고리즘을 사용해 동전 개수의 최솟값을 구할 수 있다. 역순으로 반복하면서 큰 단위의 동전부터 계산한다. 

#### 22.6.11
  + #### [BOJ 2178](../master/2178번.py)
    NxM 크기의 미로에서 지나야 하는 최단 경로를 구하는 문제. 입력 값이 붙어서 입력되므로 list 함수를 이용해 문자열을 문자 단위로 나눠 2차원 리스트에 저장한다. 또한, 주변의 인접한 칸을 탐색해야 하므로 너비 우선 탐색(BFS)을 이용해서 풀었다. queue에 시작점을 삽입하고, 현재 위치에서 4가지 방향으로 탐색을 한다. x, y가 n, m의 범위 안이면서 이동이 가능한 칸일 경우에 queue에 해당 위치의 좌표를 추가하고, 현재 위치의 value에 1을 더한다. 이렇게 queue가 빌 때까지 반복하면 n-1,m-1의 위치의 value가 최단 거리 칸 수가 된다.

  + #### [BOJ 2667 BFS](../master/2667번_BFS.py)
    NxN 지도에서 각 단지를 정의하고, 총 단지 수와 각 단지내 집의 수를 출력하는 문제. 우선 시작점을 찾기 위해 중첩 for문을 사용하여 bfs에 시작점의 좌표를 인자로 전달한다. 방문한 노드를 다시 방문하지 않도록 0으로 변경해주고, 4방향을 검사하면서 연결된 노드가 있는 경우 해당 노드를 queue에 추가한다. 한 번 탐색을 할 때마다 cnt는 한 단지의 집의 수가 되어, count 배열에 추가해준다.

#### 22.6.12
  + #### [BOJ 2667 DFS](../master/2667번_DFS.py)
    2667번을 재귀를 이용해 DFS 방식으로도 풀었다. BFS 구현과 거의 유사하지만 재귀로 호출이 이루어지기 때문에 cnt 변수를 전역변수를 사용했다. 한 단지가 탐색될 때 True가 반환되고 이 때의 cnt 값을 cout 배열에 추가한 후 cnt를 0으로 초기화한다. BFS 방식보다 DFS 방식을 이용했을 때 더 빠른 탐색이 가능했다.

  + #### [BOJ 10845](../master/10845번.py)
    정수를 저장하는 큐(Queue)을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하는 문제. 1 ≤ N ≤ 10,000이므로 input()을 사용하면 시간초과로 실패하므로 sys.stdin.readline()을 사용해야 시간이 크게 단축된다. 리스트를 사용해 Queue 클래스를 구현했다. 큐는 선입선출 구조이기 때문에 대표적으로 BFS 구현에 사용한다.

#### 22.6.13
  + #### [BOJ 1012](../master/1012번.py)
    서로 인접한 배추들이 퍼져있는 농지에 필요한 최소의 배추흰지렁이 수를 출력하는 문제. 농지를 0으로 초기화한 후, 배추가 있는 좌표를 1로 저장할 때 첫번째 괄호에 y좌표를 넣어야하는데 x좌표를 넣어서 list index out of range 에러가 뜨는 어이없는 실수를 해서 시간을 많이 날렸다. 반복을 하며 dfs 함수를 호출해 서로 인접해있는 배추 군락이 탐색될 때마다 count 값을 1 증가시키면 반복이 끝난 후 count값이 최소로 필요한 배추흰지렁이 수이다. DFS를 재귀로 구현해서 풀었는데, RecursionError로 실패가 떠서 구글링해보니 파이썬의 기본 재귀 깊이 제한이 1000으로 설정되어 있어서 재귀로 DFS를 구현할 땐 재귀 한도 설정을 늘려줘야 한다는 걸 알았다.

#### 22.6.14
  + #### [BOJ 1316](../master/1316번.py)
    단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 문제. 그룹 단어를 판별하는 checker 함수를 만들었다. for문을 돌면서 w[i]가 check 배열에 없는 문자면 배열에 추가하고, 있다면 w[i-1]과 비교해 연속되는 문자일 때 check 배열에 추가했다. 반복이 끝나고 단어와 check 배열이 같으면 그룹 단어이므로 True를 반환하는 방식으로 작성했다. 다른 코드를 참고해보니 문자열 슬라이싱을 이용해 간결하게 푸는 방법도 있었다. 앞으로 문자열을 다루는 문제를 풀 때 문자열 슬라이싱을 잘 활용하는 연습을 해야겠다.

#### 22.6.15
  + #### [BOJ 1541](../master/1541번.py)
    괄호를 적절히 쳐서 식의 값을 최소로 만드는 문제. 식의 값을 최소로 만드는 것의 핵심은 '-'를 기준으로 문자열을 분할하고, '-' 뒤의 식을 괄호로 묶어 더한 후에 크게 만든 숫자를 빼주면 된다. num_list를 순회하면서 문자열에 '+'가 포함된 원소들을 다시 분할한 후 정수로 변환해 더한다. 그 후, 결과 값에 첫번째 원소를 더하고 sum_list 값을 모두 빼면 최솟값이다.

#### 22.6.16
  + #### [BOJ 4673](../master/4673번.py)
    셀프 넘버를 한 줄에 하나씩 출력하는 문제. 지문을 이해하는 게 한참 걸려서 어떻게 풀어야할 지 갈피를 도저히 못잡았다. list보다 set을 사용했을 때 훨씬 편하게 풀 수 있었다. 코드의 핵심은 set 자료형을 사용한 것과 숫자를 문자열로 변환해서 각각의 자릿수를 분리한 것이다. 분리한 자릿수를 더한 num 값을 remove_set에 모두 추가해주고, 차집합을 이용하면 간단하게 연산 결과가 나왔다. 나에게 익숙한 list만 주로 사용했는데 set이나 dictionary의 장단점을 알아두고 잘 이용할 수 있도록 공부해야겠다.

#### 22.6.17
  + #### [BOJ 11021](../master/11021번.py)
    A와 B의 값을 입력받아 합을 출력하는 문제. 문자열 안에 변수 값을 삽입하는 편리한 방법인 문자열 포매팅 중, f-string을 알게 되었다. f-string은 python 3.6 이상의 버전부터 지원하며 3가지의 포매팅 방법 중 가장 속도가 빠르다고 한다.
  + #### [BOJ 1966](../master/1966번.py)
    중요도가 큰 문서부터 인쇄하는 프린터에서 내가 요청한 문서의 인쇄 순서를 출력하는 문제. 풀다보니 이미 풀었던 문제라는 걸 깨달았다. 그럼에도 푸는 시간이 오래 걸린 점 반성해야겠다. enumerate 함수를 사용해 index와 value를 함께 튜플 형태로 저장해주는 것과, max 함수로 value를 비교하려면 value를 0번째 요소로 먼저 넣어야 된다는 것을 기억해야겠다.
  + #### [BOJ 2775](../master/2775번.py)
    "a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다"라는 규칙을 가진 아파트의 k층n호의 거주민 수를 구하는 문제. 2차원 배열을 층 수와 호 수만큼 초기화하고, 0층을 토대로 다음 층의 거주민 수를 구할 수 있기 때문에 먼저 0층의 거주민 수를 대입한다. 표를 그려보면 home[i][j] = home[i - 1][j] + home[i][j-1]의 규칙을 가지기 때문에 차례대로 값을 대입하면 된다. 재귀로도 구현할 수 있지만 파이썬의 경우 시간초과가 발생한다.

#### 22.6.20
  + #### [프로그래머스 숫자 문자열과 영단어](../master/숫자문자열과영단어.py)
    숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어질 때 s가 의미하는 원래 숫자를 return하는 문제. num_list에 각 인덱스에 대응하는 영단어를 넣고 enumerate로 인덱스와 원소를 동시에 접근한다. 0~9까지 반복하면서 replace로 s의 영단어들을 숫자로 치환한다.

#### 22.6.21
  + #### [프로그래머스 문자열 압축](../master/문자열압축.py)
    압축할 문자열 s가 매개변수로 주어질 때, 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 리턴하는 문제. i를 단위로 건너뛰면서 문자열을 슬라이싱한다. 슬라이싱된 두 문자열이 연속될 경우 cnt 값을 1 증가시키고, 연속이 끝나면 w에 압축 문자열을 삽입한다. 반복이 끝나면 마지막 temp 값이 삽입되지 않은 상태이기 때문에 다시 한 번 동일한 if문을 통해 압축 문자열을 완성한다. i개 단위로 쪼개진 압축 문자열의 길이를 각각 len_list에 추가하고 반복이 끝나면 가장 작은 값을 return한다.
  + #### [프로그래머스 체육복](../master/체육복.py)
    여분을 가져온 앞 혹은 뒷번호의 학생에게만 체육복을 빌릴 수 있을 경우, 체육수업을 들을 수 있는 학생의 최댓값을 리턴하는 문제. 여벌 체육복을 가져온 학생이 체육복을 하나만 도난당했을 때 다른 학생에게 빌려줄 수 없다는 조건이 있으므로 서로 중복을 제거한 copy 리스트를 생성한다. 여벌 체육복을 가져온 학생의 리스트를 순회하면서 앞 혹은 뒷번호의 학생이 체육복을 도난당한 학생이라면 빌려줄 수 있으므로 lost_copy에서 제외한다. 반복이 종료되고 전체 학생 수에서 체육복을 빌리지 못한 학생의 수를 제외해서 값을 반환한다. 
    + 제출 후 Test 18, 20이 실패해서 다른 코드를 참고한 결과, 두 리스트를 정렬해야 한다. 예를 들어, n=5, lost=[4,2], reserve=[3,5]의 경우 4번이 3번한테 먼저 빌리면 2번은 빌릴 사람이 없게 된다. 2번이 3번, 4번이 5번에게 빌리는 것이 최적합이다. 문제에서 정렬된 리스트라는 조건이 없었기 때문에 정렬되지 않았을 경우도 고려해야 한다.
  + #### [프로그래머스 조이스틱](../master/조이스틱.py)
    만들고자 하는 이름이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 반환하는 문제. 알파벳을 바꾸는 상하조작과 커서를 이동하는 좌우조작을 분리해 계산한다. 알파벳 조작 횟수는 아스키코드를 이용해 ord(name[i])-ord("A")와 ord("Z")-ord(name[i])+1 중 최소값을 answer에 더한다. 커서 이동의 경우의 수를 구하는 게 너무 어려웠던 문제였다. 커서 이동에서 핵심은 연속된 "A"의 개수만큼은 커서를 이동할 필요가 없다는 점이다. 우선 move 변수에 오른쪽으로만 이동할 때의 조작 횟수를 저장한다. 그 후 반복을 돌면서 다음 index 위치에 'A'가 있을 경우 'A'의 연속이 끝나는 위치의 index를 저장한다. move 변수에 기존 값, 오른쪽으로 가다가 왼쪽으로 꺾어서 가는 경우, 왼쪽으로 가다가 오른쪽으로 꺾어서 가는 경우 중 최소값을 저장하고 answer에 더해 return한다.
    + 이번엔 제출 했을 때 Test 16, 17에서 실패했다. 'A'로만 구성된 경우엔 0을 반환해야하는데 구현한 코드로는 -1이 반환돼서 실패했던 것이었다. 첫 줄에 set 자료형을 이용해 중복을 제거했을 때 'A'만 포함하면 0을 반환해서 해결했다.

#### 22.6.22
  + #### [프로그래머스 큰 수 만들기](../master/큰수만들기.py)
    문자열에서 k개의 문자를 제거했을 때 얻을 수 있는 가장 큰 수를 만드는 문제. 앞에서부터 제거해야 해서 전체에서 작은 수를 삭제하는 방법은 불가능했다. 문자열 슬라이싱을 이용해서 풀어보려 했지만 2시간을 고민해 봐도 test 3번을 도저히 해결할 수 없었다. 다른 코드를 참고한 결과 스택을 이용하는 방법이 있었다. 가장 큰 수를 만들려면 앞자리가 큰 수여야 한다. 즉, stack의 마지막 값과 비교했을 때 num보다 작다면 pop을 반복해 숫자를 제거한다. 이렇게 stack을 이용하면 O(n)의 시간복잡도로 앞에서부터 작은 수를 제거할 수 있다. 그리디 알고리즘은 당장 눈 앞의 최적해를 구하는 방법을 생각하는게 너무 어렵다😥
    + 주의할 점은 k가 0이 되기 전에 stack에 이미 가장 큰 수가 만들어졌을 수 있다. 그러면 stack에 필요 없는 수가 쌓이고 반복이 종료되므로 뒤에서 숫자 k개를 제거해야 한다.
  + #### [프로그래머스 모의고사](../master/모의고사.py)
    수포자 1,2,3이 일정한 패턴으로 답을 찍는다고 할 때 가장 많은 문제를 맞힌 사람이 누군지 배열에 담아 반환하는 문제. 각자 찍는 패턴을 변수에 저장하고 [i % 패턴의 길이]로 인덱스를 지정하면 answer의 값을 모두 비교할 수 있다. 비교가 끝나고 1~3번의 정답 개수가 answer의 최댓값과 같거나 크면 high_score에 index+1를 추가한다.

#### 22.6.23
  + #### [프로그래머스 소수 찾기](../master/소수찾기.py)
    각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 계산하는 문제. 종이 조각은 0~9까지 숫자만으로 이루어져 있다. numbers로 조합할 수 있는 모든 경우의 수는 permutations 함수로 순열을 사용해 구한다. 그 후, set을 이용해 중복을 제거하고 정렬한다. 소수 판별은 에라토스테네스의 체를 이용해 소수 리스트를 만들고 per_list와 일치하면 answer에 추가하는 방법을 사용했다. 통과하긴 했지만 에라토스테네스의 체를 이용했을 때 과하게 큰 소수 리스트를 만들고, 그 리스트의 길이만큼을 모두 돌면서 소수를 탐색하느라 시간이 오래 걸리는 것 같다. per_list에 대해서만 소수를 판별하는 것이 훨씬 빨랐다.
  + #### [프로그래머스 카펫](../master/카펫.py)
    중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 반환하는 문제. w와 h는 카펫의 넓이인 area의 약수 쌍이다. 두 매개변수의 수가 크기 때문에 조건을 잘 설정해서 시간을 줄여야 한다. 다음 3가지 조건을 만족하는 약수 쌍이 답이다.
    1. yellow가 1일 때 answer=[3,3]이므로 길이가 최소 3 이상이어야 하고, 제곱근까지의 약수만 구하면 그 짝이 되는 약수는 자동으로 구할 수 있다.
    2. 약수 쌍 중에서 w >= h를 만족해야 한다.
    3. 갈색이 노란색의 테두리이므로 [w-2,h-2]==[yellow_w, yelow_h]인 점을 이용해 (w-2)*(h-2)==yellow여야 한다.
  + #### [프로그래머스 위장](../master/위장.py)
    스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 종류가 서로 다른 옷의 조합의 수를 계산하는 문제. 옷 조합의 개수가 필요한 것이므로 이름은 필요가 없다. 딕셔너리 자료형을 이용해 옷의 종류별 개수를 저장한다. 같은 종류의 옷은 0~1개만 입을 수 있고 각 종류별로 조합 할 수 있는 개수를 구해야 하기 때문에 머리 아플 정도로 고민했다. 그런데, 곱의 법칙을 이용해 풀면 아주 간단하게 구할 수 있는 문제였다. 수학적 지식을 잘 활용하면 간결하게 풀리는 문제들이 많아서 머리가 나쁘면 몸이 고생한다는 말이 떠올랐다. 자주 사용되는 수학 개념들은 공부할 필요가 있을 것 같다.

#### 22.6.24
  + #### [프로그래머스 신고 결과 받기](../master/신고결과받기.py)
    이용자의 ID가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return하는 문제. 우선 여러명을 신고할 수는 있지만, 동일한 유저에 대해선 신고가 1회밖에 안되기 떄문에 set을 이용해 중복을 제거한다. 유저별로 몇 번 신고됐는지를 계산하기 위해 dictionary를 만든다. report의 요소는 공백을 기준으로 신고한 유저 id와 신고된 유저 id가 있으므로 split()으로 분리하여 신고된 횟수를 계산할 수 있다. 여기까진 풀었는데 해당 유저를 신고한 유저에게만 메일 발송 횟수를 증가하는 방법이 어려웠다. report를 이용해 유저별 신고한 유저id도 딕셔너리로 만들고 메일 발송 횟수를 따져보려고 했지만 report의 길이가 상당히 크기 때문에 시간초과가 떴다. 정답 코드를 참고해보니 'id_list의 index == answer의 index'이므로 신고한 유저 id로 index() 함수를 사용해 answer의 index를 지정하는 방법을 쓰면 빠른 속도로 계산할 수 있었다.
  + #### [프로그래머스 K번째 수](../master/k번째수.py)
    2차원 배열 commands의 모든 원소에 대해 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬한 뒤 k번째에 있는 수를 구하는 문제. commands의 원소인 1차원 배열의 각 요소들을 i,j,k로 지정하고 문자열 슬라이싱과 sort() 함수를 이용하면 되는 간단한 문제였다.
  + #### [프로그래머스 신규 아이디 추천](../master/신규아이디추천.py)
    유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 7단계의 순차적인 처리과정을 통해 규칙에 맞는 새로운 아이디를 추천하는 문제. 문자열 함수를 다양하게 활용하고, 정규표현식을 이용해서 풀었다. re 모듈의 sub(정규 표현식,치환할 문자,대상 문자열）함수가 유용했고 패턴 문자를 잘 알아둬야겠다.
  + #### [프로그래머스 다리를 지나는 트럭](../master/다리를지나는트럭.py)
    다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어질 때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 계산하는 문제. 트럭은 순서대로 다리를 지나가야 하고 1초에 1만큼 이동한다. 큐를 어떻게 활용해야 하는지 감이 안잡혔는데, 큐를 아예 다리라고 생각하고 접근해야 했다. now_weight과 다음 대기 트럭의 합이 weight보다 작으면 대기 리스트에서 pop하고 큐의 맨 뒤에 push되고, 트럭이 큐의 맨 앞에 위치하면 다리를 다 건너간 것이다.

#### 22.6.25
  + #### [프로그래머스 가장 큰 수](../master/가장큰수.py)
    0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 반환하는 문제. 맨 앞의 자리수가 3으로 동일한 3과 30의 경우를 생각해봐야 한다. 3을 붙이는 경우엔 뒤에 다음으로 큰 수를 붙일 수 있지만 30은 다음 자릿수가 무조건 0이 된다. 그렇기 때문에 맨 앞의 자릿수를 기준으로 정렬하고, 동일할 경우엔 다음 자릿수를 기준으로 정렬하는 식이어야 한다. int를 자릿수마다 계산하려면 코드가 복잡해지는데 문자열 비교는 ASCII 값으로 치환해 정렬되어 첫번째 인덱스 값으로 비교한다. numbers를 문자열로 변환하고, 람다식으로 동일한 수로 자릿수를 3자리 이상으로 만들어 그걸 key 값으로 정렬한다. 하지만 오름차순으로 정렬되기 때문에 역순으로 뒤집어 문자열로 변환해주면 가장 큰 수를 만들 수 있다.
    + Test 11이 실패한 이유가 [0,0,0]같은 경우에 문자열로 반환하면 "000"이 반환되기 때문이었다. set으로 중복을 제거하고 0으로만 구성되면 "0"을 바로 반환했다. 대부분 0이 인자로 들어오거나, 0으로만 이루어졌을 때 잘못된 값이 출력되는 경우가 많아 이에 대한 결과를 생각하고 미리 처리하는 습관을 들여야겠다.
  + #### [프로그래머스 H-Index](../master/H_index.py)
    어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index이다. 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때 이 과학자의 H-Index를 반환하는 문제. 논문 인용 횟수를 내림차순으로 정렬하고 인용 횟수가 배열의 인덱스(h)보다 작아지기 시작할 때의 인덱스가 H-Index이다. 인용 횟수가 배열의 인덱스보다 작다면 h개의 논문이 h번 이하로 인용된 것이기 때문이다.
  + #### [프로그래머스 키패드 누르기](../master/키패드누르기.py)
    순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 주어진 규칙에 따라 각 번호를 누른 엄지손가락의 방향을 연속된 문자열 형태로 반환하는 문제. 중앙의 번호는 더 가까운 위치에 있는 손가락으로 누르는 것이므로 이동거리를 구하기 위해선 좌표 값이 필요하다. 즉, 각 번호의 좌표를 딕셔너리 형태로 저장하는 것이 핵심이다. 그 외엔 차근차근 규칙에 따라 구현하면 되서 쉽긴 했지만 이동거리가 -가 되는 경우를 따져서 삼항연산을 일일히 작성했다. 통과한 후에 다른 코드를 참고하니 절대값을 구하는 abs 함수가 있었다...ㅎㅎ
  + #### [프로그래머스 크레인 인형뽑기 게임](../master/크레인인형뽑기게임.py)
    게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때, 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 구하는 문제.  바구니는 인형이 밑에서부터 쌓이는 형태고 동일한 인형이 연속으로 들어갈 때 바구니에서 사라지는 구조이므로 스택으로 구현했다. board에 인형이 존재하면 해당 인형의 번호를 바구니에 넣고, board에선 꺼낸 것이므로 0으로 초기화한다. 바구니에서 인형 2개의 번호가 연속되면 2개를 꺼내고 answer에 2를 추가하는 걸 반복한다.