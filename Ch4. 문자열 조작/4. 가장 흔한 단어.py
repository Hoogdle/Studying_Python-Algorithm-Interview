### 가장 흔한 단어 ###

# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자를 구분하지 않으며 구두점(마침표,쉼표 등) 또한 무시한다.

# ex)
# 입력:
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]

# 출력:
# "ball"

### 리스트 컴프리헨션, counter 객체 사용
# def mostCommonWord(self,paragraph,banned):
#     words = [word for word in re.sub(r'[^\w]','',paragraph) #^은 not, \w은 단어 문자(word character)를 뜻함
#         .lower().split() 
#             if word not in banned]
#     counts = collections.Counter(words) # counts는 collenction모듈의 Counter클래스 객체 init은 words로
# ex)
# >>> Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
# Counter({'hi': 3, 'hey': 2, 'hello': 1})
    # return counts.most_common(1)[0][0] #collection.Counter.most_common(a) 객체의 최빈값순으로 a개 만큼 반환 (리스트로 둘러싼 튜플 형태 [(,),(,)])

# ### cf
# counts = collections.defaultdict(int) # defaultdict() dict에 만약 key 가 없다면 0으로 초기화하여 생성
# for word in words:
#     counts[word] += 1






    
    

