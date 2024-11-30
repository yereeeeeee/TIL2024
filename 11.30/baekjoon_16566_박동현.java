/*
 * 같은 로직의 자바코드는 무리 없이 통과함
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int M;
    static int[] cards;
    static boolean[] visit;
    static StringBuffer sb = new StringBuffer();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        cards = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<M; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(cards);

        visit = new boolean[M];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<K; i++) {
            sb.append(bisect(Integer.parseInt(st.nextToken()))).append("\n");
        }
        System.out.println(sb);
    }

    private static int bisect(int card) {
        int left = 0;
        int right = M-1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (card < cards[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        while (visit[left]) {
                left ++;
        }
        visit[left] = true;
        return cards[left];
    }
}
