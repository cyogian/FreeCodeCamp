function rot13(str) {
  // LBH QVQ VG!
  let alpha = /[a-zA-Z]/;
  let newStr = "";
  for (let i in str) {
    if (alpha.test(str[i])) {
      let character = str[i].charCodeAt(0) + 13;
      if (character > 90) {
        character = 64 + (character - 90);
      }
      newStr += String.fromCharCode(character);
    } else {
      newStr += str[i];
    }
  }
  return newStr;
}

// Change the inputs below to test
rot13("SERR CVMMN!");
