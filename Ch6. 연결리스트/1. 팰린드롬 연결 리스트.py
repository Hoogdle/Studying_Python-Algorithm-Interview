### 팰린드롬 연결 리스트 ###

# 연결리스트가 팰린드롬 구조인지 판별하라

# 입력:
# 1->2
# 출력:
# false

# 입력:
# 1->2->2->1
# 출력:
# true

### 풀이1 : 리스트 변환
def isPalindrome(self,head): #head는 리스트노드
    q = []

    if not head:
        return True
    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q)>1:
        if q.pop() != q.pop(0):
            return False
    return True


### 풀이2 : 데크를 이용한 최적화

# pop은 마지막 인덱스 값을 빼올 때는 간편하지만 pop(0)을 하려면 O(n)의 시간이 들게 된다.
# => 데크는 이중 연결 리스트 구조로 양쪽 방향 모두 값을 추출하는데 O(1)의 시간이 든다.
import collections

def isPalindrome(self,head):
    q = collections.deque()

    if not head:
        return True
    
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q)>1:
        if q.popleft() != q.pop():
            return False
        
    return True

### 풀이3 : 런너를 이용한 풀이
# 런너 : 연결리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법
#        한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용

# fast 러너는 2칸씩, slow 러너는 1칸씩 이동한다. fast 러너가 마지막에 다다르면 slow러너는 중간지점에 다다르게 된다.
# slow 러너는 이동하면서 연결리스트를 역순으로 저장한다.

# 파이썬의 특징 : 모든 것이 객체이다!
# rev = 1, slow = 2->3 #이라고 가정한다면
# rev, rev.next, slow = slow,rev,slow.next
#의 결과는 rev = 2->3 rev.next = 1, slow = 3 이 된다. 즉 대입의 순서가 없고 모두 한번에 갱신된다!

# rev, rev.next = slow,rev
# slow = slow.next
# rev = 2->3 , rev.next = 1
# 여기서 rev.next = 1 이므로 rev = 2->1를 가리키게 된다. rev는 slow와 같은 객체를 가리키므로
# slow 또한 2->1로 변경되게 된다.




def isPalindrome(self,head):
    rev = None
    slow = fast = head
    
    while fast and fast.next: #fast가 None이 될 때까지 계속 보내기!
        fast = fast.next.next
        rev, rev.next, slow = slow,rev,slow.next
    if fast: #fast가 None이면 slow를 그만 보내라
        slow = slow.next

    while rev and rev.val == slow.val:
        slow,rev = slow.next,rev.next
    return not rev # rev이 비어있으면 True 비지 않으면 False