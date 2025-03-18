import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static StringBuffer sb = new StringBuffer();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] ans = new int[N];
        for (int i=0; i<N; i++) {
            int cnt = 0;
            for (int j = 0; j < N; j++) {
                 if (ans[j] != 0) continue;

                 if (arr[i] == cnt) {
                    ans[j] = i+1;
                    break;
                 } else if (ans[j] == 0) cnt ++;
            }
        }
        for (int i=0; i<N; i++) {
            sb.append(ans[i]).append(" ");
        }
        System.out.println(sb);
    }
}