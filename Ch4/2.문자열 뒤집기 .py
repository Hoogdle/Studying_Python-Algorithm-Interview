### 문자열 뒤집기 ###

### Q. 문자열을 뒤집는 함수를 작성, 입력값은 문자 배열, 리턴 없이 리스트 내부를 직접 조작

def reverse(self,s) -> None:
    s = s[::-1]

##############
    
# 교재풀이1(투 포인터-Two Pointer)
def reverseString(self,s) -> None:
    left,right = 0,len(s)-1
    while left<right:
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1

##############

# 교재풀이2(파이썬다운 방식)
def reverseString(self,s) -> None:
    s.reverse()

### 파이썬은 객체를 참조하기 때문에 매개변수로 보낸 값도 함수내의 동작의 영향을 받는다!