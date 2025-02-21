/*
 * 매직 포션
 * 
 * 다익스트라
 * 
 * 문 부수고 다익스트라로 이동하기
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class bj_12913 {

    static class Node implements Comparable<Node> {
        int x;
        double dist;
        int cnt;

        public Node() {
            this.x = 0;
            this.dist = 0;
            this.cnt = 0;
        }

        public Node(int x, double dist, int cnt) {
            this.x = x;
            this.dist = dist;
            this.cnt = cnt;
        }

        @Override
        public int compareTo(Node o) {
            return Double.compare(this.dist, o.dist);
        }

    }
    static int N;
    static int M;
    static int[][] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][N];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            char[] tmp = st.nextToken().toCharArray();
            for (int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(String.valueOf(tmp[j]));
            }
        }
        System.out.println(dijkstra());
    }

    private static double dijkstra() {
        double[][] distance = new double[N][M+1];
        for (int i=0; i<N; i++) {
            Arrays.fill(distance[i], Integer.MAX_VALUE);
        }

        distance[0][0] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node());
        while (!pq.isEmpty()) {
            Node now = pq.poll();

            if (now.dist > distance[now.x][now.cnt]) continue;

            for (int nxt=0; nxt<N; nxt++) {
                if (now.x == nxt) continue;

                double dist_next = now.dist + arr[now.x][nxt];
                if (distance[nxt][now.cnt] > dist_next) {
                    distance[nxt][now.cnt] = dist_next;
                    pq.add(new Node(nxt, dist_next, now.cnt));
                }
                if (now.cnt < M) {
                    dist_next = now.dist + (double) arr[now.x][nxt] / 2;
                    if (distance[nxt][now.cnt + 1] > dist_next) {
                        distance[nxt][now.cnt + 1] = dist_next;
                        pq.add(new Node(nxt, dist_next, now.cnt + 1));
                    }
                }
            }
        }
        double ans = Integer.MAX_VALUE;
        for (double tmp: distance[1]) {
            ans = Math.min(ans, tmp);
        };

        return ans;
    }
}