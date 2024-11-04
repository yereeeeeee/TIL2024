import java.io.*;
import java.util.*;

public class Main {
    static int n = 0;
    static int s, t;
    static int[] arr;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        while ((n = sc.nextInt()) != 0) {
            s = sc.nextInt();
            t = sc.nextInt();

            arr = new int[n+1];
            dp = new int[t+1][n+1];
            int maxScore = Integer.MIN_VALUE;

            for (int i = 1; i <= n; i++) {
                arr[i] = sc.nextInt();
            }

            for (int i = 0; i <= t; i++) {
                Arrays.fill(dp[i], Integer.MIN_VALUE);
            }
            dp[0][0] = 0;

            PriorityQueue<Score> q = new PriorityQueue<Score>((a, b) -> a.time - b.time);
            q.add(new Score(0, 0, 0));

            while (!q.isEmpty()) {
                Score score = q.poll();
                if (dp[score.time][score.location] > score.value) {
                    continue;
                }

                if (score.time < t) {
                    for (int i = 1; i <= s; i++) {
                        int nextLocation = score.location + i;

                        // 별 못 먹을 때 답 갱신
                        if (nextLocation >= dp[score.time].length) {
                            maxScore = Math.max(maxScore, score.value);
                        } else if (dp[score.time + 1][nextLocation] < score.value + arr[nextLocation]) {
                            Score next = new Score(score.time + 1, nextLocation, score.value + arr[nextLocation]);

                            dp[next.time][next.location] = next.value;
                            q.add(next);
                        }
                    }
                }
            }
            System.out.println(maxScore);
        }
    }
}

class Score {
    int time, location, value;

    public Score(int time, int location, int value) {
        this.time = time;
        this.location = location;
        this.value = value;
    }
}
