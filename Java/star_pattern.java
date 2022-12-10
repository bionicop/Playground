import java.util.Scanner;
public class star_pattern {
    public static void main(String[] args)
    {
        int a,b,x;
        
        Scanner sc = new Scanner(System.in);
        System.out.print("enter number of rows to print the '*': ");
        x = sc.nextInt();
        
        for (a=0; a<=x ; a++) // "a=0" , "a<=x" - a is smaller than or equal to x(rows), "a++" a will keep adding '*'
        {
            for (b=0; b<=a; b++) // "b=0" , "b<=a" - b is smaller than or equal to a('*'), "b++" a will keep adding '*'
            {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}