import Completing_The_Square
import Vertex_Form_Parabola
import Text
import Options

def Calculate_Parabola():
    print("Choose the function to calculate the parabola you want to use: ")
    parabola_chosen = Text.Parabola_options()

    method = Options.set_parabola_option(parabola_chosen)

    if method == "Vertex form":
        result = Vertex_Form_Parabola.Calculate_Vertex_Form()
        return result
    elif method == "Complete the square":
        result = Completing_The_Square.Calculate_Completing_The_Square()
        return result
    elif method == "Partial factored form":
        return "Partial factored form is not yet implemented"
    else:
        return "The option you chose is either invalid or not yet implemented"



