def kthSmallest(self, root: TreeNode, k: int) -> int:
        inOrderRes = []
        def inOrder(root):
            if root==None: return
            inOrder(root.left)
            if (len(inOrderRes)<=k): 
                inOrderRes.append(root.val)
            else: 
                return
            # print(root.val)
            inOrder(root.right)
        inOrder(root)
        # print(inOrderRes)
        return inOrderRes[k-1]