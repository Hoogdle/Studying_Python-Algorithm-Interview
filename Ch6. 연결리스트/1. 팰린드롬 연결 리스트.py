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
        