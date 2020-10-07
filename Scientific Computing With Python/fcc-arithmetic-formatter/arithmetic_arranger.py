import re
reg = re.compile(r'([a-zA-Z0-9]+) ([\-\+\*\/]) ([a-zA-Z0-9]+)')
digit = re.compile(r'[0-9]+')
between = "    "
def arithmetic_arranger(problems, flag=False):
  if len(problems) > 5:
    return "Error: Too many problems."
  line_1 = line_2 = line_3 = line_4 = ""  
  for problem in problems:
      x = re.fullmatch(reg, problem)
      operand1 = x.group(1)
      operator = x.group(2)
      operand2 = x.group(3)
      result = None
      if operator == "+" or operator == "-":
        op1 = re.fullmatch(digit, operand1)
        op2 = re.fullmatch(digit, operand2)
        if op1 and op2:
          if len(operand1) <= 4 and len(operand2) <=4:
            if operator == "+":
              result = str(int(operand1) + int(operand2))
            else:
              result = str(int(operand1) - int(operand2))
            lop1 = len(operand1)
            lop2 = len(operand2)  
            longer = lop1 if lop1 >= lop2 else lop2
            line_1 += (2 + longer - lop1) * " " + operand1 + between
            line_2 += operator + " " + (longer - lop2) * " " + operand2 + between
            line_3 += (2 + longer) * "-" + between
            line_4 += (2 + longer - len(result)) * " " + result + between
          else:
            return "Error: Numbers cannot be more than four digits."
        else:
          return "Error: Numbers must only contain digits."
      else:
        return "Error: Operator must be '+' or '-'."
  line_1 = line_1[:-4] + "\n"
  line_2 = line_2[:-4] + "\n"
  line_3 = line_3[:-4]
  line_4 = "\n" + line_4[:-4]
  arranged_problems = line_1 + line_2 + line_3
  if flag:
    arranged_problems += line_4
  return arranged_problems