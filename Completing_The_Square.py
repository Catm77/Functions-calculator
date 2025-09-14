def Calculate_Completing_The_Square():
    print("Input the function of ax^2 + bx + c in the format of a, b, c")
    print("If there is no a value, input 1")
    print("The values should be separated by a comma and a space")
    print("The x and the squared are not needed for they will be calculated atomatically")
    user_values = input("Enter the values here: ")
    a_str, b_str, c_str = user_values.split(", ")

    a = float(a_str)
    b = float(b_str)
    c = float(c_str)

    kk = (b/2)**2

    h = (-kk * a) + c

    k = b/2 

    if a > 0:
        print("The parabola opens upwards and has a minimum value")
    elif a < 0:
        print("The parabola opens downwards and has a maximum value")

    print(f"The completed square form of the equation is: y = {a}(x + {k}))^2 + ({h})")
    print(f"The vertex is located at: ({-k}, {h})")
    return f"Completed square form: y = {a}(x + (x - {k}))^2 + ({h}), Vertex: ({-k}, {h})"