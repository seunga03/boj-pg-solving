class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        String strings = num + "";
        String[] arr = strings.split("");
        int count = 1;
        String x = k + "";
        
        for (String a : arr) {
            if (a.equals(x)) {
                return count;
            }
            count++;
        }
        
        return answer;
    }
}