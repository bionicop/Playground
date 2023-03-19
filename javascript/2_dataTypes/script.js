/* Data Types
        Primitive Data Types:
            1. String
            2. Number
            3. Boolean
            4. Null
            5. Undefined
            6. Symbol
            7. BigInt
        Reference Types:
            1. Objects
            2. Literals
            3. Arrays
            4. Functions
    
*/

// Primitive Data Types
console.group('Primitive Data Types');
const firstName = 'Joji';
const age = 25;
const singer = true;
const a = null;
const b = undefined;
const id = Symbol('id');
const numb = 987654321123456789n;

console.log(firstName, typeof firstName,'\n\n', age, typeof age, '\n\n', singer, typeof singer, '\n\n', a, typeof a, '\n\n', b, typeof b, '\n\n', id, typeof id, '\n\n', numb, typeof numb);
console.groupEnd();

// Reference Types
console.group('Reference Types');
const num = [1, 2, 3, 4];
const person = {
    name: 'Joe',
};
function ahayo(){
    console.log('Wassup ' + person.name);
}

console.log(num, typeof num);
console.log(person, typeof person);
console.log( ahayo, typeof ahayo);
console.groupEnd();