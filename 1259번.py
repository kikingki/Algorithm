while(True): 
    num = str(input())
    if num == '0':
        break
    l = len(num)
    answer = 'yes'
    for i in range(0,l//2):
        if num[i] != num[l-i-1]:
            answer = 'no'
    print(answer)


