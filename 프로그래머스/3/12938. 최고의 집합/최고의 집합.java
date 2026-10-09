class Solution {
    public int[] solution(int n, int s) {
        int quotient = s / n;
        int remain = s % n; 
        if (n > s) {
            return new int[]{-1};
        }
        int[] answer = new int[n];
        for (int i = 0; i < n; ++i) {
            if (i >= n - remain){
                answer[i] = quotient + 1;
            } else {
                answer[i] = quotient;
            }
        }
        return answer;
    }
}