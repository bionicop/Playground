import java.util.Scanner;

public class SI {
    public static void main(String[] args) {
        int P,R,T,SI;
        Scanner scan = new Scanner(System.in);

        System.out.println("Input the Principal: ");
        P = scan.nextInt();
        System.out.println("Input the Rate: ");
        R = scan.nextInt();
        System.out.println("Input the Time: ");
        T = scan.nextInt();

        SI = (P*R*T)/100;

        System.out.println("\nSimple Interest: "+SI);
        scan.close();
    }    
}
