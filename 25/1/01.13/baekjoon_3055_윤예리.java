import java.util.*;
import java.io.*;

public class Main {
    static int r, c;
    static int[] dx = new int[]{-1, 0, 1, 0};
    static int[] dy = new int[]{0, 1, 0, -1};
    static String[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        arr = new String[r][c];
        Queue<Pos> waterQueue = new LinkedList<>();
        Queue<Pos> hedgehogQueue = new LinkedList<>();

        for (int i = 0; i < r; i++) {
            String line = br.readLine();
            for (int j = 0; j < c; j++) {
                arr[i][j] = String.valueOf(line.charAt(j));
                if (arr[i][j].equals("*")) {
                    waterQueue.offer(new Pos(i, j));
                } else if (arr[i][j].equals("S")) {
                    hedgehogQueue.offer(new Pos(i, j));
                }
            }
        }

        int time = 0;

        while (!hedgehogQueue.isEmpty()) {
            // 1. 물 확장
            int waterSize = waterQueue.size();
            for (int i = 0; i < waterSize; i++) {
                Pos cur = waterQueue.poll();
                for (int d = 0; d < 4; d++) {
                    int nx = cur.x + dx[d];
                    int ny = cur.y + dy[d];

                    if (nx < 0 || nx >= r || ny < 0 || ny >= c) {
                        continue;
                    }

                    if (arr[nx][ny].equals(".") || arr[nx][ny].equals("S")) {
                        arr[nx][ny] = "*";
                        waterQueue.offer(new Pos(nx, ny));
                    }
                }
            }

            // 2. 고슴도치 이동
            int hedgehogSize = hedgehogQueue.size();
            for (int i = 0; i < hedgehogSize; i++) {
                Pos cur = hedgehogQueue.poll();
                for (int d = 0; d < 4; d++) {
                    int nx = cur.x + dx[d];
                    int ny = cur.y + dy[d];

                    if (nx < 0 || nx >= r || ny < 0 || ny >= c) {
                        continue;
                    }

                    if (arr[nx][ny].equals("D")) {
                        System.out.println(time + 1);
                        return;
                    }

                    if (arr[nx][ny].equals(".")) {
                        arr[nx][ny] = "S";
                        hedgehogQueue.offer(new Pos(nx, ny));
                    }
                }
            }
            time++;
        }

        System.out.println("KAKTUS");
    }

    static class Pos {
        int x;
        int y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
