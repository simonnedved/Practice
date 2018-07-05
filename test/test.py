from node import Node

idx = 0


def get_children(char):
    if char == 'a':
        return ['b', 'c']
    if char == 'b':
        return ['d']
    if char == 'c':
        return ['e', 'f']
    else:
        return []


def create_node(node):
    global idx
    if get_children(node.value) != []:
        for child in get_children(node.value):
            node.children.append(create_node(Node(child)))
    return node


root = create_node(Node('a'))
print(root)



