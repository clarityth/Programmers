import java.util.*;
class Solution {
    private int getIdx(String str) {
        if (str.equals("code")) return 0;
        else if (str.equals("date")) return 1;
        else if (str.equals("maximum")) return 2;
        else if (str.equals("remain")) return 3;
        return -1;
    }
    
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        int resLen = 0;
        int[][] temp = new int[data.length][4];
        int answerLen = 0;
        int resIdx = 0;
        int extIdx = getIdx(ext);
        
        if (extIdx != -1) {
            for (int i = 0; i < data.length; ++i) {
                if (data[i][extIdx] < val_ext) {
                    temp[resIdx++] = data[i];
                    ++answerLen;
                }
            }
        }
        
        int[][] answer = Arrays.copyOfRange(temp, 0, answerLen);
        int sortIdx = getIdx(sort_by);
        if (sortIdx != -1) {
            Arrays.sort(answer, new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    return o1[sortIdx] - o2[sortIdx];
                }
            });
        }
        return answer;
    }
}