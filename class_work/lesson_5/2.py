i = 0

# --- With Continue ---
for i in range(0,100,1):
    if i % 2 == 0:
        continue
    print(i, end=" ")
else: 
    print("\r")

# --- Without Continue ---
for i in range(0,100,1):
    if i % 2 != 0:
        print(i, end=" ")
else: 
    print("\r")

# --- Without if ---
for i in range(1,100,2):
     print(i, end=" ")    
else: 
    print("\r")