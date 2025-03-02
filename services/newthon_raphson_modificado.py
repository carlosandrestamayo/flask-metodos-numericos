from services import util

def newton_raphson_modificado_metodo(fn, df,df2, x0, error, decimales):
    
    x_anterior = 0
    i = 1
    xn = x0
    tabla = []
    iteraciones = []
    while True:
        #print("x_anterior ", x_anterior)

        if i == 1 :
            ea = 100
        else :
            ea = util.error_absoluto(x_anterior, xn)
        
        print("iteración: ", i)
        f_x = util.evaluate_function(fn, xn, decimales)
        df_x = util.evaluate_function(df, xn, decimales)
        df2_x = util.evaluate_function(df2, xn, decimales)
        x_anterior = xn

        #numerador = (xn - ())
        denominador = df_x**2 - f_x * df2_x
        print("denominador: ", denominador)

        # if abs(denominador) < 1e-12:  # Evitar divisiones por valores muy pequeños
        #     print(f"Iteración {i+1}: División por cero detectada en x = {xn}. Deteniendo el cálculo.")
        #     return None


        xn1 = round(xn - (f_x * df_x) / denominador, decimales)

        print("df_x: ", df_x, " f_x: ", f_x, "df2_x: ", df2_x, " xn1: ", xn1, "denominador: ", denominador)


        #xn1 = round(xn - f_x / df_x, decimales)
        
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
