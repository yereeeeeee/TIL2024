import java.util.*;
import java.io.*;

public class Main {
    static long n;
    static int p, q;
    static Map<Long, Long> map = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Long.parseLong(st.nextToken());
        p = Integer.parseInt(st.nextToken());
        q = Integer.parseInt(st.nextToken());

        System.out.println(get(n));
    }

    static long get(long k) {
        if (map.get(k) == null) put(k);
        return map.get(k);
    }

    static void put(long k) {
        // A[0] = 1
        if (k== 0L) map.put(0L, 1L);
        // A[k] = A[k / P] + A[k / Q]
        else map.put(k, get(k/p) + get(k/q));
    }
}