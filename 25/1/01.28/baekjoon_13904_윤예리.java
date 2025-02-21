import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int max_day = 0;
        PriorityQueue<Work> pq = new PriorityQueue<>();
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            pq.add(new Work(d, w)); // 최대 힙으로 정렬
            max_day = Math.max(max_day, d);
        }

        Boolean[] visited = new Boolean[max_day + 1];
        Arrays.fill(visited, false); // visited 초기화
        int score = 0;

        while (!pq.isEmpty()) {
            Work cur = pq.poll(); // 우선순위 높은 작업을 꺼냄

            // 현재 작업의 마감일부터 가능한 가장 빠른 날짜에 작업 배정
            for (int i = cur.day; i > 0; i--) {
                if (!visited[i]) {
                    visited[i] = true; // 해당 날짜를 사용 처리
                    score += cur.weight; // 점수를 합산
                    break;
                }
            }
        }

        System.out.println(score);
    }

    static class Work implements Comparable<Work> {
        int day;
        int weight;

        public Work(int day, int weight) {
            this.day = day;
            this.weight = weight;
        }

        // 우선순위를 weight(점수) 기준으로 내림차순 정렬
        @Override
        public int compareTo(Work o) {
            return o.weight - this.weight; // 점수가 높은 순으로 정렬
        }
    }
}
