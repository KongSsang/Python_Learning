def first_process(s):
    chk=0
    for c in s:
        if c=='(': 
            chk+=1
        elif c==')': 
            chk-=1
    if chk == 0:
        return True
    else:
        return False

def second_process(x):
    num_l = x.count('(')
    num_r = x.count(')')
    l = 0
    r = 0

    if x[0] == ')' or x[-1] == '(':
        classi = False
    else:
        if num_l == num_r:
            for i in x:
                if i == '(':
                    l += 1
                else:
                    r += 1
                if l < r:
                    classi = False
                    break
                else:
                    classi = True
        else:
            classi = False
    return classi

def solution(p):
	answer = ''
	u=""
	v=""
	if len(p)==0 or second_process(p): return p

	for i in range(2,len(p)+1,2):
		if first_process(p[0:i]):
			u=p[0:i]
			v=p[i:len(p)]
			break

	if second_process(u):
		answer+=u+solution(v)
	else:
		answer+='('+solution(v)+')'
		for c in u[1:-1]:
			if c=='(': answer+=')'
			else: answer+='('

	return answer

solution("()))((()")