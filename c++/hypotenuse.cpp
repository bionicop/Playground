// Hypotenuse calculator with user input
#include <iostream>
#include <cmath>

int main() {
  double a,b;
  
  // User input for side a & side b:
  std::cout << "Enter the length of the first side: ";
  std::cin >> a;
  std::cout << "Enter the length of the second side: ";
  std::cin >> b;

  // Hypotenuse Formula:
  double c = sqrt(a * a + b * b);

  std::cout << "Hypotenuse is: " << c;
  return 0;
}