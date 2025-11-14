import java.util.*;

class Solution {
    public String[] solution(String my_str, int n) {
        List<String> list = new ArrayList<>();

        for (int i = 0; i < my_str.length(); i += n) {
            // Math.min을 사용해 길이 n의 부분문자열을 넣거나, 나머지(길이 n 미만)를 넣기
            list.add(my_str.substring(i, Math.min(i + n, my_str.length())));
        }

        return list.toArray(new String[0]);
    }
}
