### 가장 긴 팰린드롬 부분 문자열 ### 

# 가장 긴 팰린드롬 부분 문자열을 출력하라.

# 입력:
# babad
# 출력
# bab (또는 aba)

# 입력:
# cbbd
# 출력
# bb

### 교재풀이

def longestPalindrome(self,s):
    def expand(left,right):
        while left>=0 and right <len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    if len(s)<2 or s==s[::-1]: #슬라이싱은 계산 속도가 매우 빠르다.
        return s
    result = ''
    for i in range(len(s)-1):
        result = max(result,
                        expand(i,i+1),
                        expand(i+i+2),
                        key = len)
    return result


### cf) 유니코드와 UTF-8
# 기존의 사용하던 아스키 코드에서는 한글이 깨짐 => 유니코드
# 영문자는 1바이트 만으로도 표현 가능 => 한 문자당 2바이트를 차지하는 유니코드는 비효율적... => UTF-8
# UTF-8은 가변적인 유니코드!
# 시작비트로 문자의 전체 바이트를 결정!
# ex)
# 앞자리 0 => 1바이트
# 앞자리 10 => 특정 문자의 중간 바이트
# 앞자리 110 => 2바이트 ...
# 불필요한 낭비를 제거할 수 있다.