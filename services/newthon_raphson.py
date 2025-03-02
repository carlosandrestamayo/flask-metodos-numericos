from services import util

def newton_raphson_metodo(fn, df, x0, error, decimales):
    
    x_anterior = 0
    i = 1
    xn = x0
    tabla = []
    iteraciones = []
    while True:
        
        f_x = util.evaluate_function(fn, xn, decimales)
        df_x = util.evaluate_function(df, xn, decimales)
        #x_anterior = xn
        xn1 = round(xn - f_x / df_x, decimales)
        ea = round(util.error_absoluto(xn, xn1)*100, decimales)
        tabla.append((i, xn, xn1, f_x, df_x, ea))
        
        iteraciones.append({
            'iteracion': i,
            'x': xn,
            'xn+1': xn1,
            'f_x': f_x,
            'df_x': df_x,
            'error': ea
        })
        
        if ea <= error:
            return tabla, xn1
        
        i += 1
        xn = xn1
