n = int(input())

# Upper half of the rhombus
for i in range(n):
    # Print spaces before the stars
    for j in range(n-i-1):
        print(" ", end="")
    # Print stars
    for j in range(i+1):
        print("* ", end="")
    # Move to the next line
    print()

# Lower half of the rhombus
for i in range(n-2, -1, -1):
    # Print spaces before the stars
    for j in range(n-i-1):
        print(" ", end="")
    # Print stars
    for j in range(i+1):
        print("* ", end="")
    # Move to the next line
    print()
