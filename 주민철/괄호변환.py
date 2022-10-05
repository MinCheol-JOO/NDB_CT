def ischeck_balidx(p):
    # 여기에서 인덱스를 반환하는 함수를 만드는 것이 중요하다
    cnt = 0
    for i in range(len(p)):
        if p[i]=='(':
            cnt+=1
        else:
            cnt-=1
        if cnt==0:
            return i
    return False

def ischeck_cor(p):
    cnt =0
    for i in p:
        if i=='(':
            cnt+=1
        else:
            if cnt==0:
                return False
            cnt-=1
    return True

def reverse(p):
    answer = ''
    for i in p:
        if i == '(':
            answer+=')'
        else:
            answer += '('
    return answer

def solution(p):
    answer = ''
    if len(p)==0:
        return p
    idx = ischeck_balidx(p)
    u= p[:idx+1]
    v= p[idx+1:]
    if ischeck_cor(u):
        answer = u+solution(v)
    else:
        answer+='('
        answer+=solution(v)
        answer+=')'
        answer+=reverse(u[1:-1])
    return answer
    
    