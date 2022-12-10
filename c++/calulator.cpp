#include <iostream>

int main()
{
    char optr;
    double num1, num2;

     std::cout << "Welcome to c<a>l" << "\n\n";
    do
    {
        // Taking Operator from the user: 
        std::cout << "enter the operator (+, -, *, /): ";
        std::cin >> optr;

        // Taking Operands from the user: 
        std::cout << "enter the 1st number: ";
        std::cin >> num1;
        std::cout << "enter the 2nd number: ";
        std::cin >> num2;

        // Now choosing the options: 
        if (optr == '+')
            std::cout << num1 + num2 << "\n\n";
        else if (optr == '-')
            std::cout << num1 - num2 << "\n\n";
        else if (optr == '*')
            std::cout << num1 * num2 << "\n\n";
        else if (optr == '/')
            std::cout << num1 / num2 << "\n\n";
        else
            std::cout << "Operator isn't valid (or maybe it will be in future update o.O stay connected...)" << "\n\n";

 
        std::cout << "Do you wish to continue (Y/N)? " << "\n\n";
        std::cin >> optr;
    } while (optr != 'N' && optr != 'n');

    return 0;
}