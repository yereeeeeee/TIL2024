/*
 * 인간-컴퓨터 상호작용
 * 
 * 누적합
 * 
 * 각 철자별로 누적합을 계산해두고, 
 * 이를 사용하여 출력한다.
 */

 import java.io.BufferedReader;
 import java.io.InputStreamReader;
 import java.util.StringTokenizer;
 
 public class Main {
 
     static int[][] prefixSum;
     static StringBuffer sb = new StringBuffer();
     public static void main(String[] args) throws Exception {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         StringTokenizer st;
         String word = br.readLine();
 
         prefixSum = createPrefixSum(word);
 
         int N = Integer.parseInt(br.readLine());
 
         for (int i=0; i<N; i++) {
             st = new StringTokenizer(br.readLine());
             char c = st.nextToken().charAt(0);
             int s = Integer.parseInt(st.nextToken());
             int e = Integer.parseInt(st.nextToken());
 
             sb.append(find(c,s,e)).append("\n");
         }
         System.out.println(sb);
     }
 
     static int ord(char c) {
         return c - 'a';
     }
 
     static int[][] createPrefixSum(String word) {
         int[][] res = new int[26][word.length()+1];
         for (int i=0; i<26; i++) {
             for (int j=1; j<=word.length(); j++) {
                 if (ord(word.charAt(j-1)) == i) {
                     res[i][j] = res[i][j-1] + 1;
                 } else {
                     res[i][j] = res[i][j-1];
                 }
             }
         }
         return res;
     }
 
     static int find(char c, int s, int e) {
         return prefixSum[ord(c)][e+1] - prefixSum[ord(c)][s];
     }
 }