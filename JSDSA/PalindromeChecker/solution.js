function palindrome(str) {
  // Good luck!
  str = str.toLowerCase().split(/[^a-zA-Z0-9]/).join("")
  console.log(str)
  let l = str.length
  for(let i = 0; i <= l/2; i++){
    if(str[i] !== str[l-1-i]){
      return false;
    }
  }
  return true;
}



palindrome("2A3*3a2");
