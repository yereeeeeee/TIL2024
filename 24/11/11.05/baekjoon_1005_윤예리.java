import java.io.*;
import java.util.*;

// 위상 정렬 알고리즘
public class Main {
    static int t, n, k, target;
    static List<List<Integer>> graph;
    static int[] times, inDegree, result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        t = Integer.parseInt(st.nextToken());
        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken()); 
            k = Integer.parseInt(st.nextToken()); 

            graph = new ArrayList<>();
            times = new int[n + 1];
            inDegree = new int[n + 1];
            result = new int[n + 1];

            for (int j = 0; j <= n; j++) {
                graph.add(new ArrayList<>());
            }

            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                times[j] = Integer.parseInt(st.nextToken());
            }

            for (int j = 0; j < k; j++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                graph.get(x).add(y);
                inDegree[y]++; // y의 진입 차수 증가
            }

            target = Integer.parseInt(br.readLine());

            int answer = topologicalSort();
            System.out.println(answer);
        }
    }

    public static int topologicalSort() {
        Queue<Integer> q = new LinkedList<>();

        // 진입 차수가 0인 노드를 큐에 추가하고 결과 배열 초기화
        for (int i = 1; i <= n; i++) {
            result[i] = times[i];
            if (inDegree[i] == 0) {
                q.offer(i);
            }
        }

        // 위상 정렬 수행
        while (!q.isEmpty()) {
            int node = q.poll();

            for (int neighbor : graph.get(node)) {
                inDegree[neighbor]--;
                // 현재 노드까지 걸린 시간을 더해서 최대 시간을 기록
                result[neighbor] = Math.max(result[neighbor], result[node] + times[neighbor]);

                if (inDegree[neighbor] == 0) {
                    q.offer(neighbor);
                }
            }
        }

        return result[target];
    }
}
