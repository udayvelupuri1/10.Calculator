from replit import clear
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2
  
operations = {"+":add,"-":sub,"*":multiply,"/":div}
def calculate():
  print(logo)
  calculateMore = False
  a = float(input("Enter first Number: "))
  while not calculateMore:
    for operator in operations:
      print(operator)
    b = input("Choose the operation:")
    c = float(input("enter another number to perform: "))
    calc = operations[b]
    res = calc(a,c)
    print(f"{a} {b} {c} = {res}")
    again = input("do you want to calculate from begining?  Yes/No?").lower()
    if again == "yes":
      a = res
    else:
      calculateMore = True
      clear()
      calculate()
calculate()
    
  
  
