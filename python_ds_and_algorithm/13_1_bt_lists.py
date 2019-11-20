"""
리스트를 사용해서 이진트리 구현하기
리스트 중간에 노드를 삽입하거나 꺼낼 때 제한이 있으므로 매우 비효율적이다.
"""

def BinaryTreeList(r:int)->list:
    return [r, [], []]


def insertLeft(root:list, newBranch:int)->list:
    t = root.pop(1) 
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root:list, newBranch:int)->list:
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root:list)->int:
    return root[0]


def setRootVal(root:list):
    root [0] = newVal


def getLeftChild(root)->list:
    return root[1]


def getRightChild(root:list)->list:
    return root[2]


def main():
    r = BinaryTreeList(3) # [3, [], []]
    print(r)
    print(insertLeft(r, 4))
    print(insertLeft(r, 5))
    print(insertRight(r, 6))
    print(insertRight(r, 7))
    print(getRootVal(r))
    print(getLeftChild(r))
    print(getRightChild(r))

if __name__ == "__main__":
    main()

