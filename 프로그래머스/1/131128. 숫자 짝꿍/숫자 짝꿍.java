import java.lang.Math;
import java.util.*;
class Solution {
    public String solution(String X, String Y) {
        int[] xCnts = new int[10];
        int[] yCnts = new int[10];
        int xLen = X.length();
        int yLen = Y.length();
        for (int i = 0; i < xLen; ++i) {
            char c = X.charAt(i);
            xCnts[c - '0']++;
        }
        for (int i = 0; i < yLen; ++i) {
            char c = Y.charAt(i);
            yCnts[c - '0']++;
        }
        StringBuilder answer = new StringBuilder();
        boolean isNotChanged = true;
        for (int i = 9; i >= 0; --i) {
            int minVal = Math.min(xCnts[i], yCnts[i]);
            if (minVal > 0) {
                if (isNotChanged && i == 0) {
                    answer.append("0");
                    isNotChanged = false;
                    break;
                }
                while (minVal > 0) {
                    isNotChanged = false;
                    answer.append(i);
                    minVal--;
                }
            }
        }
        if (isNotChanged)
            answer.append("-1");
        return answer.toString();
    }
}