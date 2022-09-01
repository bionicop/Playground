import java.util.Scanner;
public class calculator {
    public static void main(String[] args)
    {
        System.out.println("Welcome to c<a>l");
        int a, b;
        byte choice;
        Scanner grasp = new Scanner(System.in);
        do
        {
            System.out.println("\nEnter first number: ");
            a = grasp.nextInt();
            System.out.println("Enter second number: ");
            b = grasp.nextInt();
            System.out.println("What operaton would you like to perform? : ");
            System.out.println("\n 1 -> Addition \n 2 -> Subraction \n 3 -> Multiplication \n 4 -> Division \n 5 -> Modular Division");
            System.out.println("Enter your choice (Choose the corresponding Number OR Press 0 to exit): ");
            choice = grasp.nextByte();
            if(choice == 1)
            {
                System.out.println("The result is : " + (a+b));
            }
            else if(choice == 2)
            {
                System.out.println("The result is : " + (a-b));
            }
            else if(choice == 3)
            {
                System.out.println("The result is : " + (a*b));
            }
            else if(choice == 4)
            {
                System.out.println("The result is : " + (a/b));
            }
            else if(choice == 5)
            {
                System.out.println("The result is : " + (a%b));
            }  
        }while(choice != 0);
        grasp.close();
    }
}
