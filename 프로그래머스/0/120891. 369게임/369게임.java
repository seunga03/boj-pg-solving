class Solution {
    public int solution(int order) {
        int answer = 0;
        
        String s = Integer.toString(order);
        String[] arr = s.split("");
        
        for (String i : arr) {
            if ((i.equals("3")) || (i.equals("6")) || (i.equals("9"))) {
                answer++;
            }
        }
        
        return answer;
    }
}