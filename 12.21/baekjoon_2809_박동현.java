/*
 * 아스키 커리
 * 
 * 아호-코라식
 * 
 * 최대 길이 5000인 패턴을 5000개 넣으면, 최대 2.5기가의 공간복잡도가 발생한다.
 * 이를 해소하기 위해 배치 처리를 도입하여 50개, 또는 100개씩 끊어서 처리하고
 * visit를 계산해 덮지 못하는 부분을 계산한다.
 * 
 * 배치 처리라는 개념이 미쳤네
 */


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class bj_2809 {

    static class Node {
        char key;
        HashMap<Character, Node> children;
        Node fail;
        int end = 0;

        // 일반 노드용
        public Node(char key) {
            this.key = key;
            this.children = new HashMap<>();
            this.fail = null;
        }
        // 루트 노드용
        public Node() {
            this.children = new HashMap<>();
            this.fail = this;
        }
    }

    static class AhoCorasick {
        Node root = new Node();

        public AhoCorasick() {
            this.root = new Node();
        }

        public void insert(String word) {
            Node now = this.root;

            for (char c: word.toCharArray()) {
                now = now.children.computeIfAbsent(c, Node::new);
            }
            now.end = word.length();
        }

        public void connect() {
            Queue<Node> q = new LinkedList<>();
            q.add(this.root);

            while (!q.isEmpty()) {
                Node now = q.poll();

                for (char c: now.children.keySet()) {
                    Node next = now.children.get(c);

                    if (now == this.root) {
                        next.fail = this.root;
                    } else {
                        Node dst = now.fail;

                        while (dst != this.root && !dst.children.containsKey(c)) {
                            dst = dst.fail;
                        }
                        if (dst.children.containsKey(c)) {
                            dst = dst.children.get(c);
                        }
                        next.fail = dst;
                        next.end = Math.max(next.end, next.fail.end);
                    }
                    q.offer(next);
                }
            }
        }

        public void search(String word) {
            Node now = this.root;

            for (int i=0; i<word.length(); i++) {
                char c = word.charAt(i);
                while (now != this.root && !now.children.containsKey(c)) {
                    now = now.fail;
                }

                if (now.children.containsKey(c)) {
                    now = now.children.get(c);
                }

                if (now.end != 0) {
                    int start = i - now.end + 1;
                    visit[start] = Math.max(visit[start], now.end);
                }
            }
        }
    }

    static int[] visit;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        visit = new int[N];

        String word = br.readLine();
        AhoCorasick ac = new AhoCorasick();
        int M = Integer.parseInt(br.readLine());
        for (int i=0; i<M; i++) {
            ac.insert(br.readLine());

            if (i%50 == 0) {
                ac.connect();
                ac.search(word);
                ac = new AhoCorasick();
            }
        }
        ac.connect();
        ac.search(word);

        int left = 0;
        Boolean[] ans = new Boolean[N];
        Arrays.fill(ans, false);
        for (int i=0; i<N; i++) {
            left = Math.max(left, visit[i]);

            if (left>0) {
                ans[i] = true;
            }
            left --;
        }

        int answer = 0;
        for (int i=0; i<N; i++) {
            if (!ans[i]) answer ++;
        }
        System.out.println(answer);
    }
}
