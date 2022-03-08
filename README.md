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

