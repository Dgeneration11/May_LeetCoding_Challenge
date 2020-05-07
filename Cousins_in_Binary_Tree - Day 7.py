     def isCousins(self, root, x, y):
        
        def dfs(root,value,depth,parent):
            if not root : return
            
            if root.val == value:
                global depth_res
                global parent_res
                depth_res = depth
                parent_res = parent
                print(depth,parent)
                return
            else:
                dfs(root.left,value,depth+1,root.val)
                dfs(root.right,value,depth+1,root.val)
        
        dfs(root,x,0,0)
        
        x_depth = depth_res
        x_parent = parent_res
        print(x_depth,x_parent)
        dfs(root,y,0,0)
        print(x_depth,x_parent)
        
        if x_depth == depth_res and x_parent != parent_res:
            return True
        else:
            return False
        