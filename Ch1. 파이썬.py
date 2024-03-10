### 파이썬 ###

### 네이밍 컨벤션
# 각 단어는 밑줄(_)로 구분한다.
# 일반적으로 모두 소문자로 표기하며 경우에 따라 시작문자를 대문자로 표기
# ex) snake_case = 1


### 리스트 컴프리헨션
# : 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문

# a = []
# for n in range(1,10+1):
#     if n%2 == 1:
#         a.append(n*2)
# [2,6,10,14,18]
        
# =====

# f = [n*2 for n in range(1,10+1) if n%2 == 1] # [2,6,10,14,18]

# 리스트 외에도 딕셔너리,튜플에서도 가능! but 각각의 성질에 유의!

# a = {}
# for key,value in original.items():
#     a[key] = value

# =====

# a = {key:value for key,value in original.items()}



### 제너레이터(Generator)
# 그때 그때 숫자를 생성, 굳이 생성하여 보관하지 않아도 된다
# ex) 숫자 1억개를 만들어내는 프로그램, 1억개를 만든 후 어딘간에 보관하는 것이 아니라 i생성 => i삭제 => i+1 생성 꼴
# yield 구문으로 Generator 리턴, (return 대신 사용된다.), 제너레이터가 여기까지 실행 중이던 값을 내보낸다는 의미.

# def generator():
#     yield 1
#     yield 'string'
#     yield True

# g = generator()

# print(g) #<generator object generator at 0x00000120FD243AC8>
# print(next(g)) #1
# print(next(g)) #string
# print(next(g)) #True


### range
# 제너레이터의 방식으로 활용대는 함수

# print(list(range(5))) #[0, 1, 2, 3, 4]
# print(range(5)) #range(0, 5)
# print(type(range(5))) #<class 'range'>
# for i in range(5):
#     print(i,end=' ') #0 1 2 3 4


### 제너레이터의 효율성

# import sys

# a = [n for n in range(10000)]
# b = range(10000)
# print(len(a)) #10000
# print(len(b)) #10000
# print(sys.getsizeof(a)) #87624
# print(sys.getsizeof(b)) #48


### enumerate
# list,set,tuple과 같은 자료형을 인덱스를 포함한 enumerate 객체로 리턴
# a = [1,2,3,2,45,2,5]
# print(enumerate(a)) #<enumerate object at 0x000002090DBF3318>
# print(list(enumerate(a))) #[(0, 1), (1, 2), (2, 3), (3, 2), (4, 45), (5, 2), (6, 5)]

# 비교 
# for i in range(len(a)):
#     print(i,a[i])
### vs
# i = 0
# for v in a:
#     print(i,v)
#     i += 1
### vs
# for i,v in enumerate(a):
#     print(i,v) #best!


### print
# ,로 구분 (출력시 콤마대신 띄어쓰기(default) 값 구분)
# print('A1','B1') #A1 B1

# 파라미터 sep
# print('A1','B2',sep=',') #A1,B2 (공백대신 ,로 구분)

# 파라미터 end(줄바꿈 제한)
# print('aa',end=' ')
# print('bb') #aa bb

# 리스트 출력, .join
# a = ['A','B']
# print(' '.join(a)) #A B

# format
# idx = 1
# fruit = 'apple'

# print('{0} : {1}'.format(idx+1,fruit)) #2 : apple
# print('{} : {}'.format(idx+1,fruit)) #2 : apple({}의 인덱스 생략 가능)

# f-string (best)
# print(f'{idx+1} : {fruit}') #2 : apple


### pass
# 함수 정의 후 빈칸이면 오류 발생
# pass로 채워주면 해결


### locals
# 로컬에 선언된 모든 변수를 조회할 수 있는 명령, 로컬 스코프에 재한해 정보 조회가능
# cf) pprint로 가독성 좋은 줄바꿈 가능

# import pprint

# a = 10
# def hello():
#     pass
# pprint.pprint(locals())
#  'a': 10,
#  'hello': <function hello at 0x0000018FEB4A4948>,
#  'pprint': <module 'pprint' from 'c:\\Users\\rlaxo\\anaconda3\\envs\\Pytorch\\lib\\pprint.py'>}


