import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        //BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = sc.nextInt();
        for(int t = 0; t < T; t++) {
            long n = sc.nextLong();

        }

        sc.close();
        //bw.close();
        //br.close();
    }

    private static int findGCD(int a, int b) {
        if(b == 0) return a;
        return findGCD(b, a % b);
    }

}
