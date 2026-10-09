import java.util.HashMap;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> playerDic = new HashMap<>();
        String[] answer = new String[players.length];
        for (int i = 0; i < players.length; ++i) {
            playerDic.put(players[i], i);
            answer[i] = players[i];
        }
        for (int i = 0; i < callings.length; ++i) {
            int targetRank = playerDic.get(callings[i]);
            
            playerDic.replace(answer[targetRank - 1], targetRank);
            playerDic.replace(answer[targetRank], targetRank - 1);
            swap(answer, targetRank - 1, targetRank);
        }
        return answer;
    }
    public void swap(String[] a, int p1, int p2) {
        String temp = a[p1];
        a[p1] = a[p2];
        a[p2] = temp;
    }
}