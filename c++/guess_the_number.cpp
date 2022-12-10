#include <iostream>
#include <cstdlib>  // for rand() and srand()
#include <ctime>    // for time()

int main() {
  srand(time(0)); // Help's in the generation of random numbers by seeding rand with a starting value. source: https://stackoverflow.com/questions/4736485/srandtime0-and-random-number-generation
  int score = 0, round = 3,tries = 0;
  std::cout << "=== Welcome to GUeSSSSSSSS GAME ===\n\n";

  do {
    int target = rand() % 11;

    std::cout << "GuesS the number between 0 - 10: ";
    int guess;
    std::cin >> guess;
    // Check's whether the player guess is correct or not.
    if (guess == target) {
      std::cout << "\nCoRRReakt!!! You guessed the right number.\n\n";
      score++;
    } else {
      std::cout << "\nare you serious right NEOW bro InCoRRReakt!!! the right number was " << target << ".\n\n";
    }
    tries++;
  } while (score < round);
  std::cout << "Your final score is " << score << "/"<< round << "\n";
  std::cout << "ANDDDDDDDDDDDDDDDDDDDDD It took you only " << tries << " tries to win the game.\n";
  std::cout << "Congratulations you have won!\n";

  return 0;
}