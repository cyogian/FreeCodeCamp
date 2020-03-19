// No Repeats please!

function swap(index1, index2, arr) {
  let tmp;
  tmp = arr[index1];
  arr[index1] = arr[index2];
  arr[index2] = tmp;
}
// check if characters repeat in string
function checkRepeats(str) {
  let exp = /(\w)\1+/g;
  return !exp.test(str);
}

function generate(n, arr, result) {
  if (n == 1) {
    // output(A)
    result.push(arr.join(""));
  } else {
    let i = 0;
    do {
      generate(n - 1, arr, result);
      if (n % 2 === 0) {
        swap(i, n - 1, arr);
      } else {
        swap(0, n - 1, arr);
      }
      i++;
    } while (i < n);
  }
}

function permAlone(str) {
  const inputArr = str.split("");
  const result = [];
  generate(inputArr.length, inputArr, result);
  return result.filter(checkRepeats).length;
}

permAlone("aab");
