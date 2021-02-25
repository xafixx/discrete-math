U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
A = {2, 4, 6, 8, 10, 1}
B = {3, 5, 7, 9, 1, 17}
C = {1, 3, 6, 12, 14}

## basic set operation ##

# union
print(A | B)

# intersection
print(B & C)

# difference
print(A - C)

# simetric difference
print(B ^ C)
print("\n")

## set identities ##

# identity laws
print("identity laws")
print(A & U)
print(A | (set()))
print("\n")

# domination laws
print("domination laws")
print(A | U)
print(A & (set()))
print("\n")

# idempoten laws
print("idempoten laws")
print(A | A)
print(A & A)
print("\n")

# complementation laws
print("complementation laws")
print((U-(U-A)))
print("\n")

# comutative laws
print("comutative laws")
print((A | B), '=', (B | A))
print((A & B), '=', (B & A))
print("\n")

# associative laws
print("associative laws")
print((A | (B | C)), '=', ((A | B) | C))
print((A & (B & C)), '=', ((A & B) & C))
print("\n")

# distributive laws
print("distributive laws")
print(( A | (B & C)), '=', ((A | B) & ( A | C)))
print(( A & (B | C)), '=', ((A & B) | ( A & C)))
print("\n")