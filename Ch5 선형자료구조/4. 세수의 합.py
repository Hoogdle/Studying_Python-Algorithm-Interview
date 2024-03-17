### 세수의 합 ###
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라

#입력:
# nums = [-1,0,1,2,-1,-4]
#출력:
# [
#     [-1,0,1],
#     [-1,-1,2]
# ]

### 브루트 포스로 계산

# cf) sort()의 시간 복잡도는 nlogn


def treeSum(self,nums): #nums는 정수의 리스트형, 반환값은 정수형 리스트
    results = []
    nums.sort()
    nums = list(set(nums))

    for i in range(len(nums)-2):
        # 중복된 값 건너뛰기(중복요소가 아닌 것이 아니다. 같은 값을 가지는 인덱스가 참조되면 그 결과는 이미 연산 했기 때문에 pass(중복제거))
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,len(nums)-1):
            if j>i+1 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1,len(nums)):
                if k<j+1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i],nums[j],nums[k]])
    return results



