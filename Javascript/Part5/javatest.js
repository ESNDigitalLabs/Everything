//Task 1
// Write a new program which will create an array with 10 city names.
// •	Display the array in the browser/console with all the items/elements(cities)
// •	add a new city in index position 4 using splice() see example below.


let cities = ["London", "New York", "Amsterdam", "Bejing", "Barcelona", "Paris", "Bangkok", "Rome", "Mumbai", "Dublin"];
document.write(`Cities:</br> ${cities}`);
cities.splice(4,0, "Madrid");
document.write(`</br> New Cities </br> ${cities}`);


// •	Display/console log  the fourth item in the array by index position/value.
// •	Remove any two cities from the list, see example below


// let index = cities.indexOf(4);
document.write(`</br> The fourth city is :</br> ${cities[4]}`);

cities.splice(9,2);
document.write(`</br> Totally New Cities </br> ${cities}`);

// •	Return the length of the array
// •	Sort the Array in alphabetically order see example below

document.write(`</br> The number of Cities: ${cities.length}`);
cities.sort()
document.write(`</br> Cities alphabetically listed: ${cities}`);

//Task 2
// •	Display in the browser/console the 1st, 3rd, 6th, 9th and 11th characters from the string (userString) provided above.
// •	Return the length of the string.
// •	Slice the string to print between the 3rd and 11 characters.
// •	Display in the browser/console up to the 15th character from your string.
// •	Display in the browser/console all the characters in the user string in capital letters. 
// •	Display in the browser/console out the first letter of all the sub strings in capital letters. 
// •	Replace the substring “third” with a word of your choice.


let userString = " JavaScript is my first programming language";
document.write(`</br> ${userString}`);
document.write(`</br>Display the 1st character: ${userString[1]}`);
document.write(`</br>Display the 3rd character: ${userString[3]}`);
document.write(`</br>Display the 6th character: ${userString[6]}`);
document.write(`</br>Display the 9th character: ${userString[9]}`);
document.write(`</br>Display the 11th character: ${userString[11]}`);

userString.slice(3,11);
document.write(`</br> Display between the 3rd and 11 characters: ${userString,3,11}`);
document.write(`</br> Display in Capitals: ${userString.toUpperCase()}`);

userString.replace([3],"second");
// userString[3]="Toast"
document.write(`</br> New sentence:</br> ${userString}`);

// Task3 
// Write a program that will ask the user for how many sweets are in the bag.  
// •	It should also ask how many people the sweets should be shared between.  
// •	Use division to work out how many sweets each person should have and how many sweets would be left remaining.  
// •	For example, if there are 14 sweets in the bag and this was to be divided between 3 people then the programme should Display in the browser/console “There will be 4 sweets each and there would be 2 left over.”

let user = prompt("How many sweets are in the bag?: ");
let sweets = 14
document.write(`</br> There are ${sweets} sweets are in the bag? `)
prompt

let people = parseInt(prompt("How many people are you sharing with?:"));
let total = sweets / people
let left = sweets - total
document.write(`</br> That's ${total} and ${left}`)

for (let i = 0; i < newstring.length; i++) {    newstring[i] = newstring[i][0].toUpperCase() + newstring[i].substr(1);}

