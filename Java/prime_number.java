import java.util.Scanner;

public class prime_number {
    public static void main(String[] args) {
        int n,div;
        Scanner scan = new Scanner(System.in);

        System.out.println("Input the numver: ");
        n = scan.nextInt();
        div = 2;
        
        while(div < n){
                if(n%div == 0){
                    System.out.println("\nNot a prime number.");
                    break;
                }else{div = div + 1;}
        }if(n == div){
            System.out.println("\nPrime number!");
        }

        scan.close();
    }
}