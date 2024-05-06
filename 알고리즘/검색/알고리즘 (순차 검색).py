## 함수
from random import randint, choice

def seqSearch(ary, fdata):
    pos = -1
    for i in range(len(ary)):
        if (ary[i] == fdata):
            pos = i
            break




    return pos


## 변수
dataAry = [randint(30,190) for _ in range(20)]
findData = choice(dataAry) # 누나 키

## 메인
print('배열-->', dataAry)
position = seqSearch(dataAry, findData)

if (position != -1):
    print(findData,'는 ', position, '위치에 있음.')
else:
    print(findData,'는 없어요 ㅠ')


