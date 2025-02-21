import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] chars = br.readLine().toCharArray();

        int P = 0;
        int K = 0;

        for (char c: chars) {
            if (c == 'P') {
                if (K > 0) K--;
                P++;
            } else {
                if (P > 0) P--;
                K++;
            }
        }
        System.out.println(P+K);
    }
}