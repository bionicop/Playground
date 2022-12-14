#include <iostream>
#include <cstdlib>
#include <ctime>

// User Choice
char getUserChoice() {
  char choice;
  std::cout << "Enter R for rock, P for paper, or S for scissors: ";
  std::cin >> choice;

  if ((choice != 'R' && choice != 'r') && (choice != 'P' && choice != 'p') && (choice != 'S' && choice != 's')) {
    std::cout << "Invalid choice. Please enter R, P, or S." << "\n";
    return getUserChoice();
  }
  return choice;
}

// Generate's a Random Choice
char getComputerChoice() {
  char choices[] = {'R','P','S'};
  int randomIndex = rand() % 3;
  return choices[randomIndex];
}

// Convert choice into a String and Print's it
void showChoice(char choice) {
  choice = toupper(choice);

  switch (choice) {
  case 'R':
    std::cout << "Rock";
    break;
  case 'P':
    std::cout << "Paper";
    break;
  case 'S':
    std::cout << "Scissors";
    break;
  default:
    std::cout << "Choice ain't valid.";
    break;
  }
}

// WINNNERRRRRRRRR TIME!!!!!!
int chooseWinner(char userChoice, char computerChoice, int score) {
  userChoice = toupper(userChoice);
  computerChoice = toupper(computerChoice);

  if (userChoice == computerChoice) {
    std::cout << "It's a frickin~ TIEEEEEEEEEE!!!!" << "\n";
  } else if (userChoice == 'R' && computerChoice == 'S') {
    std::cout << "You WIN!!!! tHe RocK beats Scissors." << "\n";
    score++;
  } else if (userChoice == 'P' && computerChoice == 'R') {
    std::cout << "You WIN!!!! Paper beats tHe RocK." << "\n";
    score++;
  } else if (userChoice == 'S' && computerChoice == 'P') {
    std::cout << "You WIN!!!! Scissors beat paper or DOES iT?." << "\n";
    score++;
  } else {
    std::cout << "You LOOOOSe HAIYAA!!!!. Better luck next time :P." << "\n";
  }
  return score;
}

int main() {
  int score = 0, round = 3;
  std::cout << "=== Welcome to ReOCkleeee GAME ===\n\n";

  do {
    char userChoice = getUserChoice();
    char computerChoice = getComputerChoice();

    std::cout << "You chose ";
    showChoice(userChoice);
    std::cout << "\n";

    std::cout << "The computer chose ";
    showChoice(computerChoice);
    std::cout << "\n\n";
    score = chooseWinner(userChoice, computerChoice, score);
  } while (score < round);
  std::cout << "Your final score is " << score << "/" << round << "\n";

  return 0;
}