import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static class Node {
        char data;
        Node fail;
        Boolean isEnd = false;
        HashMap<Character, Node> children = new HashMap<>();

        public Node() {}
        public Node(char data) {
            this.data = data;
        }
    }

    static class Trie {
        Node root = new Node();

        public void insert(String word) {
            Node now = this.root;
            for (char c : word.toCharArray()) {
                now = now.children.computeIfAbsent(c, Node::new);
            }
            now.isEnd = true;
        }

        public void connect() {
            Queue<Node> q = new LinkedList<>();
            q.add(this.root);

            while (!q.isEmpty()) {
                Node now = q.poll();

                for (char c : now.children.keySet()) {
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

                        if (next.fail.isEnd) {
                            next.isEnd = true;
                        }
                    }
                    q.add(next);
                }
            }
        }

        public int search(String word) {
            Node now = this.root;
            int ans = 0;
            for (char c : word.toCharArray()) {
                while (now != this.root && !now.children.containsKey(c)) {
                    now = now.fail;
                }
                if (now.children.containsKey(c)) {
                    now = now.children.get(c);
                }

                if (now.isEnd) {
                    ans ++;
                }
            }
            return ans;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int tc = Integer.parseInt(st.nextToken());
        StringBuilder sb = new StringBuilder();

        for (int t = 0; t < tc; t++) {
            Trie trie = new Trie();
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            String word = br.readLine();
            String pattern = br.readLine();

            HashSet<String> patterns = createPatterns(pattern, M);
            for (String str : patterns) {
                trie.insert(str);
            }
            trie.connect();
            sb.append(trie.search(word)).append("\n");
        }
        System.out.println(sb);
    }

    public static HashSet<String> createPatterns(String pattern, int length) {
        HashSet<String> patterns = new HashSet<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < length; i++) {
            for (int j = i + 1; j <= length; j++) {
                sb.setLength(0);
                sb.append(pattern.substring(0, i))
                        .append(new StringBuilder(pattern.substring(i, j)).reverse())
                        .append(pattern.substring(j));
                patterns.add(sb.toString());
            }
        }

        return patterns;
    }
}
