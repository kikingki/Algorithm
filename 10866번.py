import sys
input = sys.stdin.readline
# 이 문제는 직접 deque을 구현했지만, 파이썬에서 제공하는 collections 패키지에 deque 모듈이 있다고 함
# insert() 메서드는 모든 요소가 메모리에서 이동될 수 있으므로 비효율적 - O(N)
class Deque(object):
    def __init__(self):
        self.items = []

    def push_front(self, item):
        self.items.insert(0, item)

    def push_back(self, item):
        self.items.append(item)

    def pop_front(self):
        if self.size() == 0:
            return -1
        return self.items.pop(0)

    def pop_back(self):
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

    def front(self):
        if self.size() == 0:
            return -1
        return self.items[0]

    # 리스트의 마지막 원소를 찾을 때 list[-1]을 쓰는게 제일 짧고 파이썬스럽다.
    def back(self):
        if self.size() == 0:
            return -1
        return self.items[-1]

m = int(input())
deque = Deque()
for _ in range(m):
    command = input().split()
    if command[0] == 'push_front':
        deque.push_front(int(command[1]))
    elif command[0] == 'push_back':
        deque.push_back(int(command[1]))
    elif command[0] == 'pop_front':
        print(deque.pop_front())
    elif command[0] == 'pop_back':
        print(deque.pop_back())
    elif command[0] == 'size':
        print(deque.size())
    elif command[0] == 'empty':
        print(deque.empty())
    elif command[0] == 'front':
        print(deque.front())
    elif command[0] == 'back':
        print(deque.back())
