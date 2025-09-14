def Calculate_Parabola():
    print("At the moment this only calculates Vertex form from Standard form")

    print("Input the ax^2 + bx + c equation values in the format a, b, c")
    print("The values should be separated by a comma and a space")
    print("The x and the squared are not needed for they will be calculated atomatically")
    user_input = input("Enter the values here: ")
    a_str, b_str, c_str = user_input.split(", ")

    a = float(a_str)
    b = float(b_str)
    c = float(c_str)

    x = -b / (2 * a)
    y = a * x**2 + b * x + c

    print(f"In vertex form the equation is: y = {a}(x - ({x}))^2 + ({y})")
    print(f"The vertex is located at: ({x}, {y})")

    return f"Vertex form: y = {a}(x - ({x}))^2 + ({y}), Vertex: ({x}, {y})"


