import java.util.*;
import java.io.*;

public class Main {
    static Map<Character, Character> toggle = new HashMap<>();
    static int n;
    static char[] state, result;

    public static void main(String[] args) throws IOException {
        // 1 -> 0, 0 -> 1
        toggle.put('1', '0');
        toggle.put('0', '1');

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        state = br.readLine().toCharArray();
        result = br.readLine().toCharArray();

        // 첫 번째 스위치를 누르지 않고 시작
        char[] case1 = Arrays.copyOf(state, state.length);
        // 첫 번째 스위치를 누르고 시작
        char[] case2 = Arrays.copyOf(state, state.length);
        case2[0] = toggle.get(case2[0]);
        case2[1] = toggle.get(case2[1]);

        int ans = Math.min(swit(case1, 0), swit(case2, 1));

        if (ans == 100001) {
            System.out.println(-1);
        } else {
            System.out.println(ans);
        }
    }

    static int swit(char[] bulb, int cnt) {
        for (int i = 1; i < n; i++) {
            // 앞선 상태가 목표와 다르면 스위치를 눌러야 한다.
            if (bulb[i - 1] != result[i - 1]) {
                cnt++;
                // 스위치를 눌러서 변화시키기
                bulb[i - 1] = toggle.get(bulb[i - 1]);
                bulb[i] = toggle.get(bulb[i]);
                if (i < n - 1) {
                    bulb[i + 1] = toggle.get(bulb[i + 1]);
                }
            }
        }

        // 마지막 상태가 목표 상태와 일치하는지 확인
        if (bulb[n - 1] == result[n - 1]) {
            return cnt;
        }
        return 100001; // 실패
    }
}
