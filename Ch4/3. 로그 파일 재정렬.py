### 로그 파일 재정렬 ###
# 로그를 재정렬해라 기준은 다음과 같음
# 1. 로그의 가장 앞 부분은 식별자
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.

# 숫자 로그도 모두 문자로 되어 있다.

# ex)
# 입력 : logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# 출력 : ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

###################

### 교재풀이

# isdigit() : string 클래스의 메서드, 문자열에 단 하나의 문자라도 있다면 False, 모두 숫자이면 True 반환
def reorderLogFiles(self, logs):
    letters, digits = [],[] 
    for log in logs:
        if log.split()[1].isdigit(): #식별자 다음 단어가 숫자인경우 문자인 경우 나누기
            digits.append(log)
        else:
            letters.append(log)
    
    letters.sort(key=lambda x:(x.split()[1:],x.split()[0])) # first key : x.split()[1:] if all same,
    # second key : x.split()[0]
    return letters+digits

#   letters.sort(key=lambda x:(x.split()[1:],x.split()[0])) 의 원래 함수식
# def func(x):
#     return x.split()[1:],x.split()[0]

# s.sort(key=func)
