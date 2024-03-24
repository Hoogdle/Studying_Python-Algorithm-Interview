### 역순 연결 리스트 ###

# 연결 리스트를 뒤집어라

# 입력:
# 1->2->3->4->5->NULL

# 출력:
# 5->4->3->2->1->NULL

### 풀이1 : 재귀 구조로 뒤집기

def reverseList(self, head): # head는 head노드, 반환 값은 노드의 리스트 
    def reverse(node,prev): #node는 노드의 리스트, prev는 노드의 리스트
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next,node)
    
    return reverse(head)