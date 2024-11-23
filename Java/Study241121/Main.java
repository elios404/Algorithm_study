import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char c = sc.next().charAt(0);
        System.out.println(c+0); // to print c as a number not as a character

        sc.close();
    }
}
