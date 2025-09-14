import Options
import Text
import Parabola
import Completing_The_Square

print("Welcome to the functions calculator")
print("What Function would you like to calculate?")

funtion_chosen = Text.function_options()

function = Options.set_option(funtion_chosen)

if function == "Parabola":
    result = Parabola.Calculate_Parabola()
    print(result)
elif function == "Circle":
    print("Circle function is not yet implemented")
elif function == "Line":
    print("Line function is not yet implemented")
elif function == "Complete the square":
    result = Completing_The_Square.Calculate_Completing_The_Square()
    print(result)
else:
    print("The option you chose is either invalid or not yet implemented")

print("Thank you for using the functions calculator")
print("Hope you got the results you were looking for")

input("Press Enter to exit")