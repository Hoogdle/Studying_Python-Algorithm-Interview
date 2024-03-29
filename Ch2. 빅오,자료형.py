### 빅오(Big-0)
# : 입력값이 무한대로 향할 때 함수의 상한을 설명하는 수학적 표기법
# 입력값 n 이 무한대로 커질 때 실행 시간의 추이
# 컴퓨터의 연산 속도는 매우 빠르다, 작은 데이터에는 관심 없음, 데이터가 매우 크면 알고리즘의 효율성이 돋보인다.

# 시간 복잡도 : 어떤 알고리즘을 수행하는 데 걸리는 시간을 설명하는 계산 복잡도(계산 복잡도를 표기하는 대표적 방법, 빅오)
# 빅오로 시간복잡도를 표기할 때는 최고차항만을 표기한다
# ex) 4n^2 + 3n + 4 번의 계산 => O(n^2)

# O(1) : 입력값이 아무리 커도 실행 시간은 일정, 최적의 알고리즘 (해시 테이블 조회 및 삽입)
# O(log n): log 특성상 매우 큰 값에도 크게 영향을 바디 않음 (이진검색)
# O(n) : 알고리즘 수행시간은 입력값에 정비례, '선형시간 알고리즘' (정렬되지 않은 리스트에서 최댓값 또는 최솟값을 찾는 경우)
# O(nlogn) : 병합정렬을 비롯한 효율 좋은 알고리즘이 이에 해당. 
# O(n^2) : 버블 정렬 같은 비효율적인 정렬 알고리즘이 해당
# O(2^n) : 피보나치 수를 재귀로 계산하는 알고리즘이 이에 해당 2^n > n^2
# O(n!) : 가장 느린 알고리즘, 입력값이 조금만 커져도 다항 시간 내에는 계산이 어렵다.

# 공간과 시간의 Trade-off : 일반적으로 실행 시간이 빠른 알고리즘은 공간을 많이 사용, 실행 시간이 느린 알고리즘은 공간을 적게 사용

# 빅오 표기법은 주어진(최선/최악/평균) 경우의 수행 시간의 상한을 나타낸다.

# cf) 원시 타입 : 메모리에 정확하게 타입 크기만큼의 공간을 할당, 그 공간을 오로지 값으로 채워 놓음
# C : 원시 타입
# 자바 : 원시 타입,객체
# 파이썬 : 객체
# 원시 객체일 수록 하드웨어에 가까워 더 빠른속도, 객체일수록 느린 속도와 많은 메모리를 차지하지만 다양한 기능 제공

### 객체
# 파이썬은 모든 것이 객체이다. 
# 크게 불변 객체, 가변 객체로 구분할 수 있다.
# 파이선에서 변수를 할당하는 작업은 해당 객체에 대한 참조를 한다는 의미(예외 없음, 문자 숫자 모두 객체)

# a = 10
# b = a
# print(id(10),id(a),id(b)) #140737258566864 140737258566864 140737258566864
# 원시객체라면 가각 다른 메모리 영역에 위치, but 파이썬은 모든 것이 객체, just 객체 참조


### 불변 객체
# bool,int,float,tuple,str
# c = 10
# print(id(c)) #140704430077136
# c += 1
# print(id(c)) #140704430077168
# 10이 11로 변하지 못한다. 다만 c는 10을 참조하는 것이 아닌 11을 참조하게 된다.


### 가변 객체 
# list,set,dict
# a = [1,2,3,4,5]
# b = a
# print(b) #[1, 2, 3, 4, 5]
# a[2] = 4
# print(b) #[1, 2, 4, 4, 5]
# a와 b 모두 같은 객체를 참조하므로 a가 참조하는 리스트의 값을 변경한다면 b에도 영향을 미친다.

# cf) 파이썬의 넘파이는 C로 만든 모듈이므로 속도가 매우 빠르다(파이썬의 리스트보다 40배 정도 빠름)


