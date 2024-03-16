### 빗물 트래핑 ###
# 높이(기둥)을 입력 받아 비가 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라

# 입력:
#[0,1,0,2,1,0,1,3,2,1,2,1]
# 출력:
# 6

### 풀이1 : 투 포인터를 최대로 이동, O(n)안에 풀이가능

def trap(self,height): #height는 높이를 저장한 리스트, 함수의 반환값은 정수형
    if not height:
        return 0
    
    volume = 0
    left,right = 0,len(height)-1
    left_max,right_max = height[left],height[right]

    while left!=right:
        left_max,right_max = max(height[left],left_max),max(height[right],right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        elif left_max > right_max:
            volume += right_max - height[right]
            right -= 1

    return volume
            










