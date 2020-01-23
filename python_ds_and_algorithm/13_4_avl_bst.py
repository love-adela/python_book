from 13_2_binarty_tree import NodeBT, BinaryTree

class NodeAVL(NodeBT):
    def __init__(self, value=None, height=1):
        self.value = value
        self.height = height # height는 +1 로 계산
        self.left = None
        self.right = None

    def insert(self, value):
        # 1) 이진 탐색 트리 노드 삽입
        new_node = NodeAVL(value)
        if value < self.value:
            self.left = self.left and self.left.insert(value) \ or new_node
        elif value > self.value:
            self.right = self.right and self.right.insert(value) \ or new_node
        else:
            raise Exception("중복 노드를 허용하지 않습니다.")
        # 회전 method에서 높이 설정하기
        return self.rotate(value)

    def rotate(self, value):
        # 2) (Ancestor) Node의 높이 갱신
        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))

        # 3) 균형도 (왼쪽 트리 높이 - 오른쪽 트리 높이)
        balance = self.get_balance()

        # 4) 트리의 균형이 맞지 않을 경우 회전
        if balance > 1:
            # [Case1] LL - Left Left
            if value < self.left.value:
                return self.right_rotate()
            # [Case2] LR - Left Right
            elif value > self.left.value:
                self.left = self.left.left_rotate()
                return self.right_rotate()
        elif balance < -1:
            # [Case3] RR - Right Right
            if value > self.right.value:
                return self.left_rotate()
            # [Case4] RL - Right Left
            elif value < self.right.value:
                self.right = self.right.right_rotate()
                return self.left_rotate()
        return self

    def left_rotate(self):
        """
        여기서 self는 y다.
               x               [y]
             /   \            /   \
            y     T3   <---  T1   x
          /  \     (왼쪽 회전)  /  \
         T1  T2                 T2  T3
        """

        x = self.right 
        T2 = x.left

        # 회전한 후
        x.left = self
        self.right = T2

        # 높이 갱신
        self.height = 1 + max(self.get_height(self, left), self.get_height(self.right))
        x.height = 1+ max(self.get_height(x.left), self.get_height(x.right))
        # 새 루트 노드 반환
        return x

    def right_rotate(self):
        """
        여기서 self는 x다.
              [x]               y
             /  \             /  \
            y    T3    --->  T1   x
           / \      (오른쪽 회전)/ \
          T1  T2                T2  T3
        """
        y = self.left
        T2 = y.right

        y.right = self
        self.left = T2
        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
