from services.util import *

def calculate_xr_biseccion(a, b, decimales):
    return round((a + b) / 2, decimales)


def metodo_biseccion(fn, xi, xs, error = 0.05, decimales = 4):

    i = 1
    xr_anterior = None
    xr = 0
    iteraciones = []
    columnas = []

    while True:
        xr_anterior = round(xr, decimales)
        xr = calculate_xr_biseccion(xi, xs, decimales)
        ea = error_absoluto(xr_anterior, xr)
        
        #xi = round(xi, decimales)
        #xs = round(xs, decimales)
        
        print("xi: ", xi, " xs: ", xs)
        fxi = convert_to_decimal(evaluate_function(fn, xi, decimales), decimales)
        fxs = convert_to_decimal(evaluate_function(fn, xs, decimales), decimales)
        fxr = convert_to_decimal(evaluate_function(fn, xr, decimales), decimales)

        iteraciones.append((i, convert_to_decimal(xi, decimales), convert_to_decimal(xs, decimales), convert_to_decimal(xr, decimales), fxi, fxs, fxr, "" if i == 1 else ea*100))
        
        columna = {"i":i,
                   "nuevox": f"xi = {xi:.{decimales}f}, xs = {xs:.{decimales}f}, xr = {xr:.{decimales}f}",
                   "intervalos": f"Intervalos de [{xi}, {xr}] y [{xr}, {xs}]",
                   #"fxi":"f(Xi) =" + fn.replace('x',f"({xi})") + " = " + str(evaluate_function(fn, xi, decimales)),
                   "fxi":"f(Xi) =" + fn.replace('x',f"({xi})") + " = " + fxi,
                   "fxs":"f(Xs) =" + fn.replace('x',f"({xs})") + " = " + fxs,
                   "fxr":"f(Xr) =" + fn.replace('x',f"({xr})") + " = " + fxr,
                   "cambiox1":"",
                   "cambiox2":""
                         } 

        if evaluate_function(fn, xr, decimales) == 0:
                return iteraciones, columnas, xr
        elif evaluate_function(fn, xi, decimales) * evaluate_function(fn, xr, decimales) < 0:
                
                xs = xr
                columna["cambiox1"] = f"La raiz se encuentra en el intervalo [{xi}, {xs}] porque f(xi)*f(xr) < 0"
                columna["cambiox2"] = f"Hacemos Xs = {xr}"
                # print(f"La raiz se encuentra en el intervalo [{a}, {b}] porque f(xi)*f(xr) < 0")
                # print(f"Hacemos Xs = {xr}")
                # iteracion = Iteracion(f"La raiz se encuentra en el intervalo [{a}, {b}] porque f(xi)*f(xr) < 0","Paragraph","normal")
                # row_iteracion.append(iteracion)
                # iteracion = Iteracion(f"Hacemos Xs = {xr}","Paragraph","normal")
                # row_iteracion.append(iteracion)
        elif evaluate_function(fn, xs, decimales) * evaluate_function(fn, xr, decimales) < 0:
                xi = xr
                columna["cambiox1"] = f"La raiz se encuentra en el intervalo [{xi}, {xs}] porque f(xi)*f(xr) no es < 0"
                columna["cambiox2"] = f"Hacemos Xi = {xr}"
                # print(f"La raiz se encuentra en el intervalo [{a}, {b}] porque f(xi)*f(xr) > 0")
                # print(f"Hacemos Xi = {xr}")
                # iteracion = Iteracion(f"La raiz se encuentra en el intervalo [{a}, {b}] porque f(xi)*f(xr) > 0","Paragraph","normal")
                # row_iteracion.append(iteracion)
                # iteracion = Iteracion(f"Hacemos Xi = {xr}","Paragraph","normal")
                # row_iteracion.append(iteracion)
        else:
                #a = xr
                print(f"La raiz se encuentra en el intervalo [{xi}, {xs}]")
                
        columnas.append(columna)
        
        i += 1
        
        if error_absoluto(xr_anterior, xr) <= error:
                #print("i: ", i)
                return iteraciones, columnas, xr


    