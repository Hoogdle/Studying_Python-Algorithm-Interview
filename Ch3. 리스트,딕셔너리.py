### 리스트, 딕셔너리

### 리스트
# 동적 배열로 구현 
# 일체의 다용도 자료형, (스택과 큐 모두 사용가능)
# 다양한 기능을 제공(O(1) 연산도 존재)

# len(a) : 전채 요소의 개수를 리턴 , O(1)
# a[i] : 인덱스 i의 요소를 가져옴, O(1)
# a[i:j] : 인덱스 i부터 j-1까지 k개의 요소를 가져옴, O(k)
# elem in a : elem 요소가 존재하는지 확인, O(n)
# a.count(elem) : elem 요소의 개수를 리턴, O(n)
# a.index(elem) : elem 요소의 인덱스를 리턴, O(n)
# a.append(elem) : 리스트 마지막에 elem 요소를 추가, O(1)
# a.pop() : 리스트 마지막 요소를 추출,스택의 연산, O(1)
# a.pop(0) : 리스트 첫번째 요소를 추출, 큐의 연산, O(n)
# del a[i] : a[i] 삭제, O(n)
# a.sort : O(nlogn)
# min(a),max(a) : O(n)
# a.reverse() : O(n)(입력 순서가 반대로 됨)

# 리스트 삭제 : 인덱스삭제(del a[i]), 요소 삭제(a.remove(elem)), pop삭제

# 파이썬은 모든 것이 객체이기 때문에 리스트 또한 객체를 가리키는 포인터 목록이라 볼 수 있다.
# 참조하는 기능이므로 마치 배열과 연결리스트를 합친 듯한 강력한 기능 제공


### 딕셔너리 
# 키/값 구조
# 내부적으로 해쉬 테이블(Hash Table)로 구현됨.
# 해쉬 테이블은 입력,조회 모두 O(1)에 가능, 다양한 타입의 키 가능

# 딕셔너리의 주요 연산 시간 복잡도
# len(a) : 요소의 개수를 리턴, O(1)
# a[key] : 키를 조회하여 값을 리턴, O(1)
# a[key] = value  키/값을 삽입, O(1)
# key in a : 딕셔너리에 키가 존재하는지 확인, O(1)
# cf) 파이썬 3.7 이상부터 딕셔너리 입력 순서 유지 그 외에는 유지하지 않는다.

# 딕셔너리 활용
# try:
#     print(a['key4'])
# except KeyError:
#     print('존재하지 않은 키')

# for k,v in a.items():
#     print(k,v)
# key1 value1
# key2 value2
# key3 value3

# del a['key1']
# print(a) #{'key2' : 'value2', 'key3' : 'value3'}



### 딕셔너리 모듈

# defaultdict 객체
# 존재하지 않은 키를 조회할 경우, 에러메시지를 출력하는 대신 디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템 생성

# import collections

# a = collections.defaultdict(int)
# a['A'] = 5
# a['B'] = 4
# print(a) #defaultdict(<class 'int'>, {'A': 5, 'B': 4}
# a['C'] += 1
# print(a) #defaultdict(<class 'int'>, {'A': 5, 'B': 4, 'C': 1})


# # counter 객체
# # 아이템에 대한 갯수를 계산해 딕셔너리로 리턴
# a = [1,2,3,4,5,5,5,6,6,]
# b = collections.Counter(a)
# print(b) #Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})

# Counter 객체에서 가장 빈도 수가 높은 요소 추출 : most_common()
# a = [1,2,3,4,5,5,5,6,6,]
# b = collections.Counter(a)
# print(b.most_common(2)) #[(5, 3), (6, 2)] #빈도가 높은 2개의 요소 추출

# OrderedDict 객체
# 파이썬 3.6이하에서 딕셔너리의 입력 순서가 유지되도록 해줌
# 3.7이상에서는 필요 없는 기능
