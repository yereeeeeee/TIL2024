import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] before, after;
    static int[] dx = {0,1,0,-1};
    static int[] dy = {-1,0,1,0};
    static int N,M;
    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        before = fillArr(N,M);
        after = fillArr(N,M);
        
        System.out.println(check() && Arrays.deepEquals(before, after) ? "YES" : "NO");
    }

    static int[][] fillArr(int N, int M) throws Exception {
        int[][] arr = new int[N][M];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        return arr;
    }

    static void dfs(int x, int y, int now, int nxt) {
        if (before[x][y] != now) {
            return;
        }
        before[x][y] = nxt;

        for (int i=0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                dfs(nx,ny,now,nxt);
            }
        }
    }

    static boolean check() {
        int cnt = 0;
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (before[i][j] != after[i][j]) {
                    dfs(i,j,before[i][j], after[i][j]);
                    if (++cnt > 1) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}