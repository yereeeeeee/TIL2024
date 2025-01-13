import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        long[] arr = new long[n];
        long max_mk = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            max_mk = Math.max(max_mk, arr[i]);
        }

        long left = 1;
        long right = max_mk;
        long answer = 0;

        while (left <= right) {
            long mid = (left + right) / 2;
            int cnt = 0;

            for (long mk : arr) {
                // 몇 명 한테 나눠줄 수 있는지?
                cnt += mk / mid;
            }

            // cnt가 많으면 mid를 키우기
            if (cnt >= k) {
                answer = mid;
                left = mid + 1;
            }
            // cnt가 적으면 mid를 줄이기
            else {
                right = mid - 1;
            }
        }

        System.out.println(answer);
        
    }
}