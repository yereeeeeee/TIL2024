import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class bj_9237 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // 입력
        int N = Integer.parseInt(st.nextToken());
        // reverseOrder 사용을 위해 Wrapper 클래스 사용
        Integer[] arr = new Integer[N];

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            arr[i] = Integer.valueOf(st.nextToken());
        }

        // 역순 정렬
        Arrays.sort(arr, Collections.reverseOrder());

        int ans = 0;
        for (int i=0; i<N; i++) {
            ans = Math.max(arr[i] + i + 2, ans);
        }

        System.out.println(ans);
    }
}
