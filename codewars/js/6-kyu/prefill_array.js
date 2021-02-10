
function prefill(n, v) {
    if (n === '0' || n === 0) return [] ;
    if(!Number.isInteger(n) || n < 0 ){
//     when using parseInt on a float it would return RangeError hennce the use of Number.isInteger
        let typeError = new TypeError();
        typeError.name = "TypeError";
        typeError.message =  `${n} is invalid`;
        throw typeError
    }

    // create new array of n elements to fill with value v
    return new Array(n).fill(v);
}
//better solution
function prefill2(n,v){

    if (parseInt(n) !== Math.abs(n)) throw new TypeError(`${n} is invalid`);
    return +n ? Array(n).fill(v) : [];
}


prefill('1',1)
prefill(3,1)