import java.util.Scanner;

public class max_of_3 {
    public static void main(String[] args) {
        int a,b,c;
        Scanner scan = new Scanner(System.in);

        System.out.println("Input number 1: ");
        a = scan.nextInt();
        System.out.println("Input number 2: ");
        b = scan.nextInt();
        System.out.println("Input number 3: ");
        c = scan.nextInt();

        if(a>b){ // this line checks wether 'a' is greater than 'b'.
            if(a>c){ // this line checks wether 'a' is also greater than 'c'.
                System.out.println("Max number is "+a);
            }else{System.out.println("Max number is "+c);}
        }else{
            if(b>c){ // this line checks wether 'b' is greater than 'c'.
                System.out.println("Max number is "+b);
            }else{
                System.out.println("Max number is "+c);
            }
        }

        scan.close();
    } 
}