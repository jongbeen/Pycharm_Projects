class Node:
    def __init__(self,data):
        v, x, y = data[0], data[1][0], data[1][1]
        self.value = v
        self.x = x
        self.y = y
        self.left = None
        self.right = None

class Nodemgmt:
    def __init__(self, data):
        self.head = data
        self.head.left = None
        self.head.right = None

    def insert(self, input_node):
        self.current_node = self.head
        while True:
            if input_node.x < self.head.x:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node = input_node
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = input_node
                    break
    def pre_order(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.value)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.head)

    def post_order(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.value)
        _post_order_traversal(self.head)

def solution(nodeinfo):
    nodes = [(i+1,nodeinfo[i]) for i in range(len(nodeinfo))]
    nodes.sort(key=lambda data:data[1][1], reverse=True)
    init_data = nodes.pop(0)
    init_node = Node(init_data)
    NodeMgmt = Nodemgmt(init_node)
    while nodes:
        data = nodes.pop(0)
        node = Node(data)
        NodeMgmt.insert(node)
    # NodeMgmt.post_order()
    NodeMgmt.pre_order()

    answer = [[]]
    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))