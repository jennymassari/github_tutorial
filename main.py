print("Hello, World!")
snoopy = r"""
       .-'''-.
      / .===. \
      \/ 6 6 \/
      ( \___/ )
 ___ooo__V__ooo___
/                \
|  Snoopy says:   |
|   Be Cool 😎    |
\________________/
       || ||
     __|| ||__
    (___| |___)
    """
print(snoopy)

# No-op change

print("My foo coracao for you: \n")

for row in range(6):
    for col in range(7):
        if ((row == 0 and col % 3 != 0) or
            (row == 1 and col % 3 == 0) or
            (row - col == 2) or
            (row + col == 8)):
            print("1", end=" ")
        else:
            print(" ", end=" ")
    print()