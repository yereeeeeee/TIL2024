import java.io.*;
import java.util.*;

class Pos {
    int z;
    int x;
    int y;

    public Pos(int z, int x, int y) {
        this.z = z;
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int M, N, H;
    static int[][][] arr;
    static int[] dx = {-1, 0, 1, 0, 0, 0};
    static int[] dy = {0, 1, 0, -1, 0, 0};
    static int[] dz = {0, 0, 0, 0, -1, 1};
    static Queue<Pos> q = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        arr = new int[H][N][M];
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < M; k++) {
                    arr[i][j][k] = Integer.parseInt(st.nextToken());
                    if (arr[i][j][k] == 1) q.add(new Pos(i, j, k));
                }
            }
        }

        System.out.println(bfs());
    }

    static int bfs() {
        while (!q.isEmpty()) {
            Pos curr = q.poll();

            for (int d = 0; d < 6; d++) {
                int nx = curr.x + dx[d];
                int ny = curr.y + dy[d];
                int nz = curr.z + dz[d];

                if (check(nz, nx, ny)) {
                    q.add(new Pos(nz, nx, ny));
                    arr[nz][nx][ny] = arr[curr.z][curr.x][curr.y] + 1;
                }
            }
        }

        int result = Integer.MIN_VALUE;

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < M; k++) {
                    if (arr[i][j][k] == 0) return -1;
                    result = Math.max(result, arr[i][j][k]);
                }
            }
        }
        if (result == 1) return 0;
        else return (result - 1);
    }

    static boolean check(int z, int x, int y) {
        if (z < 0 || z >= H || x < 0 || x >= N || y < 0 || y >= M) return false;
        if (arr[z][x][y] == 0) return true;
        else return false;
    }
}
