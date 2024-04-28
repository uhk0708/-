## 함수


## 변수
stack = [None,None,None,None,None]
top = -1


## 메인


# Push
top += 1
stack[top] = '커피'

top += 1
stack[top] = '녹차'

top += 1
stack[top] = '꿀물'

print('바닥:', stack)


# Pop
data = stack[top]
stack[top] = None
top -= 1
print('팝-->',data)

data = stack[top]
stack[top] = None
top -= 1
print('팝-->',data)

data = stack[top]
stack[top] = None
top -= 1
print('팝-->',data)


print('바닥:', stack)
