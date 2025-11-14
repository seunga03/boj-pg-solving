class Solution {
    public int solution(int[] array) {
        String s = "";
        int answer = 0;
        for(int a : array) {
            s += Integer.toString(a);
        }
        
        String[] arr = s.split("");
        
        for (String ch : arr) {
            if (ch.equals("7")) {
                answer++;
            }
        }
        
        return answer;
    }
}