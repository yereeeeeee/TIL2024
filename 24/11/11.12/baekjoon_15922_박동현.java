/*
 * 아우으 우아으이야!!
 * 
 * 스위핑
 * 스위핑 테크닉을 여기서 어떻게 써야될 지 모르겠어서 기본 정렬 그리디 방식으로 해결
 */


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj_15922 {

    static class Node implements Comparable<Node> {
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Node o) {
            if (o.x == this.x) {
                return this.y - o.y;
            } return this.x - o.x;
        }

        @Override
        public String toString() {
            return "(" + this.x + ", " + this.y + ")";
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        Node[] arr = new Node[N];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arr[i] = new Node(x,y);
        }

        Arrays.sort(arr);

        int ans = 0;
        int start = arr[0].x;
        int end = arr[0].y;
        for (int i=1; i<N; i++) {
            int s = arr[i].x;
            int e = arr[i].y;

            if (end < s) {
                ans += end-start;
                start = s;
            }
            end = Math.max(end,e);
        }

        ans += end-start;

        System.out.println(ans);
    }
}
