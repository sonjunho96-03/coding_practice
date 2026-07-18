def solution(t, p):
    answer = 0
    
    length = len(p) # 비교할 문자열 길이
    
    for i in range(len(t) - length + 1): # 비교 가능한 부분 문자열 개수는 전체 길이 - 자를 길이 + 1
        part =  t[i:i + length] # 자른 문자열을 part에 저장
        
        if int(part) <= int(p):
            answer += 1
    
    
    return answer