### 두 수의 합 ###

# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

# 입력:
# nums = [2,7,11,15], target = 9
# 출력:
# [0,1]

### 풀이1(브루트 포스 계산,O(n^2)), 비효율적 풀이, 5284 밀리초
def twoSum(self, nums,target): #nums는 문자열 배열
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

### 풀이2(in을 이용한 탐색) ,864밀리초
# target - n 이 리스트에 존재하는지 확인!

def twoSum(self, nums,target):
    for i,n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            return [nums.index(n),nums[i+1:].index(complement)+(i+1)]
# in 의 시간 복잡도 == O(n)
# 전체 시간 복잡도 == O(n^2), 하지만 풀이1 보다는 빠름
        

### 풀이3(첫 번째 수를 뺀 결과 키 조회)
# dictionary 기반 풀이라 매우 빠름, 48밀리초
def twoSum(self, nums,target): #nums 는 숫자 저장한 리스트
    nums_map = {}
    for i,num in enumerate(nums):
        nums_map[num] = i
    for i,num in enumerate(nums):
        if target - num in nums and i!=nums_map[target-num]: #찾고자하는 target-num의 index가 num의 인댁스와 같지 않다면
            return[i,nums_map[target-num]] # 각각의 인덱스 리턴
        

### 풀이4(조회 구전 개선,풀이3과 메커니즘은 같음),44밀리초
def twoSum(self,nums,target):
    nums_map = {}
    for i,num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num],i]
        nums_map[num] = i


### 풀이5 : 투 포인터 이용 (nums가 정렬 되어있을 때만 사용 가능)
# 두 합이 같을 때 동안 left -> 으로 , right는 <-로 이동하는 메커니즘

def twoSum(self,nums,target):
    left,right = 0, len(nums)-1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left,right]
        
