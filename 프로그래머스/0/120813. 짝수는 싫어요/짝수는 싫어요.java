class Solution {
    public int[] solution(int n) {
        int size = 1;
        if (n % 2 == 1)
            size = n / 2 + 1; 
        else
            size = n / 2;
        int[] answer = new int[size];
        int idx = 0;
        for (int i = 1; i <= n; ++i) {
            if (i % 2 == 1) {
                answer[idx] = i;
                idx++;
            }
        }
        
        return answer;
    }
}