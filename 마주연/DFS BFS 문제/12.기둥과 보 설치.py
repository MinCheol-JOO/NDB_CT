# x, y, a, b : x좌표, y좌표, 구조물(0: 기둥, 1: 보), 설치 유무(0: 삭제, 1: 설치)
def is_ok(result): # 지금 상태, 괜찮을까?
    for x, y, a in result:
        if a: # 보일 때
            if [x, y - 1, 0] in result or [x + 1, y - 1, 0] in result or ([x - 1, y, 1] in result and [x + 1, y, 1] in result):
                continue
            return False
        else: # 기둥일 때
            if not y or [x, y, 1] in result or [x - 1, y, 1] in result or [x, y - 1, 0] in result:
                continue
            return False
    return True
    
def solution(n, build_frame):
    result = []
    for build in build_frame: # build_frame을 하나씩 살펴보며
        if build[3]: # 설치
            result.append(build[:3]) # x,y,a(구조물) 추가
            if not is_ok(result): # 지금 상태 안 괜찮다면
                result.remove(build[:3]) # 설치한거 다시 삭제
        else: # 삭제
            result.remove(build[:3]) # x,y,a(구조물) 제거
            if not is_ok(result): # 지금 상태 안 괜찮다면
                result.append(build[:3]) # 삭제한거 다시 설치
                
    return sorted(result) # 정렬해서 반환