import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static StringBuffer sb = new StringBuffer();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        int[] arr = new int[N+1];
        st = new StringTokenizer(br.readLine());

        int prev = 0;
        for (int i=1; i<=N; i++) {
            int cur = Integer.parseInt(st.nextToken()) + i - 1;
            if (prev < cur) prev = cur;
            arr[i] = prev;
        }

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<M; i++) {
            int acorn = Integer.parseInt(st.nextToken());
            int left = 1;
            int right = N+1;

            while (left < right) {
                int mid = (left+right) / 2;

                if (acorn > arr[mid]) {
                    left = mid + 1;
                }
                else {
                    right = mid;
                }
            }
            sb.append(right).append(" ");
        }
        System.out.println(sb);
    }
}
