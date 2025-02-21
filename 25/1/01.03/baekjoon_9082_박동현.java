/*
 * 동전
 * 
 * DP
 */


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    static StringBuffer sb = new StringBuffer();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int tc = Integer.parseInt(st.nextToken());

        for (int t=0; t<tc; t++) {

            int N = Integer.parseInt(br.readLine());
            int[] coins = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i=0; i<N; i++) {
                coins[i] = Integer.parseInt(st.nextToken());
            }

            int K = Integer.parseInt(br.readLine());
            int[] DP = new int[K+1];
            DP[0] = 1;
            for (int coin: coins) {
                for (int i=1; i<=K; i++) {
                    if (i >= coin) {
                        DP[i] += DP[i-coin];
                    }
                }
            }
            sb.append(DP[K]).append("\n");
        }
        System.out.println(sb);
    }
}