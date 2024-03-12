### 문자열 조작 ###
# 문자열을 변경하거나 분리하는 등의 여러 과정


# 주어진 문자열이 팰린드롬 인지 확인, 대소문자 구별X, 영문자와 숫자만을 대상으로 함
# 팰린드롬 : 앞뒤가 똑같은 단어 혹은 문장


# 나의 풀이
# s = input()
# s = list(s)


# original = []
# temp = []
# for i in s:
#     if i == ' ':
#         del i
#         continue
#     if not i.isalpha():
#         del i
#         continue
#     if i.isupper():
#         i = i.lower()
#     original.append(i) #원본 필터링 저장
#     temp.append(i) #필터링된 문자열 저장
    
# temp.reverse() #필터링된 문자열 reverse

# print(original)
# print(temp)

# if original == temp:
#     print("true")
# else:
#     print("false")

#################
    
# 교재 풀이1(리스트)

# def isPalindrome(self, s:str) -> bool:
#     strs = []
#     for char in s:
#         if char.isalnum(): #isalnum : 영문자 숫자여부 판별
#             strs.append(char.lower()) #.lower() 소문자로 변환

#     while len(strs)>1:
#         if strs.pop(0) != strs.pop(): #pop(0) 처음 pop() 나중 요소 반환
#             return False
#     return True

#################

# 교재 풀이2(데크)
# import collections

# def isPalindrome(self, s:str) -> bool:
#     # 자료형 데크형으로 선언
#     strs  = collections.deque()

#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
#     while len(strs)>1:
#         if strs.popleft() != strs.pop():
#             return False
        
#     return True
# 리스트 풀이에 비해 5배 정도 빠름
# 리스트의 pop(0)은 O(n), deque의 popleft()는 O(1)
# 이를 각각 n번 반복하면 리스트는 O(n^2) 데크는 O(n) 성능차이!

#################

# 교재 풀이3(슬라이싱)
# 정규표현식 : 특정한 규칙을 가지는 문자열의 집합을 표현하는데 사용
# ex) [0-9],숫자 // [^0-9],비숫자 // [^a-zA-Z0-9], 숫자+문자가 아닌 것

# import re

# def isPalindrome(self, s:str) ->bool: 
#     s = s.lower()
#     # 정규식으로 불필요한 문자 필터링(한 번에 걸러냄)
#     s = re.sub('[^a-z0-9]', '',s) # s에서 매개변수1를 지우고 매개변수2를 추가

#     return s==s[::-1] #슬라이싱

# # 2번 풀이 보다 2배 정도 빠름


### 문자열 슬라이싱
# 내부적으로 매우 빠르게 동작
# 문자열을 조작할 때 항상 슬라이싱을 우선으로 사용
# S[1:4] 1부터 4이전 까지
# S[::1] 전체표현
# S[::-1] 뒤집기
# S[::2] 2칸씩 앞으로 이동

