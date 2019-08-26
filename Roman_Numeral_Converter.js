function convertToRoman(num) {
  let thousands = Math.floor(num / 1000);
  let hundreds = Math.floor((num % 1000) / 100);
  let tens = Math.floor(((num % 1000) % 100) / 10);
  let ones = Math.floor(((num % 1000) % 100) % 10);
  let res = ""
  for(let i = 0; i < thousands; i++){
    res += "M";
  }
  if(hundreds == 9){
    res += "CM";
  }
  else if(hundreds >= 5){
    res += "D";
    for(let i = 0; i < hundreds - 5; i++){
      res += "C";
    }
  }
  else if(hundreds == 4){
    res += "CD";
  }
  else{
    for(let i = 0; i < hundreds; i++){
      res += "C";
    }
  }
  if(tens == 9){
    res += "XC";
  }
  else if(tens >= 5){
    res += "L";
    for(let i = 0; i < tens - 5; i++){
      res += "X";
    }
  }
  else if(tens == 4){
    res += "XL";
  }
  else{
    for(let i = 0; i < tens; i++){
      res += "X";
    }
  }
  if(ones == 9){
    res += "IX";
  }
  else if(ones >= 5){
    res += "V";
    for(let i = 0; i < ones - 5; i++){
      res += "I";
    }
  }
  else if(ones == 4){
    res += "IV";
  }
  else{
    for(let i = 0; i < ones; i++){
      res += "I";
    }
  }
  return res;
}

convertToRoman(36);
