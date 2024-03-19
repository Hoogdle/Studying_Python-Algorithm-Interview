### 그룹 애너그램 ###

# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

# 입력:
# ["eat","tea","tan","ate","nat","bat"]

# 출력:
# [
#     ["ate","eat","tea"],
#     ["nat","tan"]
#     ["bat"]
# ]

###################

# cf) sorted 함수
# sorted(정렬할 데이터(반복 가능한 데이터), key 파라미터,reverse 파라미터)
# key : 어떤 것을 기준으로 정렬할 것인가?
# reverse = False : 오름차순, reverse = True : 내림차순
# sort vs sorted
# list.sort() 본체의 리스트를 정렬해서 변환
# sorted(list) 본체의 리스트를 버리고, 정렬한 새로운 리스트
# ex) 
# s = 'apple'
# print(sorted(s)) #['a', 'e', 'l', 'p', 'p']

### 교재풀이

def groupAnagrams(self,strs:List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list) # 없으면 새로운 key 생성 해줌

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values()) 
    

### 추가 내용 
# sorted
a = [2,5,1,9,7]
print(sorted(a)) #[1, 2, 5, 7, 9]

b = 'zbdaf'
print(sorted(b)) #['a', 'b', 'd', 'f', 'z']

c = ['ccc','aaaa','d','bb']
print(sorted(c,key=len)) #['d', 'bb', 'ccc', 'aaaa'] #길이를 기준으로 정렬 (key가 기준)

# 심화
a = ['cde','cfc','abc']
def fn(s):
    return s[0],s[-1]
print(sorted(a,key=fn)) #['abc', 'cfc', 'cde'] #기준이 처음 인덱스와 마지막 인덱스 이므로 cfc가 cde보다 먼저 정렬됨.

