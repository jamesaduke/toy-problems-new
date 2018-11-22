// An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

// isIsogram( "Dermatoglyphics" ) == true
// isIsogram( "aba" ) == false
// isIsogram( "moOse" ) == false // -- ignore letter case

function isogram(str){
    //...
    if (typeof str === undefined){
        return true;
    }
    var passing = true;
 
    //   lowercase
    var strLower = str.toLowerCase();
    var counts = {};
 
    for (i = 0; i <= strLower.length; i++) {
        var letter = strLower.charAt(i);
        if(counts[letter]) {
            counts[letter] = 1 + counts[letter]
        } else {
            counts[letter] = 1;
        }
        if(counts[letter] > 1) {
            return passing = false;
        }

    }
    return passing
}
