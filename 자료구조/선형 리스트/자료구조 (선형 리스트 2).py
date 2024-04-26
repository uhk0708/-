## 함수
def add_data(friend):
    # 1단계 : 빈칸 추가
    katok.append(None)
    klen = len(katok) # 선형 리스트의 길이를 파악!
    
    # 2단계 : 마지막 칸에 데이터 입력
    katok[klen-1] = friend

## 변수
katok = []

## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)
