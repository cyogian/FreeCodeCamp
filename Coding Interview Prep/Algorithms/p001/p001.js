// Find the Symmetric Difference
function bisym(A, B) {
  const res = [];
  A.map(e => {
    if (!B.includes(e) && !res.includes(e)) {
      res.push(e);
    }
  });
  B.map(e => {
    if (!A.includes(e) && !res.includes(e)) {
      res.push(e);
    }
  });
  return res;
}

function sym(...args) {
  return args.reduce((A, B) => bisym(A, B)).sort();
}

sym([1, 2, 3], [5, 2, 1, 4]);
