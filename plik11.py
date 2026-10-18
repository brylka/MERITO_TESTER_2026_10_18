for j in range(0,11):
    for i in range(0,11):
        if i == 0 and j == 0:
            print("*", end="\t")
        elif i == 0:
            print("\033[31m", j, "\033[0m", sep="", end="\t")
        elif j == 0:
            print("\033[31m", i, "\033[0m", sep="", end="\t")
        else:
            print(j*i, end="\t")
    print()
