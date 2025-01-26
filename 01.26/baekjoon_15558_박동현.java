import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static class Node {
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int[] dr = {-1,1};
    static int N,K;
    static int[][] arr;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new int[2][N];
        for (int i=0; i<2; i++) {
            String line = br.readLine();
            for (int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(line.charAt(j)+"");
            }
        }
        System.out.println(bfs()? 1:0);
    }

    private static boolean bfs() {
        int[][] visit = new int[2][N];

        Queue<Node> q = new LinkedList<>();
        q.add(new Node(0,0));
        while (!q.isEmpty()) {
            Node now = q.poll();

            for (int dy: dr) {
                int ny = now.y + dy;

                if (ny >= N) return true;
                if (ny <= visit[now.x][now.y]) continue;
                if (arr[now.x][ny] == 0) continue;
                if (visit[now.x][ny] != 0) continue;
                visit[now.x][ny] = visit[now.x][now.y] + 1;
                q.add(new Node(now.x,ny));
            }

            int ny = now.y + K;
            if (ny >= N) return true;
            if (ny <= visit[now.x][now.y]) continue;
            if (arr[1-now.x][ny] == 0) continue;
            if (visit[1-now.x][ny] != 0) continue;
            visit[1-now.x][ny] = visit[now.x][now.y] + 1;
            q.add(new Node(1-now.x,ny));
        }
        return false;
    }
}