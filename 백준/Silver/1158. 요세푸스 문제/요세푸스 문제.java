import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> queue = new LinkedList<>();
    
        int n = sc.nextInt();
        int k = sc.nextInt();
    
        for (int i = 1; i <= n; i++) {
            queue.add(i);
        }
    
        ArrayList<Integer> result = new ArrayList<>();

        while (!queue.isEmpty()) {
            for (int i=0;i<k-1;i++) {
                int tmp1 = queue.poll();
                queue.offer(tmp1);
            }
        
            int tmp2 = queue.poll();
            result.add(tmp2);        
        }
    
        // result를 <a, b, c> 형태로 출력 - 여러 블로그 참고
        StringBuilder sb = new StringBuilder();
        sb.append("<");

        for (int i = 0; i < result.size(); i++) {
            sb.append(result.get(i));
            if (i != result.size() - 1) {
                sb.append(", ");
            }
        }

        sb.append(">");
        System.out.println(sb.toString());

    }
}