// 시간 없어서 쉬운거 자바로 풀었음
// 스타트링크. bfs

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class bj_5014 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int F = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int G = Integer.parseInt(st.nextToken());
        int U = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());

        // S 층에서 G층으로 가야함
        // U만큼 위로 가거나, D만큼 아래로 가는 방법이 있음
        // 최대 F층임 (0층이나 F+1층에서 내리지 않음)

        int ans = bfs(S,G,U,D,F);
        System.out.println(ans==-1? "use the stairs": ans);

    }

    private static int bfs(int start, int end, int up, int down, int max) {

        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        // max 최대는 100만이라 visit를 만드는게 부담인 것 같지만, visit를 hashmap으로 사용하는 경우, 시간복잡도와 공간복잡도가 말도 안되게 튄다.
        // 배열: 81176kb, 204ms
        // 해시: 206556kb, 576ms
        int[] visit = new int[max+1];
        visit[start] = 1;
        while (!q.isEmpty()) {
            int now = q.poll();
            if (now == end) {
                return visit[now] - 1;
            }

            for (int i: new int[]{up, -down}) {
                int next = now+i;
                if (0 < next && next <= max) {
                    if (visit[next] == 0) {
                        visit[next] = visit[now] + 1;
                        q.add(next);
                    }
                }
            }
        }
        return -1;
    }
}
