class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int pCnt = 0, yCnt = 0;
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            if (c == 'P' || c == 'p')
                pCnt++;
            else if (c == 'Y' || c == 'y')
                yCnt++;
        }
        if (pCnt != yCnt)
            answer = false;
        
        return answer;
    }
}