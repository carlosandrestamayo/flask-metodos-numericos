from services import util

# def calculate_xr_regla_falsa(a, b, decimales):
#     return round((a + b) / 2, decimales)

def calculate_xr_regla_falsa(fn, a, b, decimales):
    
    fa = util.evaluate_function(fn, a, decimales)
    fb = util.evaluate_function(fn, b, decimales)
    
    xr = ((a * fb - b * fa) / (fb - fa))
    
    return round(xr, decimales)

def metodo_regla_falsa(fn, xi, xs, error = 0.05, decimales = 4):

    i = 1
    xr_anterior = None
    xr = 0
    iteraciones = []
    columnas = []

    while True:
        print("while")
        xr_anterior = xr    
        xr = calculate_xr_regla_falsa(fn, xi, xs, decimales)
        
        ea = util.error_absoluto(xr_anterior, xr)
        
        fxi = util.evaluate_function(fn, xi, decimales)
        fxs = util.evaluate_function(fn, xs, decimales)
        fxr = util.evaluate_function(fn, xr, decimales)

        iteraciones.append((i, xi, xs, xr, fxi, fxs, fxr))  

        columnas.append({"i":i,
                         "nuevox": f"xi = {xi}, xs = {xs}, xr = {xr}",
                         "intervalos": f"Intervalos de [{xi}, {xr}] y [{xr}, {xs}]",
                         "fxi":"f(Xi) =" + fn.replace('x',f"({xi})") + " = " + str(util.evaluate_function(fn, xi, decimales)),
                         "fxs":"f(Xs) =" + fn.replace('x',f"({xs})") + " = " + str(util.evaluate_function(fn, xs, decimales)),
                         "fxr":"f(Xr) =" + fn.replace('x',f"({xr})") + " = " + str(util.evaluate_function(fn, xr, decimales))
                         })


        print("i: ", i, "xi: ", xi, "xs: ", xs, "xr: ", xr, "xr_anterior: ", xr_anterior, "ea: ", ea, )
        print("f(xi): ", fxi, "f(xr): ", fxr)
        print(fxi*fxr)


        if fxi * fxr == 0:
               print("if")
        elif fxi * fxr < 0:
               xs = xr
               print("elif 1-1")

        elif fxi * fxr >= 0:
               print("elif 1-2")
               xi = xr
        else:
               print("else")

        # if util.evaluate_function(fn, xr, decimales) == 0:
        #         print("if")
        #         return iteraciones, columnas, xr
        # elif util.evaluate_function(fn, xi, decimales) * util.evaluate_function(fn, xr, decimales) < 0:
        #         print("elif")
        #         xs = xr
        #         # print(f"La raiz se encuentra en el intervalo [{a}, {b}] porque f(xi)*f(xr) < 0")
        #         # print(f"Hacemos Xs = {xr}")
        #         # iteracion = Iteracion(f"La raiz se encuentra en el intervalo [{a}, {b}] porque f(xi)*f(xr) < 0","Paragraph","normal")
        #         # row_iteracion.append(iteracion)
        #         # iteracion = Iteracion(f"Hacemos Xs = {xr}","Paragraph","normal")
        #         # row_iteracion.append(iteracion)
        # elif util.evaluate_function(fn, xs, decimales) * util.evaluate_function(fn, xr, decimales) >= 0:
        #         print("elif2")
        #         xi = xr
        #         # print(f"La raiz se encuentra en el intervalo [{a}, {b}] porque f(xi)*f(xr) > 0")
        #         # print(f"Hacemos Xi = {xr}")
        #         # iteracion = Iteracion(f"La raiz se encuentra en el intervalo [{a}, {b}] porque f(xi)*f(xr) > 0","Paragraph","normal")
        #         # row_iteracion.append(iteracion)
        #         # iteracion = Iteracion(f"Hacemos Xi = {xr}","Paragraph","normal")
        #         # row_iteracion.append(iteracion)
        # else:
        #         #a = xr
        #         print(f"La raiz se encuentra en el intervalo [{xi}, {xs}]")
        
        i += 1
        
        if util.error_absoluto(xr_anterior, xr) <= error:
                #print("i: ", i)
                return iteraciones, columnas, xr 


    