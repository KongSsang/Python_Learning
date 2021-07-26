a, b = map(int, input().strip().split(' '))
answer = ''
for j in range(b):
    answer += '*'*a
    if j == b-1:
        break
    answer += '\n'
print(answer)