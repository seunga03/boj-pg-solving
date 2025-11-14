class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        String[] arr = my_string.split("");
        for (String a:arr){
            for (int i=0;i<n;i++) {
                answer += a;                
            }
        }
        return answer;
    }
}