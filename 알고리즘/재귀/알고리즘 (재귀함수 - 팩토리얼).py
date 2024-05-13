## 함수

def factorial(num):
    if num <= 1:
        print('1 반환')
        return 1
    print(f'{num} * {num-1}! 호출')
    retVal = factorial(num-1)

    print(f'{num} * {num-1} (={retVal})반환')
    return num * retVal
    



## 메인
print(factorial(5))
