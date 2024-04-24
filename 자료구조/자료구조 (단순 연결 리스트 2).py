## 함수 선언부
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):
    global memory, head, pre, current
    # Case 1 : 하필 머리 앞에 삽입하기 (다현, 화사)
    if(findData == head.data):
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node) # 안 중요! (생략 가능)
        return
    # Case 2 : 중간 노드 앞에 삽입(사나, 솔라)
    current = head
    while (current.link != None):
        pre = current
        current = current.link
        if (current.data == findData):
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node) # 안 중요! (생략 가능)
            return
    # Case 3 : 없는 노드 앞에 삽입 (재남, 문별) == 마지막에 추가
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node) # 안 중요! (생략 가능)
    return

def deleteNode(deleteData):
    global memory, head, pre, current
    # Case 1 : 하필 머리를 삭제(다현)
    if (deleteData == head.data):
        current = head
        head = head.link
        del(current)
        return
    # Case 2 : 중간 노드를 삭제(쯔위)
    current = head
    while (current.link != None):
        pre = current
        current = current.link
        if (deleteData == current.data):
            pre.link = current.link
            del(current)
            return
    # Case 3 : 없는 노드를 삭제(채남)
    return

def findNode(findData):
    global memory, head, pre, current
    current = head
    if (findData == current) :
        return current
    while (current.link != None):
        current =current.link
        if (findData == current.data):
            return current
    return Node()

## 변수 선언부
memory = [] # 안 중요!
head , pre, current = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효'] # 여러분 데이터!



## 메인 선언부
node = Node()
node.data = dataArray[0]
head = node
memory.append(node) # 안 중요! (생략 가능)

for data in dataArray[1:]: #  ['정연', '쯔위', ...]
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node) # 안 중요! (생략 가능)

    
printNodes(head)

'''
insertNode('다현','화사')
printNodes(head)
insertNode('사나','솔라')
printNodes(head)
insertNode('재남','문별')
printNodes(head)

deleteNode('다현')
printNodes(head)
deleteNode('쯔위')
printNodes(head)
deleteNode('재남')
printNodes(head)
'''

retNode = findNode('사나')
print(retNode.data, '의 뮤비가 플레이 됩니다~~~')
