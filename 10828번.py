# 입력이 많기 때문에 readline() 메서드 사용
import sys
input = sys.stdin.readline

# 클래스로 스택 구현
class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return -1
        return self.items.pop()

    def size(self):
        return len(self.items)

    # bool() 메서드는 None, 숫자 0, 비어있는 리스트 등의 경우에 False로 판단
    def empty(self):
        if bool(self.items):
            return 0
        return 1

    def top(self):
        if self.size() == 0:
            return -1
        return self.items[-1]


m = int(input())
stack = Stack()

for _ in range(m):
    command = input().split()
    if 'push' in command:
        stack.push(int(command[1]))
    elif 'pop' in command:
        print(stack.pop())
    elif 'size' in command:
        print(stack.size())
    elif 'empty' in command:
        print(stack.empty())
    elif 'top' in command:
        print(stack.top())