/*
 * 자바로 번역하다보면 틀린 부분 찾기 쉬움 
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static class Node implements Comparable<Node> {
        int x;
        double weight;
        int isRunnable;

        public Node(int x, double weight) {
            this.x = x;
            this.weight = weight;
        }
        public Node(int x, double weight, int isRunnable) {
            this.x = x;
            this.weight = weight;
            this.isRunnable = isRunnable;
        }

        @Override
        public int compareTo(Node o) {
            return Double.compare(this.weight, o.weight);
        }
    }

    static ArrayList<ArrayList<Node>> graph = new ArrayList<>();
    static int N;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        for (int i=0; i<=N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph.get(a).add(new Node(b,c));
            graph.get(b).add(new Node(a,c));
        }

        int[] fox = dijkstraForFox();
        double[] wolf = dijkstraForWolf();

        int ans = 0;
        for (int i=1; i<=N; i++) {
            if (fox[i] < wolf[i]) {
                ans ++;
            }
        }
        System.out.println(ans);
    }

    private static int[] dijkstraForFox() {
        int[] distance = new int[N+1];
        Arrays.fill(distance, Integer.MAX_VALUE);

        distance[1] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(1, 0));
        while (!pq.isEmpty()) {
            Node node = pq.poll();

            int now = node.x;
            int nowDistance = (int) node.weight;

            if (nowDistance > distance[now]) continue;
            for (Node next: graph.get(now)) {
                int nextDistance = nowDistance + (int) next.weight;
                if (distance[next.x] > nextDistance) {
                    distance[next.x] = nextDistance;
                    pq.add(new Node(next.x, nextDistance));
                }
            }
        }
        return distance;
    }

    private static double[] dijkstraForWolf() {
        double[][] distance = new double[N+1][2];
        for (double[] row: distance) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }

        distance[1][0] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(1, 0, 1));

        while (!pq.isEmpty()) {
            Node node = pq.poll();

            int now = node.x;
            double nowDistance = node.weight;
            int isRunnable = node.isRunnable;

            if (nowDistance > distance[now][1-isRunnable]) continue;

            for (Node next: graph.get(now)) {
                double nextDistance = isRunnable>0? nowDistance + next.weight / 2 : nowDistance + next.weight * 2;
                if (distance[next.x][isRunnable] > nextDistance) {
                    distance[next.x][isRunnable] = nextDistance;
                    pq.add(new Node(next.x, nextDistance, 1-isRunnable));
                }
            }
        }

        double[] res = new double[N+1];
        for (int i=0; i<=N; i++) {
            res[i] = Math.min(distance[i][0], distance[i][1]);
        }
        return res;
    }
}