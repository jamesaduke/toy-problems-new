const twoSum = (nums, target) => {
    let vals =[];
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                vals.push(i);
                vals.push(j);
            }
        }
    }
    return vals;
}

let nums = [3,2 ,4];
let target = 7;

console.log(twoSum(nums, target));