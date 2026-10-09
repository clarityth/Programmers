import sys
# 깊은 트리 탐색 시 발생하는 런타임 에러 방지
sys.setrecursionlimit(10**4)

class Node:
    # 트리를 구성할 노드 객체 정의
    def __init__(self, idx, x_val):
        self.idx = idx
        self.x_val = x_val
        self.left = None
        self.right = None

# 부모 노드와 자식 노드의 x값을 비교하여 알맞은 위치에 재귀적으로 삽입
def insert(parent, child):
    if parent.x_val > child.x_val:
        if parent.left == None:
            parent.left = child
        else:
            insert(parent.left, child)
    else:
        if parent.right == None:
            parent.right = child
        else:
            insert(parent.right, child)

def solution(nodeinfo):
    # 정렬 후에도 원래의 노드 번호를 찾기 위한 매핑
    idx_dict = {}
    for i, (x, y) in enumerate(nodeinfo):
        idx_dict[(x, y)] = i + 1
    
    # y축 내림차순(위에서 아래로), x축 오름차순(왼쪽에서 오른쪽으로) 정렬
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    
    # 정렬된 배열의 첫 번째 원소를 루트 노드로 고정
    nodes = Node(idx_dict[(nodeinfo[0][0], nodeinfo[0][1])], nodeinfo[0][0])
    
    # 나머지 노드들을 순서대로 루트 노드에 던져서 이진 탐색 트리 완성
    for i in range(1, len(nodeinfo)):
        insert(nodes, Node(idx_dict[(nodeinfo[i][0], nodeinfo[i][1])], nodeinfo[i][0]))
    
    # 전위 순회: Root -> Left -> Right
    def preorder(node, res):
        res.append(node.idx)
        if node.left != None:
            preorder(node.left, res)
        if node.right != None:
            preorder(node.right, res)
        return res
    
    # 후위 순회: Left -> Right -> Root
    def postorder(node, res):
        if node.left != None:
            postorder(node.left, res)
        if node.right != None:
            postorder(node.right, res)
        res.append(node.idx)
        return res
    
    # 두 순회 결과를 배열에 담아 반환
    return [preorder(nodes, []), postorder(nodes, [])]