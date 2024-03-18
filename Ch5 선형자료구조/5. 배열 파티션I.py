### 배열 파티션I ### 
# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 구하여라

# ex)
# 입력:
# [1,4,3,2]
# 출력:
# 4

### 풀이1 : 오름차순 풀이(332밀리초)
# 가장 큰 것끼리 묶어서 페어를 만들어 min을 냈을 때 결과가 최대가 되는데 이는 결국 오름차순으로
# 2개씩 묶는 것과 동일한 결과를 가져온다


def arrayPairSum(self,nums): #nums 는 숫자를 담은 리스트
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min[pair]
            pair = []
    return sum

### 풀이2 : 짝수 번째 값 계산 (관찰성 wow)(308밀리초)
# 위의 풀이과정에서 볼 수 있듯이 sort로 정렬하게 되면 결국 pair의 작은 값은 항상 짝수번째 인덱스(0,2,4,...)에 위치하게 된다.
def arrayPairSum(self,nums): #nums는 숫자를 담은 리스트
    sum = 0
    nums.sort()

    for i,n in enumerate(nums):
        if i%2==0:
            sum += n

    return sum

### 풀이 3 : 파이썬다운 방식 (284밀리초)
# 슬라이싱 활용
def arrayPairSum(self,nums):
    return sum(sorted(nums)[::2])