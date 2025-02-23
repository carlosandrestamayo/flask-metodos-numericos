from services import util

def calculate_x2_secante(fn, x0, x1, decimales):
    
    fx0 = util.evaluate_function(fn, x0, decimales)
    fx1 = util.evaluate_function(fn, x1, decimales)
    
    x2 = x1 - ((fx1 * (x1 - x0)) / (fx1 - fx0))
        
    return round(x2, decimales)

def metodo_secante(fn, x0, x1, error = 0.05, decimales = 4):
    pass
    columnas = []
    iteraciones = []
    i = 1
    while True:
        
        x2 = calculate_x2_secante(fn, x0, x1, decimales)
        ea = util.error_absoluto(x1, x2)
        
        fx0 = util.evaluate_function(fn, x0, decimales)
        fx1 = util.evaluate_function(fn, x1, decimales)
        fx2 = util.evaluate_function(fn, x2, decimales)

        iteraciones.append((i, x1, x0, x2, fx0, fx1, fx2))
        print(iteraciones)
        columnas.append({"i":i,
                         "nuevox": f"X0 = {x0}, X1 = {x1}, xr = {x2}",
                         "fX0":"f(X0) =" + fn.replace('x',f"({x0})") + " = " + str(util.evaluate_function(fn, x0, decimales)),
                         "fX1":"f(X1) =" + fn.replace('x',f"({x1})") + " = " + str(util.evaluate_function(fn, x1, decimales)),
                         "fxr":"f(Xr) =" + fn.replace('x',f"({x2})") + " = " + str(util.evaluate_function(fn, x2, decimales))
                         })
        
        if ea < error:
            return iteraciones, columnas, x2 
        x0 = x1
        x1 = x2
        i += 1
        