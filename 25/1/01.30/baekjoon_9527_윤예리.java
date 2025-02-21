import java.io.*;
import java.util.*;

public class Main {
    static long[] dp = new long[55];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());

        // DP[n] = DP[n-1] × 2 + 2^n
        dp[0] = 1;
        for (int i = 1; i < 55; i++) {
            dp[i] = (dp[i-1] << 1) + (1L << i);
        }
        long result = calc(b) - calc(a-1);
        System.out.println(result);
    }

    static long calc(long n) {
        long cnt = n&1;
        int size = (int) (Math.log(n) / Math.log(2));
        for (int i=size; i>0; i--) {
            if ((n & (1L<<i)) != 0L) {
                cnt += dp[i-1] + (n - (1L<<i) + 1);
                n -= (1L << i);
            }
        }
        return cnt;
    }
}