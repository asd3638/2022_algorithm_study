from collections import deque
n, k = map(int, input().split())
deque = deque()
index = 1
answer = []
deque = [i for i in range(1, n + 1)]
while len(deque):
    if index % k == 0:
        answer.append(deque.popleft())
        index += 1
    else:
        deque.append(deque.popleft())
        index += 1
print("<", ', '.join(str(i) for i in answer), ">", sep="")
