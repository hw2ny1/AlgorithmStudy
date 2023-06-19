s = list(input())
t = list(input())

result = 0
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        result = 1
        break
print(result)