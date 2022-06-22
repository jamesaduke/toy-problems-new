/*
 * Programming Quiz: Inline Functions
 */

 /*
 * QUIZ REQUIREMENTS
 * - Your code should have an `emotions()` function
 * - Your code should call the `emotions()` function
 * - Your `emotions()` function call should have an inline function expression passed as the second parameter
 * - Your function expression should return the expected output
 */


// don't change this code
// emotions() function definition
function emotions(myString, myFunc) {
    console.log("I am " + myString + ", " + myFunc(2));
}



// your code goes here
// Call the emotions() function with two arguments""
emotions("enthusiast", function(number){
  	let laughString = ""
	for (i = 1; i <= number; i++){
    	laughString += "ha";
    }
  	return laughString + "!"
});
// Argument 1 - "happy" string
// Argument 2 - an inline function expression