/*
 * 10830 행렬 제곱
 * 
 * 분할 정복을 이용한 제곱 연산
 * 제곱 연산에 대한 분할 정복만 시행하면 되는듯 
 */



import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_10830 {

    static int N;
    static StringBuffer sb = new StringBuffer();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        long M = Long.parseLong(st.nextToken());
        int[][] arr = new int[N][N];

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] answer = divConq(arr,M);
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                sb.append(answer[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    private static int[][] divConq(int[][] arr, long M) {
        if (M==1) {
            for (int i=0; i<N; i++) {
                for (int j=0; j<N; j++) {
                    arr[i][j] %= 1000;
                }
            }
            return arr;
        }
        int[][] tmp = divConq(arr,M/2);

        if (M%2==1) {
            return multiply(multiply(tmp, tmp), arr);
        } else {
            return multiply(tmp,tmp);
        }
    }

    private static int[][] multiply(int[][] a, int[][] b) {
        int[][] res = new int[N][N];
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                for (int k=0; k<N; k++) {
                    res[i][j] += a[i][k] * b[k][j];
                }
                res[i][j] %= 1000;
            }
        }
        return res;
    }
}
