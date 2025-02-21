/*
괄호의 값

스택

스택으로 해결할 수 있는 가장 기본적인 문제 형식
 */

 import java.io.BufferedReader;
 import java.io.InputStreamReader;
 import java.util.Stack;
 
 public class Main {
     public static void main(String[] args) throws Exception {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
         String s = br.readLine();
         Stack<Character> stack = new Stack<>();
         int tmp = 1;
         int ans = 0;
         for (int i=0; i<s.length(); i++) {
             char c = s.charAt(i);
 
             if (c == '(') {
                 stack.push(c);
                 tmp *= 2;
             }
             else if (c == ')') {
                 if (stack.isEmpty() || stack.peek() != '(') {
                     ans = 0;
                     break;
                 }
                 if (s.charAt(i-1) == '(') {
                     ans += tmp;
                 }
                 stack.pop();
                 tmp /= 2;
             }
             else if (c == '[') {
                 stack.push(c);
                 tmp *= 3;
             }
             else if (c == ']') {
                 if (stack.isEmpty() || stack.peek() != '[') {
                     ans = 0;
                     break;
                 }
                 if (s.charAt(i-1) == '[') {
                     ans += tmp;
                 }
                 stack.pop();
                 tmp /= 3;
             }
         }
         System.out.println(stack.isEmpty() ? ans: 0);
     }
 }