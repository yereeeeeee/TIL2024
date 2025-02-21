import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] S = br.readLine().toCharArray();
        char[] P = br.readLine().toCharArray();

        int answer = 0;
        int i = 0; // P에서 현재 탐색 중인 위치

        while (i < P.length) { // P를 모두 탐색할 때까지 반복
            boolean found = false;
            int maxLen = 0; // 최대 부분 문자열 길이 저장

            // S의 각 위치에서 시작하는 부분 문자열이 P의 i부터 어디까지 매칭되는지 찾음
            for (int j = 0; j < S.length; j++) {
                int len = 0; // 현재 매칭 길이
                while (i + len < P.length && j + len < S.length && P[i + len] == S[j + len]) {
                    len++; // 일치 길이 증가
                }
                maxLen = Math.max(maxLen, len); // 최대 매칭 길이 갱신
            }

            // 최대 일치 부분 문자열을 사용하여 P에서 처리한 부분을 건너뜀
            i += maxLen;
            answer++;
        }

        System.out.println(answer);
    }
}
