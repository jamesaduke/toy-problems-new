const vowels = ['a', 'e', 'i', 'o', 'u'];
function encode(string) {
    return [...string].map(char => vowels.includes(char) ? vowels.indexOf(char)+1 : char).join('');

}
function decode(string) {
    return [...string].map(char => Number(char) ? vowels[Number(char)-1] : char).join('');
}