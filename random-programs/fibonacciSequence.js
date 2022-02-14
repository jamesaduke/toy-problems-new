/**
 * Program to create a Fibonacci sequence of a given length.
 * input: array of 2 starting numbers, length of sequence
 * output: array of fibonacci numbers
 */

function fibonacciSequence(result, len) {
    let num1 = result[0];
    let num2 = result[1];
    let nextNum;

    while (result.length < len) {
        nextNum = num1 + num2;
        result.push(nextNum);
        num1 = num2;
        num2 = nextNum;
    }
}