from services import util
import sympy as sp

def punto_fijo_metodo(fn, gx, x0, error, decimales):

    x_anterior = 0
    i = 1
    xn = x0
    tabla = []
    iteraciones = []

    while True:

        print("i: ", i)
        if i == 1 and False:
            ea = 100
        else:
            ea = round(util.error_absoluto(x_anterior, xn), decimales)
        
        x_anterior = xn
        xn1 = util.evaluate_function(gx, xn, decimales)
        ea = round(util.error_absoluto(x_anterior, xn1)*100,4)

        tabla.append((i, xn, xn1, ea))

        if ea <= error :
            return tabla, xn1
        
        i += 1
        xn = xn1


    