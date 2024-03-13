### 가장 흔한 단어 ###

# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자를 구분하지 않으며 구두점(마침표,쉼표 등) 또한 무시한다.

# ex)
# 입력:
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]

# 출력:
# "ball"

### 나의 코드
import re

def commonWord(self,s,ban):
    s = s.lower()
    s = re.sub('[^a-z ]','',s) #단어와 공백만 존재하게

