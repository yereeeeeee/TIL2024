/* 고냥이
 * 
 * 투 포인터
 * 
 * 포인터를 정해 해시맵에 값을 저장하면서, size를 체크하며 조건 분기를 정함 
 */

 import java.io.BufferedReader;
 import java.io.InputStreamReader;
 import java.util.HashMap;
 
 public class Main {
 
     public static void main(String[] args) throws Exception {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
         int N = Integer.parseInt(br.readLine());
         String word = br.readLine();
         HashMap<Character, Integer> data = new HashMap<>();
         
         int ans = 0;
         int left = 0;
         int right = 0;
         while (right < word.length()) {
             char rightChar = word.charAt(right);
             if (data.size() < N || data.containsKey(rightChar)) {
                 data.put(rightChar, data.getOrDefault(rightChar, 0) + 1);
                 right ++;
                 ans = Math.max(ans, right-left);
             } else {
                 char leftChar = word.charAt(left);
                 data.put(leftChar, data.get(leftChar) - 1);
                 if (data.get(leftChar) == 0) {
                     data.remove(leftChar);
                 }
                 left ++;
             }
         }
         System.out.println(ans);
     }
 }