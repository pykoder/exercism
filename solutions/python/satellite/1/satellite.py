def t_f_t(preorder, inorder):
    root = preorder[0]
    root_index = inorder.index(root)
    left = inorder[0:root_index]
    right = inorder[root_index+1:]
    print(root, left, right)
    
    l = {} if not left else t_f_t(preorder[1:len(left)+1], left)
    r = {} if not right else t_f_t(preorder[len(left)+1:], right)
    return {'v': root, 'l': l, 'r': r}

def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError(f"traversals must have the same length")
    s1 = {*preorder}
    s2 = {*inorder}
    if s1 != s2:
        raise ValueError("traversals must have the same elements")
    if len(s1) != len(preorder) or len(s2) != len(inorder):
        raise ValueError("traversals must contain unique items")
    if not preorder:
        return {}
    return t_f_t(preorder, inorder)        
    
