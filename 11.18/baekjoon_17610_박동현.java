import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_17610 {

    static int[] data;
    static int[] arr;
    static int N;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        arr = new int[N];
        st = new StringTokenizer(br.readLine());
        int sum = 0;
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            sum += arr[i];
        }
        data = new int[sum+1];
        backtrack(0,0);
        int tmp = 0;
        for (int i=1; i<=sum; i++) {
            tmp += data[i];
        }
        System.out.println(sum-tmp);
    }

    private static void backtrack(int idx, int res) {
        if (idx == N) return;

        backtrack(idx+1, res+arr[idx]);
        backtrack(idx+1, res);
        backtrack(idx+1, Math.abs(res-arr[idx]));

        data[res+arr[idx]] = 1;
        data[res] = 1;
        data[Math.abs(res-arr[idx])] = 1;
    }
}
