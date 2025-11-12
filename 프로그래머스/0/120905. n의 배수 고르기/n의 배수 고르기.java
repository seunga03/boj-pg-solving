class Solution {
    public int[] solution(int n, int[] numlist) {
        
        int len = 0;
        
        for (int num : numlist) {
            if (num % n == 0){
                len++;
            }
        }
        
        int[] answer = new int[len];
        
        int i = 0;
        
        for (int num : numlist) {
            if (num % n == 0){
                answer[i] = num;
                i++;
            }
        }

        return answer;
    }
}