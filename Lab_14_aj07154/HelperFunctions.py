# Helper Function #1
def insert(bst, key):
    if not bst:
        bst.update({"value": key, "left": {}, "right": {}})
    elif key < bst["value"]:
        insert(bst["left"], key)
    elif key > bst["value"]:
        insert(bst["right"], key)

# Helper Function #2
def exist(bst, key):
    if not bst:
        return False
    elif bst["value"] == key:
        return True
    elif key < bst["value"]:
        return exist(bst["left"], key)
    else:
        return exist(bst["right"], key)

# Helper Function #3
def minimum(bst, starting_node):
    if not bst:
        return None
    current = bst
    while current["value"] != starting_node:
        if starting_node > current["value"]:
            current = current["right"]
        elif starting_node < current["value"]:
            current = current["left"]
    while current["left"]:
        current = current["left"]
    return current

# Helper Function #4
def maximum(bst, starting_node):
    if not bst:
        return None
    current = bst
    while current["value"] != starting_node:
        if starting_node < current["value"]:
            current = current["left"]
        elif starting_node > current["value"]:
            current = current["right"]
    while current["right"]:
        current = current["right"]
    return current

# Helper Function #5
def inorder_traversal(bst, res):
    if not bst:
        return
    inorder_traversal(bst["left"], res)
    res.append(bst["value"])
    inorder_traversal(bst["right"], res)

# Helper Function #6
def preorder_traversal(bst, res):
    if not bst:
        return
    res.append(bst["value"])
    preorder_traversal(bst["left"], res)
    preorder_traversal(bst["right"], res)

# Helper Function #7
def postorder_traversal(bst, res):
    if not bst:
        return
    postorder_traversal(bst["left"], res)
    postorder_traversal(bst["right"], res)
    res.append(bst["value"])

# Helper Function #8
def successor(bst, key, successor_node=None):
    if not bst:
        return None
    else:
        current = bst
        while current["value"] != key:
            if key < current["value"]:
                successor_node = current
                current = current["left"]
            if key > current["value"]:
                current = current["right"]
        if current["right"]:
            minn = minimum(current["right"], current["right"]["value"])["value"]
            return minn
        if successor_node:
            return successor_node["value"]
        return None

