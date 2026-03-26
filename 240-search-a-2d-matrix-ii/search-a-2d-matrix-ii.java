class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int rowLength = matrix.length;
        boolean result = false;

        for(int i = 0 ; i < rowLength ; i++)
        {
            if(matrix[i][0] <= target)
            {
                int colLength = matrix[i].length;
                for(int j = 0 ; j < colLength ; j++)
                {
    
                    if(matrix[i][j] == target)
                    {
                        result = true;

                        return result;
                    }

                     if(matrix[i][j] > target)
                    {
                        break;
                    }
                }
            }
            
        }

        return result;
    }
}