## 함수

def countDown(n):
    if n == 0 :
        print('발사!!')
    else:
        print(n)
        countDown(n-1)



## 메인
print(countDown(5))
