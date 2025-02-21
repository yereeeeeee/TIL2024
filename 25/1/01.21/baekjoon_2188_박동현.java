import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int[] pairA;
    static int[] pairB;
    static int[] distance;
    static int N;
    static int M;
    static ArrayList<int[]> graph;
    public static void main(String[] args) throws Exception { 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();
        graph.add(new int[0]);
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int size = Integer.parseInt(st.nextToken());
            int[] tmp = new int[size];
            for (int j=0; j<size; j++) {
                tmp[j] = Integer.parseInt(st.nextToken());
            }
            graph.add(tmp);
        }

        pairA = new int[N+1];
        pairB = new int[M+1];
        distance = new int[N+1];
        int ans = 0;
        while (bfs()) {
            for (int i=1; i<=N; i++) {
                if (pairA[i] == 0 && dfs(i)) {
                    ans ++;
                }
            }
        }
        System.out.println(ans);
    }

    private static boolean bfs() {
        Queue<Integer> q = new LinkedList<>();
        for (int i=1; i<=N; i++) {
            if (pairA[i] != 0) {
                distance[i] = Integer.MAX_VALUE;
            } else {
                distance[i] = 0;
                q.add(i);
            }
        }
        distance[0] = Integer.MAX_VALUE;

        while (!q.isEmpty()) {
            int now = q.poll();

            if (distance[now] < distance[0]) {
                for (int nxt: graph.get(now)) {
                    if (distance[pairB[nxt]] == Integer.MAX_VALUE) {
                        distance[pairB[nxt]] = distance[now] + 1;
                        q.add(pairB[nxt]);
                    }
                }
            }
        }
        return distance[0] != Integer.MAX_VALUE;
    }

    private static boolean dfs(int now) {
        if (now != 0) {
            for (int nxt: graph.get(now)) {
                if (distance[pairB[nxt]] == distance[now] + 1 && dfs(pairB[nxt])) {
                    pairA[now] = nxt;
                    pairB[nxt] = now;
                    return true;
                }
            }
            distance[now] = Integer.MAX_VALUE;
            return false;
        }
        return true;
    }
}