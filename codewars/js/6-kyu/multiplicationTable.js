multiplicationTable = function (n) {
    let results = []
    for(let i = 1; i <= n; i++)
    {
        const arrNums = Array(n) // create an array of size n
            .fill(1) // fill the array with 1
            .map((element, index) => (element + index) * i); // multiply each element in the array by the value of the row it is located
        results.push(arrNums);
    }

    return results;
}

console.log(multiplicationTable(3));