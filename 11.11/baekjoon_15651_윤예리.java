import java.util.*;
import java.io.*;

public class baekjoon_15651_윤예리 {
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        backtracking(0, new int[m], sb);
        System.out.print(sb.toString());
    }

    static void backtracking(int idx, int[] tmp, StringBuilder sb) {
        if (idx == m) {
            for (int i = 0; i < m; i++) {
                sb.append(tmp[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = 1; i <= n; i++) {
            tmp[idx] = i;
            backtracking(idx + 1, tmp, sb);
        }
    }
}
