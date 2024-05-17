## 함수
from random import randint

def selectSort(ary):
    n = len(ary) # 전체 데이터 개수
    for i in range(0,n-1,1): # 사이클 (큰 회전)
        minIdx = i
        for j in range(i+1,n,1):
            if (ary[minIdx] > ary[j]):
                minIdx = j
        ary[i], ary[minIdx] = ary[minIdx] , ary[i]

    return ary
        


## 변수
dataAry = [randint(30,190) for _ in range(20)]


## 메인
print('정렬 전-->', dataAry)
dataAry = selectSort(dataAry)
print('정렬 후-->', dataAry)
