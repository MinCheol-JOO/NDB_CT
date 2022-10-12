## 괄호 변환
# 백준 9012번 괄호문자열의 업그레이드 버전.

# 균형잡힌 괄호 확인
def balance_check(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt == 0:
            return i

# 올바른 괄호 확인
def right_check(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            # 올바른 괄호 문자열이 아니면 False
            if cnt == 0:
                return False
            cnt -= 1
    return True

def solution(p):
    
    answer = ''
    
    # 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
    if len(p) == 0:
        return p
    
    # 2. 균형잡힌 괄호 문자열 u,v로 분리
    idx = balance_check(p)
    u = p[:idx+1]
    v = p[idx+1:]
    
    # 3. u가 올바른 괄호 문자열이면 v에 대해 1단계부터 다시 수행
    if right_check(u):
        answer = u + solution(v)
    
    # 4. 3이 아닌 경우
    else:
        answer += '('           # 4-1
        answer += solution(v)   # 4-2
        answer += ')'           # 4-3
        u = list(u[1:-1])       # 4-4
        # 4-5
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
            answer += u[i]

    return answer