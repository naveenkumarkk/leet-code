class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        i = 0
        ans = []
        dirc = 'u'
        x,y = 0, 0
        while i<m+n-1:
            try:
                ans.append(mat[x][y])
            except:
                pass
            if dirc == 'u':
                if y+1<n and x-1>=0:
                    x -= 1
                    y += 1
                else:
                    dirc = 'd'
                    y += 1
                    i += 1
            else:
                if x+1<m and y-1>=0:
                    x+=1
                    y-=1
                else:
                    dirc = 'u'
                    x += 1
                    i += 1
        return ans