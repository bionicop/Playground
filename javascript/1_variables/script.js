/* Variables can be declared in following ways:
        1. var
        2. let
        3. const

    Variables Naming Conventions:
        1. Only letters, numbers, underscores & dollar signs.
        2. Can not start with numbers.

    Multi-Word Formatting:
        1. firstName : camelCase
        2. FirstName : PascalCase
        3. firstname : lowercase
        4. first_name : underscore
    
*/

let firstName = 'Deez';
let lastName = 'Nuts';

console.log(firstName, lastName, age);

var age = 21;
console.log(age);


let score;
score = 1;
console.log(score);


const arr = [1, 2, 3, 4];
arr.push(5);
console.log(arr);

const person = {
    firstName: 'neon',
};
person.firstName = 'O.o';
person.lastName = 'o.O';
console.log(person);