class Solution {
    public int solution(int n, int k) {        
        int service = (n / 10) * 2000;
        int lambKebabs = n * 12000;
        int drink = k * 2000;
        int answer = lambKebabs + drink - service;

        return answer;
    }
}