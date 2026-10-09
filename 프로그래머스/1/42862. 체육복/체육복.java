import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int lLen = lost.length;
        int rLen = reserve.length;
        int answer = n - lLen;
        Arrays.sort(reserve);
        boolean[] isLost = new boolean[31];
        for (int i = 0; i < lLen; ++i) {
            isLost[lost[i]] = true;
        }
        for (int i = 0; i < rLen; ++i) {
            int stuNum = reserve[i];
            if (isLost[stuNum]) {
                answer++;
                isLost[stuNum] = false;
                reserve[i] = -1;
            }
        }
        
        for (int i = 0; i < rLen; ++i) {
            int stuNum = reserve[i];
            if (stuNum == -1)
                continue;
            if (isLost[stuNum - 1]) {
                answer++;
                isLost[stuNum - 1] = false;
            }
            else if (isLost[stuNum + 1]) {
                answer++;
                isLost[stuNum + 1] = false;
            } 
        }
        
        return answer;
    }
}