from binary_tree import TreeNode


def pre_order(root: TreeNode | None, res: list[int]):
    """先序遍历"""
    if not root:
        return
    res.append(root.val)
    pre_order(root.left, res)
    pre_order(root.right, res)

def in_order(root: TreeNode | None, res: list[int]):
    """中序遍历"""
    if not root:
        return
    in_order(root.left, res)
    res.append(root.val)
    in_order(root.right, res)

def post_order(root: TreeNode | None, res: list[int]):
    """后序遍历"""
    if not root:
        return
    post_order(root.left, res)
    post_order(root.right, res)
    res.append(root.val)

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    pre_res = []
    pre_order(n1, pre_res)
    print(pre_res)

    in_res = []
    in_order(n1, in_res)
    print(in_res)

    post_res = []
    post_order(n1, post_res)
    print(post_res)