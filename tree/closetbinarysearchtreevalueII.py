# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BetterSolution:
    def smaller(self, route: '[(TreeNode, bool)]'):
        if route[-1][0].left:
            route.append((route[-1][0].left, True))
            while route[-1][0].right:
                route.append((route[-1][0].right, False))
        elif not route[-1][1]:
            route.pop()
        else:
            while route and route[-1][1]:
                route.pop()
            if route:
                route.pop()
        return route
    
    def larger(self, route: '[(TreeNode, bool)]'):
        if route[-1][0].right:
            route.append((route[-1][0].right, False))
            while route[-1][0].left:
                route.append((route[-1][0].left, True))
        elif route[-1][1]:
            route.pop()
        else:
            while route and not route[-1][1]:
                route.pop()
            if route:
                route.pop()
        return route
    
    def closestKValues(self, root: 'TreeNode', target: 'float', k: 'int') -> '[int]':
        if root.left:
            s, l = self.smaller([(root, True)]), [(root, True)]
        else:
            s, l = [(root, True)], self.larger([(root, True)])
        ans = []
        while s and l:
            if s[-1][0].val > target:
                s, l = self.smaller(s), self.smaller(l)
            elif target > l[-1][0].val:
                s, l = self.larger(s), self.larger(l)
            else:
                break
        while k > 0:
            if not s:
                ans.append(l[-1][0].val)
                l = self.larger(l)
            elif not l:
                ans.append(s[-1][0].val)
                s = self.smaller(s)
            else:
                sd, ld = abs(target - s[-1][0].val), abs(target - l[-1][0].val)
                if sd <= ld:
                    ans.append(s[-1][0].val)
                    s = self.smaller(s)
                else:
                    ans.append(l[-1][0].val)
                    l = self.larger(l)
            k -= 1
        return ans

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> [int]:

        # Helper, takes a path and makes it the path to the next node
        def nextpath(path, kid1, kid2):
            if path:
                if kid2(path):
                    path += kid2(path),
                    while kid1(path):
                        path += kid1(path),
                else:
                    kid = path.pop()
                    while path and kid is kid2(path):
                        kid = path.pop()

        # These customize nextpath as forward or backward iterator
        kidleft = lambda path: path[-1].left
        kidright = lambda path: path[-1].right

        # Build path to closest node
        path = []
        while root:
            path += root,
            root = root.left if target < root.val else root.right
        dist = lambda node: abs(node.val - target)
        path = path[:path.index(min(path, key=dist))+1]

        # Get the path to the next larger node
        path2 = path[:]
        nextpath(path2, kidleft, kidright)

        # Collect the closest k values by moving the two paths outwards
        vals = []
        for _ in range(k):
            if not path2 or path and dist(path[-1]) < dist(path2[-1]):
                vals += path[-1].val,
                nextpath(path, kidright, kidleft)
            else:
                vals += path2[-1].val,
                nextpath(path2, kidleft, kidright)
        return vals