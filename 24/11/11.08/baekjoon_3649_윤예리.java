import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        try {
            while (true) {
                int x = Integer.parseInt(br.readLine()) * 10000000;
                int n = Integer.parseInt(br.readLine());
                int[] l = new int[n];

                for (int i = 0; i < n; i++) {
                    l[i] = Integer.parseInt(br.readLine());
                }

                Arrays.sort(l);

                int left = 0;
                int right = n-1;
                while (left < right) {
                    int sum = l[left] + l[right];

                    if (sum == x) {
                        break;
                    } else if (sum > x) {
                        right--;
                    } else {
                        left++;
                    }
                }

                if (left >= right) {
                    System.out.println("danger");
                } else {
                    System.out.println("yes" + " " + l[left] + " " + l[right]);
                }
            }
        } catch (Exception e) {
            System.out.println();
        }
    }
}