class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(root):
            if root == None:
                return ",#"
            
            return "," + str(root.val) + serialize(root.left) + serialize(root.right)
        
        def getLPS(s):
            m, j = len(s), 0
            lps = [0] * m
            for i in range(1, m):
                while s[i] != s[j] and j > 0: j = lps[j-1]
                if s[i] == s[j]:
                    j += 1
                    lps[i] = j
            return lps
        
        def kmp(s, p):
            lps = getLPS(p)
            n, m, j = len(s), len(p), 0
            for i in range(n):
                while s[i] != p[j] and j > 0: j = lps[j-1]
                if s[i] == p[j]:
                    j += 1
                    if j == m: return True
            return False
            
        return kmp(serialize(root), serialize(subRoot))