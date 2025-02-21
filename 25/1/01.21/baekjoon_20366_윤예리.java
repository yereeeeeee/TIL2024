import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        long answer = Long.MAX_VALUE;

        for (int i = 0; i < n - 3; i++) {
            for (int j = i + 3; j < n; j++) { // j는 항상 i + 3 이상이어야 함
                int left = i + 1;
                int right = j - 1;

                long target = arr[i] + arr[j]; // i와 j의 눈사람 높이 합

                while (left < right) {
                    long sum = arr[left] + arr[right]; // 나머지 두 눈사람 높이 합
                    answer = Math.min(answer, Math.abs(sum - target));

                    if (sum > target) {
                        right--; // 합이 크면 right를 왼쪽으로 이동
                    } else if (sum < target) {
                        left++; // 합이 작으면 left를 오른쪽으로 이동
                    } else {
                        // 최소 차이가 0이면 바로 종료
                        System.out.println(0);
                        return;
                    }
                }
            }
        }

        System.out.println(answer);
    }
}
