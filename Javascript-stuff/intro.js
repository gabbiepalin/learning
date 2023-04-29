const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });

// I make a variable to store my name in
let myName = "";
let hisName = "";

// I make a base integer variable to store ages
let myAge = "";
let hisAge = "";

readline.question('Who are you?', name_i_entered => {
    myName = name_i_entered;
    readline.close();
  });
readline.question('What is your age?', age_i_entered => {
    myAge = age_i_entered;
    readline.close();
})
console.log(myName);
console.log(myAge);