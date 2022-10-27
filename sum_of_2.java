import java.util.Scanner;

public class sum_of_2{
    public static void main(String[] args){
        int a,b,sum;
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Input 2 numbers: ");
        a = scan.nextInt();
        b = scan.nextInt();
        sum=a+b;

        System.out.println("\nSum: "+sum);
        scan.close();
    }
}