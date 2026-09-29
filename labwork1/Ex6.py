def ransequence():
    print("range1:", *range(0, 7))
    print("range2:", *range(1, 11, 3))
    print("range3:", *range(5, 0, -1))
    print("range4:", *range(6, -3, -2))


ransequence()