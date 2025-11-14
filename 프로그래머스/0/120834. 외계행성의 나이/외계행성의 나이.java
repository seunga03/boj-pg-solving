class Solution {
    public String solution(int age) {
        String answer = "";
        char[] arr = (age + "").toCharArray();

        for (char a : arr) {
            answer += (char)('a' + (a - '0'));
        }
        return answer;
    }
}