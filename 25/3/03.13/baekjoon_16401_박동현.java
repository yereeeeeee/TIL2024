import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] arr = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<M; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        int left=0, right=arr[arr.length-1] +1, ans=0, mid;
        while (left <= right) {
            mid = (left + right) / 2;
            if (check(N, mid, arr)) {
                left = mid + 1;
                ans = mid;
            } else {
                right = mid - 1;
            }
        }
        System.out.println(ans);
    }

    private static boolean check(int x, int length, int[] arr) {
        if (length == 0) {
            return true;
        }
        for (int i=arr.length-1; i>=0; i--) {
            x -= arr[i] / length;
            if (x <= 0) {
                return true;
            }
        }
        return false;
    }
}