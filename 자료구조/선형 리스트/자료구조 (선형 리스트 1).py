## 함수 선언부



## 전역 변수부
katok = ['다현','정연','쯔위','사나','지효']



## 메인 코드부


## 데이터 추가 (모모에게 1회 카톡)
# 1단계 : 빈칸 추가
katok.append(None)
# 2단계 : 마지막 칸에 새 친구 입력
katok[5] = '모모'
print(katok)


## 데이터 삽입 (미나에게 연속 40회 카톡 == 미나를 3등으로)
# 1단계 : 빈칸 추가
katok.append(None)
# 2단계 : 한칸씩 뒤로 이동(마지막 친구부터...3등까지)
katok[6] = katok[5] # 모모
katok[5] = None
katok[5] = katok[4] # 지효
katok[4] = None
katok[4] = katok[3] # 사나
katok[3] = None
# 3단계 : 3등자리에 미나 입력
katok[3] = '미나'
print(katok)
