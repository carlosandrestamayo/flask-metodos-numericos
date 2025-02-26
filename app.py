from flask import Flask, render_template, request, send_from_directory

from services import util, biseccion, regla_falsa, secante, newthon_raphson

app = Flask(__name__)
#app = Flask(__name__, static_folder="dist", static_url_path="")

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/biseccion', methods=['GET', 'POST'])
def biseccion_route():
    iteraciones = []
    columnas = []
    error_data = False
    msg_data = ""
    error_bolzano, msg_bolzano = False, ""
    xr = 0
    if request.method == 'POST':
        fn = request.form.get('fn','')
        a = float(request.form.get('a', 0))
        b = float(request.form.get('b', 1))
        ea = float(request.form.get('ea', 0.0001))
        decimales = int(request.form.get('decimales', 4))
        
        error_data, msg_data = util.validate_data(fn, a, b)    
        
        if not error_data:
            error_bolzano, msg_bolzano = util.teorema_bolzano(fn, a, b, decimales)
            if not error_bolzano :
                iteraciones, columnas, xr = biseccion.metodo_biseccion(fn, a, b, 0.005/100, decimales)
                return render_template('biseccion.html', resultados = iteraciones, columnas = columnas,error_data = error_data, msg_data = msg_data, error_bolzano = error_bolzano, msg_bolzano = msg_bolzano)
            else:
                return render_template('biseccion.html', resultados = iteraciones, columnas = columnas,error_data = error_data, msg_data = msg_data, error_bolzano = error_bolzano, msg_bolzano = msg_bolzano)
        else:
            return render_template('biseccion.html', resultados = iteraciones, columnas = columnas,error_data = error_data, msg_data = msg_data, error_bolzano = error_bolzano, msg_bolzano = msg_bolzano)
    
    return render_template('biseccion.html', resultados = iteraciones, columnas = columnas,error_data = error_data, msg_data = msg_data, error_bolzano = error_bolzano, msg_bolzano = msg_bolzano)
    
@app.route('/reglafalsa',  methods=['GET', 'POST'])
def reglafalsa():
    iteraciones = []
    columnas = []
    error_data = False
    msg_data = ""
    error_bolzano, msg_bolzano = False, ""
    xr = 0
    if request.method == 'POST':
        
        fn = request.form.get('fn','')
        a = float(request.form.get('a', 0))
        b = float(request.form.get('b', 1))
        ea = float(request.form.get('ea', 0.0001))
        decimales = int(request.form.get('decimales', 4))
        
        error_data, msg_data = util.validate_data(fn, a, b)    
        
        if not error_data:
            error_bolzano, msg_bolzano = util.teorema_bolzano(fn, a, b, decimales)
            if not error_bolzano :
                iteraciones, columnas, xr = regla_falsa.metodo_regla_falsa(fn, a, b, 0.005/100, decimales)
                return render_template('reglafalsa.html', resultados = iteraciones, columnas = columnas,error_data = error_data, msg_data = msg_data, error_bolzano = error_bolzano, msg_bolzano = msg_bolzano)
            else:
                return render_template('reglafalsa.html', resultados = iteraciones, columnas = columnas,error_data = error_data, msg_data = msg_data, error_bolzano = error_bolzano, msg_bolzano = msg_bolzano)
        else:
            return render_template('reglafalsa.html', resultados = iteraciones, columnas = columnas,error_data = error_data, msg_data = msg_data, error_bolzano = error_bolzano, msg_bolzano = msg_bolzano)
    
    return render_template('reglafalsa.html', resultados = iteraciones, columnas = columnas,error_data = error_data, msg_data = msg_data, error_bolzano = error_bolzano, msg_bolzano = msg_bolzano)

@app.route('/puntofijo',  methods=['GET', 'POST'])
def puntofijo():
    return render_template('puntofijo.html')

@app.route('/secante',  methods=['GET', 'POST'])
def secante_route():
    
    iteraciones = []
    columnas = []
    error_data = False
    msg_data = ""
    x2 = 0
    fn = ""
   
    if request.method == 'POST':
        fn = request.form.get('fn','')
        x0 = float(request.form.get('a', 0))
        x1 = float(request.form.get('b', 1))
        ea = float(request.form.get('ea', 0.0001))
        decimales = int(request.form.get('decimales', 4))
        
        error_data, msg_data = util.validate_data(fn, x0, x1) 
    
        if not error_data:
            iteraciones, columnas, x2 = secante.metodo_secante(fn, x0, x1, 0.005/100, decimales)
            
    return render_template('secante.html', resultados = iteraciones, columnas = columnas, error_data = error_data, msg_data = msg_data,fn=fn, x0 =x0, x1 = x1)

@app.route('/newtonraphson',  methods=['GET', 'POST'])
def newton_raphson_route():
    iteraciones = []
    columnas = []
    error_data = False
    msg_data = ""
    xr = 0
    df = ""
    resultados = []
    imprimir = ""
   
    if request.method == 'POST':
        fn = request.form.get('fn','')
        x0 = float(request.form.get('a', 0))
        ea = float(request.form.get('ea', 0.0001))
        decimales = int(request.form.get('decimales', 4))
        imprimir = request.form.get('imprimir',"")
        print("imprimir ",imprimir)
        
        error_data, msg_data = util.validate_function(fn) 
        
        if not error_data:
            df = util.derivate_function(fn)
            resultados, xr = newthon_raphson.newton_raphson_metodo(fn, df, x0, ea/100, decimales)
            print(resultados)
        
    return render_template('newton_raphson.html', df = df, resultados = resultados, columnas= columnas, xr = xr)

if __name__ == '__main__':
    app.run(debug=True)