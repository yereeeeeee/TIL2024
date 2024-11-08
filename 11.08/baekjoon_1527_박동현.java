/*
* 1527 금민수의 개수
*
* 백트래킹
*
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class bj_1527 {

    // 최대 7,777,777,777 까지 올라갈 수 있으니 Integer 제한을 뚫는다.
    static ArrayList<Long> arr = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String N = st.nextToken();
        String M = st.nextToken();
        // 최대 사이즈를 구해서
        int size = Math.max(N.length(), M.length());
        // 백트래킹
        backtrack(size, "");

        int n = Integer.parseInt(N);
        int m = Integer.parseInt(M);

        int ans = 0;
        for (int i=0; i<arr.size(); i++) {
            // 조건에 해당하면 개수 추가
            if (n <= arr.get(i) && m >= arr.get(i)) {
                ans ++;
            }
        }
        System.out.println(ans);
    }
    // 백트래킹을 통해 4와 7만으로 이루어진 숫자 다 찾음
    private static void backtrack(int size, String res) {

        if (size == 0) return;

        for (String n: new String[] {"4","7"}) {
            backtrack(size - 1, res+n);
            arr.add(Long.parseLong(res+n));
        }
    }
}
