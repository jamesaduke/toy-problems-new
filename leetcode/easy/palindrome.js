/**
 * @param {number} x
 * @return {boolean}
 */

const isPalindrome = function(x) {
    // Implement the soulution without converting to string (Number based reversal)
    /**
     * Check if the number is less than zero
     * If the number is less than zero return false
     * Initialize a variable temp with X(because we lose the initial value of x in the logic)
     * Initialize the reverse variable with zero
     * Loop over the number and check if the number is divisible by 10
     * If the number is divisible by 10 then divide the number by 10 and add the remainder to the reverse variable
     * If the number is not divisible by 10 then add the number to the reverse variable
     * Check if the reverse variable is equal to the temp variable
     * If the reverse variable is equal to the temp variable then return true
     * If the reverse variable is not equal to the temp variable then return false
     */

    if(x < 0) return false;

    const temp = x;
    let reverse = 0;

    while(x > 0) {
        reverse = (x % 10) + (reverse * 10);
        x = Math.floor(x / 10);
    }
    return reverse === temp;

}
console.log(isPalindrome(123));

// Two pointer method

/**
 *In this solution, we will take care of some of the simple cases before writing out logic.
 Once those are taken care of, we will follow the two-pointer method to check if the number is a palindrome.

The idea is, we will take one digit from the start, and another from the last.
Check if both are equal if not, the number is not a palindrome.
 */

const isPalindromeTwoPointer = x => {
    if (x < 0) return false;

    if (x < 10) return true;

    if (x % 10 == 0 && x !== 0){
        return false;
    }

    const str = String(x);
    let i = 0, j = str.length - 1;

    while (i < j ) {
        if(str[i] !== str[j]) return false;

        i++;
        j--;
    }
    return true;

}

console.log(isPalindromeTwoPointer(123));
