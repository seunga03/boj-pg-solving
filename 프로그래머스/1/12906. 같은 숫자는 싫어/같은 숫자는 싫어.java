import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        for (int a : arr) {
            if (list.isEmpty() || list.get(list.size() - 1) != a) {
                list.add(a);
            }
        }
        
        int[] answer = list.stream().mapToInt(Integer::intValue).toArray();

        return answer;
    }
}