### 두 정렬 리스트의 병합 ###
# 정렬되어 있는 두 연결 리스트를 합쳐라

# 입력: 
# 1->2->4, 1->3->4

# 출력:
# 1->1->2->3->4->4

### 재귀 구조로 연결

# cf)
# 파이썬은 모든 것이 객체이기 때문에 다중할당이 한 번에 가능하다!
# a,b= b,a 
# a가 b가 가리키는 주소를 가리키도록
# b가 a가 가리키는 주소를 가리키도록
# 한번에 변경!

def mergeTwoLists(self, l1,l2): #l1과 l2는 연결리스트 이 함수의 반환 값은 연결리스트
    if (not l1) or (l2 and l1.val > l2.val):
        l1,l2= l2,l1
    if l1:
        l1.next = self.margeTwoLists(l1.next,l2)
    return l1

# 직접 그리며 확인하기!

# 파이썬 연산자 우선순위
# ()가 무조건 연산자 제 1순위!
# 함수 호츨이 제 2순위!
# and 연산이 or연산 보다 우선순위!