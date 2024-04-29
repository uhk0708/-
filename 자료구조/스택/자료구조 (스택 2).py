## 함수

def isStackFull():
    global SIZE, stack, top
    if (top == SIZE-1):
        return True
    else:
        return False



def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False
        

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('스택 텅~')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('스택 텅~')
        return
    return stack[top]



## 변수
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

## 메인
push('커피')
push('녹차')
'''
push('꿀물')
push('콜라')
push('환타')
'''
print('바닥', stack)

'''
push('게토레이')
print('바닥:', stack)
'''

retData = pop()
print('팝-->', retData)


print('다음 예정==>', peek())

retData = pop()
print('팝-->', retData)


retData = pop()
print('팝-->', retData)
print('바닥', stack)

