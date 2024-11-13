/*
가장 긴 증가하는 부분 수열 4
DP, 역추적
 */


 import java.io.BufferedReader;
 import java.io.InputStreamReader;
 import java.util.StringTokenizer;
 
 public class bj_14002 {
  
     static StringBuffer sb = new StringBuffer();
     public static void main(String[] args) throws Exception {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         StringTokenizer st = new StringTokenizer(br.readLine());
 
         int N = Integer.parseInt(st.nextToken());
 
         int[] arr = new int[N+1];
         st = new StringTokenizer(br.readLine());
         for (int i=1; i<=N; i++) {
             arr[i] = Integer.parseInt(st.nextToken());
         }
 
         int[] DP = new int[N+1];
         for (int i=0; i<=N; i++) {
             for (int j=0; j<i; j++) {
                 if (arr[i] > arr[j]) {
                     DP[i] = Math.max(DP[i], DP[j]+1);
                 }
             }
         }

         int res = 0;
         int now = Integer.MAX_VALUE;
         for (int i=0; i<=N; i++) {
             res = Math.max(DP[i], res);
         }

         sb.append(res).append("\n");

         int[] ans = new int[res];
         int tmp = 0;
         for (int i=N; i>0; i--) {
             if (res == DP[i] && now > arr[i]) {
                 ans[tmp] = arr[i];
                 tmp ++;
                 res --;
                 now = arr[i];
             }
         }

         for (int i=ans.length-1; i>=0; i--) {
             sb.append(ans[i]).append(" ");
         }

         System.out.println(sb);
     }
 }
 