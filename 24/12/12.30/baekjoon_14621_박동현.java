/*
 * 나만 안되는 연애
 * 
 * MST
 * 
 * 여-여, 남-남 으로 가는 모든 간선을 전처리 시점에 제외해버리면 그만인 문제
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
        int weight;

        public Node(int x, int weight) {
            this.x = x;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return this.weight - o.weight;
        }
    }

    static ArrayList<ArrayList<Node>> graph = new ArrayList<>();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        for (int i=0; i<=N; i++) {
            graph.add(new ArrayList<>());
        }
        
        String[] gender = new String[N+1];
        st = new StringTokenizer(br.readLine());
        for (int i=1; i<=N; i++) {
            gender[i] = st.nextToken();
        }

        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (gender[a].equals(gender[b])) continue;

            graph.get(a).add(new Node(b,c));
            graph.get(b).add(new Node(a,c));
        }

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(1,0));

        boolean[] visit = new boolean[N+1];
        Arrays.fill(visit, false);
        visit[0] = true;

        int ans = 0;
        while (!pq.isEmpty()) {
            Node now = pq.poll();

            if (visit[now.x]) continue;
            
            ans += now.weight;
            visit[now.x] = true;

            for (Node next: graph.get(now.x)) {
                pq.add(next);
            }
        }
        System.out.println(check(visit)? ans: -1);
    }

    static boolean check(boolean[] arr) {
        for (boolean b: arr) {
            if (!b) return false;
        }
        return true;
    }
}