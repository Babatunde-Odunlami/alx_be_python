#Creating a pattern in a square format given a size of one side
pattern_size = int(input("Enter the size of the pattern:"))
j = 0
while j <= pattern_sixe:
    for i in range(pattern_size):
        print("*", end="")
    print()
    j +=1
