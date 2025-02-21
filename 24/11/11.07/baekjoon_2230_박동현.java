import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj_2230 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];

        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(arr);

        int left = 0;
        int right = 1;
        int ans = Integer.MAX_VALUE;
        while (left < N && right < N) {

            if (arr[right] - arr[left] == M) {
                ans = M;
                break;
            }

            if (arr[right] - arr[left] > M) {
                ans = Math.min(ans, arr[right] - arr[left]);
                left ++;
            }

            else if (arr[right] - arr[left] < M) {
                right ++;
            }

        }
        
        System.out.println(ans);
    }
}
