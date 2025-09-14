def set_option(function_name):
    if function_name == "1":
        print("You chose: Parabola")
        return "Parabola"
    elif function_name == "2":
        print("You chose: Circle")
        return "Circle"
    elif function_name == "3":
        print("You chose: Line")
        return "Line"
    elif function_name == "4":
        print("You chose: Complete the square")
        return "Complete the square"
    else:
        print("The option you chose is either invalid or not yet implemented")
    