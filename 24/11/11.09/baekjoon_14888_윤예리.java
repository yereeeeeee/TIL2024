import java.io.*;
import java.util.*;

public class baekjoon_14888_윤예리 {
    static int n;
    static int[] arr;
    static int[] nums = new int[4]; // 덧셈, 뺄셈, 곱셈, 나눗셈
    static int max_answer = Integer.MIN_VALUE;
    static int min_answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        backtracking(1, arr[0]);

        System.out.println(max_answer);
        System.out.println(min_answer);
    }

    public static void backtracking(int idx, int tmp) {
        if (idx == n) {
            max_answer = Math.max(max_answer, tmp);
            min_answer = Math.min(min_answer, tmp);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (nums[i] > 0) {
                nums[i] -= 1;
                if (i == 0) {
                    backtracking(idx + 1,tmp + arr[idx]);
                }
                else if (i == 1) {
                    backtracking(idx + 1,tmp - arr[idx]);
                }
                else if (i == 2) {
                    backtracking(idx + 1,tmp * arr[idx]);
                }
                else {
                    backtracking(idx + 1, tmp / arr[idx]);
                }
                nums[i] += 1;
            }
        }
    }

}
