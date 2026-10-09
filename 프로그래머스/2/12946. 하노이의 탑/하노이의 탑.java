import java.util.ArrayList;
class Solution {
    private static ArrayList<int[]> temp;
    public int[][] solution(int n) {
        temp = new ArrayList<int[]>();
        hanoi(n, 1, 2, 3);
        int[][] answer = new int[temp.size()][];
        for (int i = 0; i < temp.size(); ++i) {
            answer[i] = temp.get(i);
        }
        return answer;
    }
    public void hanoi(int n, int from, int by, int to) {
        if (n == 1) {
            temp.add(new int[]{from, to});
            return;
        }
        hanoi(n - 1, from, to, by);
        temp.add(new int[]{from, to});
        hanoi(n - 1, by, from, to);
    }
}