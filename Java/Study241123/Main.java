import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int v = sc.nextInt();
        int v_minus = v-a;
        int day = v_minus/(a-b) + 1;
        if (v_minus%(a-b) != 0) day++;

        System.out.println(day);
        sc.close();
    }
}