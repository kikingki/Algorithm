croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']    # 크로아티아 알파벳을 리스트에 저장
word = input()

for i in croa:  # 리스트 순회
    # replace() 메서드로 입력한 단어에 크로아티아 알파벳이 있으면 공백으로 변환
    word = word.replace(i,' ')

print(len(word))


