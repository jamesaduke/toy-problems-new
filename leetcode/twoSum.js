// const twoSum = (nums, target) => {
//     let vals =[];
//     for (let i = 0; i < nums.length; i++) {
//         for (let j = i + 1; j < nums.length; j++) {
//             if (nums[i] + nums[j] === target) {
//                 vals.push(i);
//                 vals.push(j);
//             }
//         }
//     }
//     return vals;
// }

// oprimized solutions still not getting it 🕵🏿‍♀️

var twoSum = function(nums, target) {
    const indicies = {}

    for (let i = 0; i < nums.length; i++) {
      const num = nums[i]
      if (indicies[target - num] != null) {
        console.log(indicies);
        return [indicies[target - num], i]
      }
      indicies[num] = i
    }
  };

let nums = [3,2 ,4];
let target = 7;

console.log(twoSum(nums, target));