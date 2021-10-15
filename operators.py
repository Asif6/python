# Add or + operator 
a=10
b=5

print(f"result=: {a+b}")

# Sub or - operator
print(f"The result is : {a-b}")

# Multiplication or * operator
print(f"The result is {a*b}")
print(f"The result is {a**b}") # a^b We use ** for Power Calculations
# Division or / 
print(f"The result is {a/b}")
print(f"The result is {123//10}") # Floor Division

# Modulus or % Operator

print(f"The result is {a%b}")

# Assignment operator or =
a=10
print(f"The result is {a}")
a+=10
print(f"The result is {a}")
a-=5
a*=2
a/=4
a%=2

# And operator 
a=10;b=20
if a==10 and b==20:
    print("OK")
else:
    print("Not Ok")
# Or operator (or)

if a==10 or b==20:
    print("OK")
else:
    print("Not OK")

# Not operator not

if a !=20:
    print("Ok")
else:
    print("Not OK")
if not a:
    print("YES")
else:
    print("NO")

# Greater Than  >
result=a>b
print(result)

# Less Than <

result=a<b
print(result)

# Greater Than or Equal To	>=
result=a>=b
print(result)

# Less Than or Equal To <=
result=a<=b
print(result)

# Equal To ==
result=a==b
print(result)

# Not Equal To !=
result=a!=b
print(result)

# Python Identity Operators is/is not 

a is b  #Returns True if both variables are the same object
x = ["apple", "banana"]
print("banana" in x)

a is not b #Returns True if both variables are not the same object

x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list


