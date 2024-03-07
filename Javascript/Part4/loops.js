
/*
To explore loops and integrate them into your code
For Loop
While Loop
ForEach Loop
Do While Loop
*/

//for loop is use to iterate over an object for a specific number of times 


// ++ is the increment operator , where we place the increment operator impacts when the increment takes place
let num1 = 10;
document.write(` The value of num1 before the increment ${num1}</br>`);
 
// initial value + 1
num1++;
document.write(` The value of num1 after the increment ${num1}</br>`);
 
 
let num2 = 20;
num3 = ++num2;
 
document.write(` The value of num1 after the increment ${num3}</br>`);
 
// for Loop
// i = 0
// i = 1 ...2...3....4...5
for (let i = 0; i <21; i++){
    document.write(`</br> ${i}`)
}


// declare empty array
let multiplesOfTwo = [];
document.write(`</br>Empty array ${multiplesOfTwo}`);
 
 
for (let aNumber = 0; aNumber <25; aNumber++){
    // document.write(`</br> $i{i}`)
    if (aNumber % 2 === 0)
    {
        multiplesOfTwo.push(aNumber)
    }
 
};
document.write(`</br>Populated array ${multiplesOfTwo}`);
 
let people = ["Philip", "James", "Erica", "Fatinah", "Jason", "Johanna", "Sam"];
 
for (let aPerson in people){
    document.write(`</br>${people[aPerson]} `)
 
}

// aName = prompt("Enter a name to search ")
 
for (let findName in people){
    // document.write(`</br>${people[aPerson]} `)
    if(people[findName] === "Fatinah")
    // if(people[findName] === aName)
    {
        break;
    }
    document.write(`</br>The list is ends on ${people[findName]} name`)
 
};
  

// Task 1: Create an array of your favourite films / TV shows, up to 5 items.
//Use an array method to add 2 more items to your array.
//Use a loop to cycle through the array and log each item to the console/ browser.



// Task 2: Generate 10 random numbers between 1-100 and log them to the console/browser.

//While iterates/repeats until a condition is met


// Task 3: Create a loop that counts backwards from 20-0.



// ForEach method calls a function for each element in an array



// Do While run the loop first before checking for the condition

let films = ["Crash", "Top Gun", "Dirty Dancing", "The Story of Life", "Elf", "Spiderman", "Storyteller"];
films.push("Aquaman, Batman")
document.write(`</br>Films:</br> ${films}`);

// for (let i = 1; i <100; i++){
//     document.write(`</br> ${i}`)
// }

let randomNums = [];
document.write(`</br> Empty array ${randomNums}`);
 
for (let i = 0; i < 100; i++) {
  let randomNumber = Math.floor(Math.random() * 100) + 1;
  randomNums.push(randomNumber);
}
document.write(`<br/> Populated array: ${randomNums}`);

//let number = ["<= 20"];
document.write(`</br> `   );

//While iterates/repeats until a condition is met
//While loop
let number = 0;
 
while(number < 5){
    document.write(`</br>Number ${number}`)
    number++
};
 
let total = 0;
 
// ask for user input
let userNum = parseInt(prompt("Enter a number: "))
 
while(userNum >= 0){
    // add only positve numbers
    // total = total + userNum //total += userNum
    total += userNum
 
 
        // keep asking for user input if the number is positive
    userNum = parseInt(prompt("Enter a number: "))
 
}
document.write(`</br> The total is ${total} `);
 
// Do While run the loop first before checking for the condition
 
let number1 = 10;
let number2 = 11;
do{
    // body: will run at least once even if the condition is false/ not met
    document.write(`</br> This code will be executed at least once`)
}while(number1 > number2);
 
 
//let number1 = 10;
//let number2 = 11;
do{
    // body: will run at least once even if the condition is false/ not met
    document.write(`</br> This code will be executed at least once`)
    document.write(`</br> The value ${number1} is less than the value ${number2}`)
    number1++;
   
 
}while(number1 > number2);

// ForEach method calls a function for each element in an array
    document.write(`</br> ForEach method calls a function for each element in an array</br>`)
let peopleArray = ["Philip", "James", "Erica", "Fatinah", "Jason", "Johanna", "Sam", "Nikita"];
 
// using forEach
// theArrayObject.forEeach(somefunction)
peopleArray.forEach(names);
 
 
function names(aPerson){
    // display names of people in the array
    document.write(`</br> ${aPerson}</br>`)
}
peopleArray.forEach(usergreetings);
 
 
function usergreetings(aPerson, index, arrayObject){
    // display names of people in the array
    arrayObject[index] = "Hello "  + aPerson
    document.write(`</br> ${aPerson}</br>`)
}
 
let usersArray = ["Philip", "James", "Erica", "Fatinah", "Jason", "Johanna", "Sam", "Nikita"];
document.write(`</br> update </br>`)
usersArray.forEach(usergreetings);
 
 
function usergreetings(aPerson, index, arrayObject){
    // display names of people in the array
    arrayObject[index] = "</br> Hello "  + aPerson
 
}
document.write(`</br> ${usersArray}</br>`);

// Task 5:
// Review the for loop examples above and convert them to while, do While and forEach
 