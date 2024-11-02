import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[] curr, target, diff, dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        curr = new int[n];
        target = new int[n];
        diff = new int[n];
        dp = new int[n]; // n 번째 줄까지 tab 하는 최소 수
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            curr[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            target[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i < n; i++) {
            diff[i] = target[i] - curr[i];
        }
        dp[0] = Math.abs(diff[0]);

        for (int i = 1; i < n; i++) {
            // 다음이랑 부호가 같다면
            if (diff[i] * diff[i-1] > 0) {
                // 더 작은 수 까지 tab 해주기
                dp[i] = dp[i-1] + Math.max(0, Math.abs(diff[i]) - Math.abs(diff[i-1]));
            }
            else {
                // 얘만 tab 해주기
                dp[i] = dp[i-1] + Math.abs(diff[i]);
            }
        }

        System.out.println(dp[n-1]);
    }
}