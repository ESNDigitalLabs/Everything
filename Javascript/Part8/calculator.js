// Basic Calculator - 
//an example to how we can link functions to HTML elements and get user input values

// sumUp will take 2 values and add them together
function sumUp(valueOne, valueTwo) {
    //convert strings to numbers and add together  
    return Number(valueOne) + Number(valueTwo); // convert string value to a number value
  };
 
  // define some basic variables we need for the calculate function
  const operator = document.getElementById('container calculator') // operation
  const numberOne = document.getElementById('numberone') //INPUT 1
  const numberTwo = document.getElementById('numbertwo') //INPUT 2
  const result = document.getElementById('result') //Output
  
  //Calculate - the fuction that brings it all together
  //Task: Fix the basic calculator sheets so that it's working. 20 mins --> 10am

  function calculate(){
    //sum calls the sumUP function and valueOne and valueTwo are provided inside brackets
    let sum = sumUp(numberOne.value, numberTwo.value);
    // numberOne.value = will get the input from the user for that box (2, 67, 890)
    result.value = sum.toString();
    //result is converted to a string and applied to the value property of our result input
  };/**/


  let test = document.getElementById('multi');
  console.log(test.value);



//Multi-Arithmetic Calc considerations:- How can the user choose their operation?Option to select the operation

//Maths Funcions:-

//add
//subtract
//multiply
//divide
   
//How does the calculating function know which operation is chosen? 
//If else or switch statement which checks operator value
   
 // - Are all the operations supported arithmetically?  All the operators have arithmetic code to support them
   
 // - Does our calculating function need any information fed to it?
 // Fed with the operations (select) value. has context menu
  //Compose

  // Challenge
// Create a concept/system where it takes user inputs and feeds back a diferent background color,
// depending on the values provided.
// Use DOM, Events and Interactions to achieve this.