from sympy import sympify, symbols, lambdify
from sympy.core.sympify import SympifyError

def validate_function(expresion):
    try:
        sympify(expresion)
        return False, ""
    except SympifyError as e:
        print(e)
        return True, e
    
def verificar_limites(xi, xs):
   if xi < xs :
       return False, ""
   return True, "xs debe ser menor que xi"
   

def evaluate_function(fn, a, decimales = 4):
    x = symbols('x')
    f = lambdify(x,fn)
    #print(f(a))
    return round(f(a), decimales)
    
def teorema_bolzano(fn, a, b, decimales):
    fa = evaluate_function(fn, a, decimales)
    fb = evaluate_function(fn, b, decimales)
    
    if fa * fb < 0:
        return False, "Existen Raices en el intervalo"
    else:
        return True, "No existe raices en este intervalo"

def error_absoluto(xr_anterior, xr):
  return abs((xr - xr_anterior) / xr)

def validate_data(fn, a, b):
    error, msg = False, ""
    
    error, msg =  validate_function(fn)
    if not error :
        error, msg = verificar_limites(a, b)

    return error, msg
            
    
    