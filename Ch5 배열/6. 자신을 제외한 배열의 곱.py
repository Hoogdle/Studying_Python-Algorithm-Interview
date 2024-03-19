### 자신을 제외한 배열의 곱 ###

# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.

# 입력:
# [1,2,3,4]
# 출력:
# [24,12,8,6]

# 조건:
# 나눗셈을 하지 않고 O(n)에 풀이하라

### 풀이 : 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈

def productExceptSelf(self,nums): #nums는 숫자를 저장한 리스트
    out = []
    p = 1
    # 왼쪽 곱셈을 저장한다.
    for i in range(0,len(nums)):
        out.append(p)
        p *= nums[i]
    p = 1
    # 왼쪽 곱셈 결과 리스트를 기준으로 오른쪽 값들을 하나하나 곱해준다.
    for i in range(len(nums)-1,-1,-1):
        out[i] = out[i] * p
        p = p*nums[i]
    return out
