import java.util.*;

class Solution {
    public int solution(String before, String after) {
        String[] bef = before.split("");
        String[] aft = after.split("");
        
        Arrays.sort(bef);
        Arrays.sort(aft);
        
        if (Arrays.equals(bef, aft)) {
            return 1;
        }
        return 0;
    }
}