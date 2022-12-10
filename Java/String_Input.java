import java.util.Scanner;

public class String_Input{ 
    public static void main(String[] args){
    String a;
    
    Scanner input = new Scanner(System.in);
    System.out.print("Enter the magic line: ");
    a=input.nextLine();
    
    System.out.println("-> " + a);
    input.close();}
}