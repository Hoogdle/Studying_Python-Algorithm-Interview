### 주식을 사고팔기 가장 좋은 시점 ###

# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.

# 입력:
# [7,1,5,3,6,4]
# 출력:
# 5

# 설명:
# 1일 때 사서 6일 때 파는 것이 가장 큰 이익을 남길 수 있다.

### 풀이1 : 브루트 포스 계산(타임아웃) 
# 반복문 활용에서 배울 점 많음
# max함수를 활용하자!
# 코드가 진짜 아름답다...
def maxProf(self,prices): # prices는 숫자를 담은 리스트
    max_price = 0
    
    for i,price in enumerate(prices):
        for j in range(i,len(prices)):
            max_price = max(max_price - price[j],max_price)
    
    return max_price

### 풀이2 : 지점과 현재 값과의 차이 계산
# 최댓값과 최솟값의 초기값을 지정하는 방법 중 하나로
# 최댓값에는 가장 낮은 값을 초기값으로 => 언제든지 교체될 수 있게
# 최솟값에는 가장 높은 값을 초기값으로 => 언제든지 교체될 수 있게
import sys

def maxProf(self,prices):
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값을 갱신
    for price in prices:
        min_price = min(price,min_price)
        profit = max(profit,price-min_price)

    return profit

### sys 모듈을 활용한 최댓값 최솟값 배치

mx = -sys.maxsize # -무한대
mn = sys.maxsize # +무한대
# 이렇게 설정하면 최댓값 최솟값의 변경이 수월해진다! 
# 임의의 숫자로 최댓값 최솟값을 설정하는 것은 지양하자...