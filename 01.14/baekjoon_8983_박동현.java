import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int M;
    static int[] lines;
    public static void main(String[] args) throws Exception { 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        lines = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<M; i++) {
            lines[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(lines);

        int ans = 0;
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            int idx = binarySearch(x);
            int distLeft = Math.abs(x - lines[idx]) + y;
            int distRight = idx<M-1? Math.abs(x - lines[idx+1]) + y: Integer.MAX_VALUE;
            int dist = Math.min(distLeft, distRight);

            if (dist<=L) ans ++;
        }

        System.out.println(ans);
    }

    private static int binarySearch(int x) {
        int left = 0;
        int right = M-1;
        int idx = 0;
        while (left <= right) {
            int mid = (left+right) / 2;

            if (lines[mid] == x) return mid;
            
            if (lines[mid] < x) {
                idx = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return idx;
    }
}