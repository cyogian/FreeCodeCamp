    function checkCashRegister(price, cash, cid) {
      let change = cash - price;
      // Here is your change, ma'am.
      let converters = {
        "ONE HUNDRED": 100.00,
        TWENTY: 20.00,
        TEN: 10.00,
        FIVE: 5.00,    
        ONE: 1.00,    
        QUARTER: 0.25,    
        DIME: 0.10,
        NICKEL: 0.05,
        PENNY: 0.01       
      }
      let availables = {}
      let totalCid = 0;
      cid.map((x) => {
        totalCid += x[1];
        availables[x[0]] = x[1];
      })
      if(totalCid === change){
        return {status: "CLOSED", change: [...cid]};
      }
      else if(totalCid < change){
        return {status: "INSUFFICIENT_FUNDS", change: []};
      }
      else{
        let changeList = []
        for(let i in converters){
         if(availables[i] && change >= converters[i]){
           let deducted;
           if(change >= availables[i]){
             deducted = availables[i]
           }
           else{
             deducted = Math.trunc(change / converters[i]) * converters[i];
           }
           change -= deducted;
           availables[i] -= deducted;
           changeList.push([i, deducted])
           change = Math.round(change * 100) / 100
         }
       }
       if(change === 0){
         return {
           status : "OPEN",
           change : changeList
         }
       }
       else{
         return {
           status: "INSUFFICIENT_FUNDS",
           change: []
         }
       }
      }
    }

    // Example cash-in-drawer array:
    // [["PENNY", 1.01],
    // ["NICKEL", 2.05],
    // ["DIME", 3.1],
    // ["QUARTER", 4.25],
    // ["ONE", 90],
    // ["FIVE", 55],
    // ["TEN", 20],
    // ["TWENTY", 60],
    // ["ONE HUNDRED", 100]]

    checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]])


