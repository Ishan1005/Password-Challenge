import random
ALPHA = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
SYMB = ["!","@","#","$""%","^","&","*","(",")","~"]
passw = ""    
length = int(input("Enter the length of the password      "))
for i in range(length):
    A = random.choice(ALPHA)
    a = (random.choice(ALPHA)).lower()
    SYM = random.choice(SYMB)
    N = random.randint(0,9)
    passw = passw+A+a+SYM+str(N) 
print("Password is",passw[0:length])