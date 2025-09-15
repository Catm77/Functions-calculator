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
    else:
        print("The option you chose is either invalid or not yet implemented")

def set_parabola_option(parabola_option):
    if parabola_option == "1":
        print("You chose: Vertex form")
        return "Vertex form"
    elif parabola_option == "2":
        print("You chose: Completing the square")
        return "Complete the square"
    elif parabola_option == "3":
        print("You chose: Partial factored form")
        return "Partial factored form"
    else:
        print("The option you chose is either invalid or not yet implemented")
    