# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        _, result = build_tree(S, 0, 0)
        return result

def build_tree(S, curr_index, curr_depth):
    if curr_index >= len(S):
        return curr_index, None
    
    new_index, new_depth = extract_depth(S, curr_index)
    new_index, new_value = extract_value(S, new_index)
    
    if new_depth == curr_depth:
        result = TreeNode(new_value)
        
        new_index, result.left = build_tree(S, new_index, curr_depth + 1)
        
        if new_index < len(S):
            new_index, result.right = build_tree(S, new_index, curr_depth + 1)

        return new_index, result
    
    else:
        return curr_index, None

def extract_depth(S, curr_index):
    depth = 0
    i = curr_index
    
    for i in range(curr_index, len(S)):
        if S[i] == '-':
            depth += 1
        else:
            break
    
    return i, depth

def extract_value(S, curr_index):
    value = []
    i = curr_index
    
    for i in range(curr_index, len(S)):
        if S[i] != '-':
            value.append(S[i])
        else:
            break
    
    return i, int(''.join(value)) if value else None    


class BetterSolution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        nodes = [(len(d), int(v)) for d, v in re.findall(r'(\-*)(\d+)', S)]

        root = TreeNode(nodes[0][1])
        stack = [(root, 0)]
        for i in range(1, len(nodes)):
            d, v = nodes[i]
            cur = TreeNode(v)
            while d != stack[-1][1] + 1:
                stack.pop()
            if stack[-1][0].left:
                stack[-1][0].right = cur
            else:
                stack[-1][0].left = cur
            stack.append((cur, d))
        return root