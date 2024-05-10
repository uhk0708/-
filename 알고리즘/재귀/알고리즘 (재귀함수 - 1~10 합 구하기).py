## 함수

def addNumber(num):
    if (num == 1):
        return 1
    return num + addNumber(num-1)



## 변수

print(addNumber(1000))
