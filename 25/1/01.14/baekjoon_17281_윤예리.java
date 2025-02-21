import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int[][] player;
    static boolean[] visited = new boolean[10];
    static boolean[] position; // 1루, 2루, 3루에 해당하는 선수 상태
    static int[] select = new int[10]; // 선수를 배치할 순서
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());  // 게임에 나오는 이닝 수
        player = new int[n + 1][10];  // n+1개의 이닝에 대해 10명 선수의 데이터를 저장

        StringTokenizer st;
        for (int i = 1; i <= n; i++) {  // 1번 이닝부터 n번 이닝까지 입력 받기
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j < 10; j++) {  // 1번 타자부터 9번 타자까지
                player[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 4번 타자는 반드시 1번 선수
        select[4] = 1;  // 4번 타자는 1번 선수로 고정
        search(2);  // 선수 배치 탐색 시작 (2번 타자부터 9번 타자까지 순열을 찾음)
        System.out.println(answer);  // 최고 점수 출력
    }

    // 선수 배치 조합을 구하는 함수
    static void search(int d) {
        if (d == 10) {  // 9명 선수를 배치했으면 경기를 진행
            play();
            return;
        }
        if (d == 4) {  // 4번 타자는 고정
            search(d + 1);
            return;
        }
        for (int i = 2; i < 10; i++) {  // 2번 타자부터 9번 타자까지 순회
            if (visited[i]) continue;
            visited[i] = true;
            select[d] = i;
            search(d + 1);
            visited[i] = false;
        }
    }

    // 경기를 진행하는 함수
    static void play() {
        int inning = 1;
        int curPlayer = 1;  // 1번 타자부터 시작
        int score = 0;
        while (inning <= n) {
            int out = 0;
            position = new boolean[4];  // 1루, 2루, 3루, 홈에 해당하는 선수 상태
            while (out < 3) {
                if (player[inning][select[curPlayer]] == 0) out++;  // 아웃 처리
                else score += move(player[inning][select[curPlayer]]);  // 점수 계산

                curPlayer = (curPlayer + 1) % 9;  // 타자 순서 변경 (9명이기 때문에 0~8로 순환)
            }
            inning++;  // 이닝 변경
        }
        answer = Math.max(score, answer);  // 최고 점수 갱신
    }

    // 선수의 타격 결과를 처리하는 함수
    static int move(int check) {
        int score = 0;
        // 각 타격 결과에 따라 주자들을 이동시키고 점수 계산
        if (check == 1) {  // 1루타
            if (position[3]) score++;  // 3루에 있던 선수 홈
            position[3] = position[2];
            position[2] = position[1];
            position[1] = position[0];
            position[0] = true;
        } else if (check == 2) {  // 2루타
            for (int i = 3; i >= 1; i--) {  // 뒤에서부터 순서대로 이동
                if (position[i]) {
                    score++;
                    position[i] = false;
                }
            }
            position[3] = position[0];
            position[2] = true;
            position[0] = false;
        } else if (check == 3) {  // 3루타
            for (int i = 3; i >= 1; i--) {
                if (position[i]) {
                    score++;
                    position[i] = false;
                }
            }
            position[3] = true;
        } else {  // 홈런
            for (int i = 0; i < 3; i++) {
                if (position[i]) {
                    score++;
                    position[i] = false;
                }
            }
            score++;  // 홈런 추가 점수
        }
        return score;
    }
}
