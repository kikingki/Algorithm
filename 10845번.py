import sys
input = sys.stdin.readline

# 클래스로 큐 구현
class Queue(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return -1
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    # bool() 메서드는 None, 숫자 0, 비어있는 리스트 등의 경우에 False로 판단
    def empty(self):
        if bool(self.items):
            return 0
        return 1

    def front(self):
        if self.size() == 0:
            return -1
        return self.items[0]

    def back(self):
        if self.size() == 0:
            return -1
        return self.items[-1]

n = int(input())
queue = Queue()

for _ in range(n):
    command = input().split()
    if 'push' in command:
        queue.push(int(command[1]))
    elif 'pop' in command:
        print(queue.pop())
    elif 'size' in command:
        print(queue.size())
    elif 'empty' in command:
        print(queue.empty())
    elif 'front' in command:
        print(queue.front())
    elif 'back' in command:
        print(queue.back())