class Category:
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.balance -= amount
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category_object):
        if not self.check_funds(amount):
            return False
        self.balance -= amount
        self.ledger.append({
            "amount":
            -amount,
            "description":
            f'Transfer to {category_object.category_name}'
        })
        category_object.balance += amount
        category_object.ledger.append({
            "amount":
            amount,
            "description":
            f'Transfer from {self.category_name}'
        })
        return True

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True

    def __str__(self):
        output = self.category_name.center(30, "*")
        for each in self.ledger:
            line = "\n" + each["description"][:23].ljust(23) + "{:.2f}".format(
                each["amount"])[-7:].rjust(7)
            output += line
        output += "\nTotal: " + "{:.2f}".format(self.balance)
        return output

def round( n ):
    # Smaller multiple
    return (n // 10) * 10

def create_spend_chart(categories):
    output = "Percentage spent by category"
    lines = [
        "\n100|", "\n 90|", "\n 80|", "\n 70|", "\n 60|", "\n 50|", "\n 40|",
        "\n 30|", "\n 20|", "\n 10|", "\n  0|", "\n    "
    ]
    totalWithdrawCat = [cat.ledger[0]["amount"] - cat.get_balance() for cat in categories]
    totalWithdraw = sum(totalWithdrawCat)
    totalLength = 0
    for i in range(len(categories)):
      if totalLength < len(categories[i].category_name):
        totalLength = len(categories[i].category_name)
      percent = round((totalWithdrawCat[i] / totalWithdraw) * 100)
      lines[0] += " o " if percent >= 100 else "   "
      lines[1] += " o " if percent >= 90 else "   "
      lines[2] += " o " if percent >= 80 else "   "
      lines[3] += " o " if percent >= 70 else "   "
      lines[4] += " o " if percent >= 60 else "   "
      lines[5] += " o " if percent >= 50 else "   "
      lines[6] += " o " if percent >= 40 else "   "
      lines[7] += " o " if percent >= 30 else "   "
      lines[8] += " o " if percent >= 20 else "   "
      lines[9] += " o " if percent >= 10 else "   "
      lines[10] += " o " if percent >= 0 else "   "
      lines[11] += "---"
      for j in range(len(categories[i].category_name)):
        if len(lines) < j + 13:
          lines.append(f'\n    {i * "   "} {categories[i].category_name[j]} ')
        else:
          lines[j + 12] += f' {categories[i].category_name[j]} '
      for j in range(len(categories[i].category_name), totalLength):
        lines[j + 12] += "   "
    for i in range(11):
      lines[i] += " "
    lines[11] += "-"
    for i in range(12, len(lines)):
      lines[i] += " "
    for line in lines:
      output += line
    print(output)
    return output