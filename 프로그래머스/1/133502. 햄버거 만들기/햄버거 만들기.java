import java.util.*;
class Solution {
    private final int[] pattern = {1, 2, 3, 1};
    public int solution(int[] ingredient) {
        int answer = 0;
        ArrayList<Integer> il = new ArrayList<>();
        int len = ingredient.length;
        for (int i = 0; i < len; ++i) {
            il.add(ingredient[i]);
            while (il.size() >= 4) {
                int lastIdx = il.size() - 1;
                if (il.get(lastIdx) == 1 && il.get(lastIdx - 1) == 3 && il.get(lastIdx - 2) == 2 && il.get(lastIdx - 3) == 1) {
                    answer++;
                    for (int j = 0; j < 4; ++j) {
                        il.remove(lastIdx - j);
                    }
                } else 
                    break;
            }
        }
        return answer;
    }
}