length, index = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
print(li[index-1])