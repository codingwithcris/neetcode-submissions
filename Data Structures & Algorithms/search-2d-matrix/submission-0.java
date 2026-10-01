class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rowL = 0;
        int rowH = matrix.length - 1;

        while (rowL <= rowH) {
            int outerMid = rowL + ((rowH - rowL) / 2);
            int[] row = matrix[outerMid];

            int h = row.length - 1;
            int l = 0;
            int innerMid = 0;
            while (l <= h) {
                innerMid = l + ((h-l) / 2);
                if (row[innerMid] > target) {
                    h = innerMid - 1;
                } else if (row[innerMid] < target) {
                    l = innerMid + 1;
                } else {
                    return true;
                }
            }

            if (row[innerMid] > target) {
                rowH = outerMid - 1;
            } else {
                rowL = outerMid + 1;
            }
        }
        return false;
    }
}
