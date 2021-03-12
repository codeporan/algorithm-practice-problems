// Solution-1-Brute Force — O(n²)
// https://levelup.gitconnected.com/how-to-solve-two-sum-in-javascript-d1ebd9dfd3d3
// https://paulrohan.medium.com/solving-the-classic-two-sum-and-three-sum-problem-in-javascript-7d5d1d47db03

const twoSum = (arr, target) => {
  var result = [];

  for (var i = 0; i < arr.length; i++) {
    for (var j = i + 1; j < arr.length; j++) {
      if (arr[i] + arr[j] === target) {
        result.push(arr[i]);
        result.push(arr[j]);
      }
    }
  }
  return result;
};

console.log("Brute Force:", twoSum([2, 7, 15], 17));

const twoSum_On_Better = (arr, target) => {
  let numObject = {};
  for (let i = 0; i < arr.length; i++) {
    let thisNum = arr[i];
    numObject[thisNum] = i;
  }

  for (var i = 0; i < arr.length; i++) {
    let diff = target - arr[i];
    if (numObject.hasOwnProperty(diff) && numObject[diff] !== i) {
      return [i, numObject[diff]];
    }
  }
};
console.log("Hashing:", twoSum_On_Better([2, 7, 11, 15], 17));

