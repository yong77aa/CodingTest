package test.recursiveCall;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class recursion {
    static int n;

    public static void main(String[] args) throws Exception {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(bf.readLine());
        print(1);

    }

    public static void print(int num) {
        if (num <= n) {
            System.out.println(num);
            print(num + 1);

        }
    }
}