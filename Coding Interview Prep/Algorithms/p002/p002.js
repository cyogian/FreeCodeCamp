// Inventory Update
function updateInventory(arr1, arr2) {
  // All inventory must be accounted for or you're fired!
  arr2.map(e => {
    const arr = arr1.find(arr => arr[1] === e[1]);
    if (arr) {
      arr[0] += e[0];
    } else {
      arr1.push(e);
    }
  });
  arr1.sort((a, b) => {
    if (a[1] < b[1]) return -1;
    if (a[1] > b[1]) return 1;
    return 0;
  });
  return arr1;
}

// Example inventory lists
var curInv = [
  [21, "Bowling Ball"],
  [2, "Dirty Sock"],
  [1, "Hair Pin"],
  [5, "Microphone"]
];

var newInv = [
  [2, "Hair Pin"],
  [3, "Half-Eaten Apple"],
  [67, "Bowling Ball"],
  [7, "Toothpaste"]
];

updateInventory(curInv, newInv);
