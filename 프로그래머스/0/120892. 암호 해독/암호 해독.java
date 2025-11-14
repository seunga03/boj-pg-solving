class Solution {
    public String solution(String cipher, int code) {
        String answer = "";
        String[] arr = cipher.split("");
        for (int i=1;i<(arr.length+1);i++){
            if (i%code==0) {
                answer += arr[i-1];
            }
        }
        return answer;
    }
}