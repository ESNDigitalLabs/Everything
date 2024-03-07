// The default data type for prompt is string. Therefore, no data conversin is required
//let user = prompt("Enter your username: ");
 


//Use parseInt for numberic whole number with prompt to convert user input to integer data type
//let num1 = parseInt(prompt("Enter the first number: "));
//let num2 = parseInt(prompt("Enter the second number: "));
//let total = num1 + num2;
 


// Use parsefloat for decimal numbers with prompt to convert user input to decimal/float data type


//document.write(`Welcome ${user}`);
//document.write(`The answer to  ${num1}  + ${num2} = ${total}`);

// Task 1: follow the exampe above to use the parsefloat to convert to a float/decimal data type

let user = prompt("Enter your username: ");
let num1 = parseFloat(prompt("Enter the first number: "));
let num2 = parseFloat(prompt("Enter the second number: "));
let total = num1 + num2;
document.write(`Welcome ${user}`);
document.write(`</br>The answer to  ${num1}  + ${num2} = ${total}`);