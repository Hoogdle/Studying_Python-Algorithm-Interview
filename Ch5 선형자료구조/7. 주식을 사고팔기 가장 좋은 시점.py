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