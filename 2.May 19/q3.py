condition = None;
product = 1
int_sum = 0
count = 0

while condition != 'q':
  input_value = input('Please enter an integer = ')
  condition = input("if you want to quit, type 'q' or else type anything else = ")
  input_int = int(input_value)

  product *= input_int
  int_sum += input_int
  count += 1
  
  if condition == 'q': 
    avg = int_sum/count

print('average = ', avg)
print('product = ', product)


