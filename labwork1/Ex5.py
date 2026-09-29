def findcolor():
    colors = ["blue", "orange", "purple", "red"]
    favorite_color = input("What is your favorite color? ").strip().lower()

    if favorite_color in colors:
        color_index = colors.index(favorite_color)
        print(f"Your color is at index {color_index} in my list")
    else:
        print("Sorry, I could not find your color")


findcolor()