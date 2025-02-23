from services import util

def calculate_xr_biseccion(a, b, decimales):
    return round((a + b) / 2, decimales)


def bisection(fn, xi, xs, error = 0.05, decimales = 4):

    contador = 1
    xr_anterior = None
    xr = 0
    iteraciones = []
    columnas = []

    while True:
        xr_anterior = xr
        xr = calculate_xr_biseccion(xi, xs, decimales)
        ea = util.error_absoluto(xr_anterior, xr)
        
        fxi = util.evaluate_function(fn, xi, decimales)
        fxs = util.evaluate_function(fn, xs, decimales)
        fxr = util.evaluate_function(fn, xr, decimales)

        iteraciones.append((contador, xi, xs, xr, fxi, fxs, fxr))

        columnas.append({"contador":contador,
                         "nuevox": f"xi = {xi}, xs = {xs}, xr = {xr}",
                         "intervalos": f"Intervalos de [{xi}, {xr}] y [{xr}, {xs}]",
                         "fxi":"f(Xi) =" + fn.replace('x',f"({xi})") + " = " + str(util.evaluate_function(fn, xi, decimales)),
                         "fxs":"f(Xs) =" + fn.replace('x',f"({xs})") + " = " + str(util.evaluate_function(fn, xs, decimales)),
                         "fxr":"f(Xr) =" + fn.replace('x',f"({xr})") + " = " + str(util.evaluate_function(fn, xr, decimales))
                         })


        if util.evaluate_function(fn, xr, decimales) == 0:
                return xr
        elif util.evaluate_function(fn, xi, decimales) * util.evaluate_function(fn, xr, decimales) < 0:
                xs = xr
                # print(f"La raiz se encuentra en el intervalo [{a}, {b}] porque f(xi)*f(xr) < 0")
                # print(f"Hacemos Xs = {xr}")
                # iteracion = Iteracion(f"La raiz se encuentra en el intervalo [{a}, {b}] porque f(xi)*f(xr) < 0","Paragraph","normal")
                # row_iteracion.append(iteracion)
                # iteracion = Iteracion(f"Hacemos Xs = {xr}","Paragraph","normal")
                # row_iteracion.append(iteracion)
        elif util.evaluate_function(fn, xs, decimales) * util.evaluate_function(fn, xr, decimales) < 0:
                xi = xr
                # print(f"La raiz se encuentra en el intervalo [{a}, {b}] porque f(xi)*f(xr) > 0")
                # print(f"Hacemos Xi = {xr}")
                # iteracion = Iteracion(f"La raiz se encuentra en el intervalo [{a}, {b}] porque f(xi)*f(xr) > 0","Paragraph","normal")
                # row_iteracion.append(iteracion)
                # iteracion = Iteracion(f"Hacemos Xi = {xr}","Paragraph","normal")
                # row_iteracion.append(iteracion)
        else:
                #a = xr
                print(f"La raiz se encuentra en el intervalo [{xi}, {xs}]")
        
        contador += 1
        
        if util.error_absoluto(xr_anterior, xr) <= error:
                #print("contador: ", contador)
                
                return iteraciones, columnas 


    