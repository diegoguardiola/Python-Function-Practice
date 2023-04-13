# A function named hello() 
def hello():
  print("Hello, user!")
  
# A function named pack() that accepts three arguments and returns a list with the three arguments inside as list elements.

def pack(a,b,c):
  return [a,b,c]

# A function called eat_lunch() That accepts a list of any length, and print out a series of strings that say "First I eat __" 
# (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". 

def eat_lunch(lunch_list):
  if len(lunch_list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(lunch_list)):
      if i == 0:
        print(f"First I eat {lunch_list[0]}")
      else:
        print(f"Next I eat {lunch_list[i]}")

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])