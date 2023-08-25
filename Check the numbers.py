def correct_input():
   numbers = (input("Enter numbers: "))
   num_list = list(numbers.split(","))
   num_int = [int(x) for x in num_list]  
   return num_int

a = correct_input()

while(all(x > 0 for x in a) != True):
   print("You need to change input!")
   a = correct_input()
else:
   print("all good!")