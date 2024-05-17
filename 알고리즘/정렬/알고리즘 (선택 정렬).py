## 함수
from random import randint

def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if (ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx


## 변수
before = [randint(30,190) for _ in range(8)]
after = []


## 메인
print('정렬 전-->', before)
for i in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])



print('정렬 후-->',after)
