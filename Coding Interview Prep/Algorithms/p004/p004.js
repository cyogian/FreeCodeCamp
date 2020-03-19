// Pairwise
function pairwise(arr, arg) {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if ((arr[i] !== "$" || arr[j] !== "$") && arr[i] + arr[j] === arg) {
        result.push(i + j);
        arr[i] = "$";
        arr[j] = "$";
      }
    }
  }
  result = result.reduce((a, b) => a + b, 0);
  console.log(result);
  return result;
}
pairwise([1, 4, 2, 3, 0, 5], 7);
