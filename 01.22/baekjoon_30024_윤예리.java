import java.io.*;
import java.util.*;

public class Main {
    static int n, m, k;
    static int[][] arr;
    static boolean[][] visited;
    static PriorityQueue<Pos> pq = new PriorityQueue<>();
    static int[] dx = new int[]{-1, 0, 1, 0};
    static int[] dy = new int[]{0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n][m];
        visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (i==0 || j==0 || i==n-1 || j==m-1) {
                    pq.add(new Pos(arr[i][j], i, j));
                    visited[i][j] = true;
                }
            }
        }

        k = Integer.parseInt(br.readLine());
        // 옥수수 밭 돌면서 q에 넣고 힙으로 뽑기
        for (int i = 0; i < k; i++) {
            Pos cur = pq.poll();
            System.out.println((cur.x + 1) + " " + (cur.y + 1));

            for (int d = 0; d < 4; d++) {
                int nx = cur.x + dx[d];
                int ny = cur.y + dy[d];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if (visited[nx][ny]) continue;

                pq.add(new Pos(arr[nx][ny], nx, ny));
                visited[nx][ny] = true;
            }
        }
    }

    static class Pos implements Comparable<Pos>{
        int value;
        int x;
        int y;

        public Pos(int value, int x, int y) {
            this.value = value;
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Pos o) {
            return Integer.compare(o.value, this.value);
        }
    }
}