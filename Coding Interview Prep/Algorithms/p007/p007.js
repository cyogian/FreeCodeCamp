// Insertion Sort

function swap(i, j, arr) {
  let temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}

function insertionSort(array) {
  // change code below this line
  for (let i = 1; i < array.length; i++) {
    for (let j = i; j >= 0; j--) {
      if (array[j] < array[j - 1]) {
        swap(j, j - 1, array);
      }
    }
  }
  console.log(array);
  return array;
  // change code above this line
}

insertionSort([
  1,
  4,
  2,
  8,
  345,
  123,
  43,
  32,
  5643,
  63,
  123,
  43,
  2,
  55,
  1,
  234,
  92
]);
