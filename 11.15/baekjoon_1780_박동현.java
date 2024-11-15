/*
 * 종이의 개수
 * 
 * 분할 정복
 */



import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_1780 {

    static int[][] arr;
    static int[] answer = new int[3];
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        arr = new int[N][N];

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        getPapers(N, 0, 0);

        for (int ans: answer) {
            System.out.println(ans);
        }

    }

    private static void getPapers(int num, int x, int y) {
        int now = arr[x][y];

        for (int i=x; i<x+num; i++) {
            for (int j=y; j<y+num; j++) {
                if (arr[i][j] != now) {

                    int next = num / 3;
                    // 분할정복
                    for (int k=x; k<x+num; k+=next) {
                        for (int l=y; l<y+num; l+=next) {
                            getPapers(next, k, l);
                        }
                    }
                    return;
                }
            }
        }
        answer[now+1] ++;
    }
}
