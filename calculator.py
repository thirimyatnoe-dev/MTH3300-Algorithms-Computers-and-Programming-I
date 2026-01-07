
expression = input('Enter an expression: ')
symbols = expression.split()

operators =[]
numbers = []

# putting elements into separate lists
for s in symbols:  
    if s == '+' or s == '-' or s == '*' or s == '/':
        operators.append(s)
    else:
        numbers.append(float(s))

calculation = float(numbers[0]) # since there will be only 2 elements in the numbers as we go through the loop (if we want to add whatever is at the beginning first w/o considering the order of operations), I will just use index 0 here

for n in numbers:
    for o in operators:
        for i in range(len(numbers)):
            if o == '+':
                calculation += numbers[i+1]
                if i == 0: 
                    del numbers[i] #since the value of number[0] is now in the value of calculation, we don't want it to be added more than once, so delete it
                    break # putting break stops the i to increment  
            if o == '-':
                calculation -= numbers[i+1]
                if i == 0:
                    del numbers[i]
                    break
            if o == '*':
                calculation *= numbers[i+1] 
                if i == 0:
                    del numbers[i]
                    break
            if o == '/':
                if numbers[i+1] == 0:
                    print("Division by zero is not allowed")
                calculation /= numbers[i+1]
                if i == 0:
                    del numbers[i]
                    break
          
print (calculation)
