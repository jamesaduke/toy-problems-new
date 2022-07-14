// create a function called buildTriangle() that will accept an input (the triangle at its widest width) and will return the string representation of a triangle. See the example output below.

// buildTriangle(10);

// Returns:

// *
// * *
// * * *
// * * * *
// * * * * *
// * * * * * *
// * * * * * * *
// * * * * * * * *
// * * * * * * * * *
// * * * * * * * * * *

function makeLine(lineSize) {
    let line = "";
    for (let i = 0; i < lineSize; i++) {
        line += "*";
    }
    return line + "\n"
}

function buildTriangle(triangleSize){
    let triangle = "";
    for (i = 0; i <= triangleSize; i++) {
        triangle += makeLine(i);
    }

    return triangle;

}
console.log(buildTriangle(10));