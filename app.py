from flask import Flask, render_template, request, send_from_directory

from services import util, biseccion, regla_falsa
#from services import biseccion

#print(biseccion.bisection())

app = Flask(__name__)
#app = Flask(__name__, static_folder="dist", static_url_path="")

@app.route('/', methods=['GET', 'POST'])
def index():
    #return send_from_directory("dist", "index.html")
    return render_template('index.html')

@app.route('/biseccion', methods=['GET', 'POST'])
def biseccion_route():
    iteraciones = []
    columnas = []
    error_data = False
    msg_data = ""
    error_bolzano, msg_bolzano = False, ""
    if request.method == 'POST':
        fn = request.form.get('fn','')
        a = float(request.form.get('a', 0))
        b = float(request.form.get('b', 1))
        ea = float(request.form.get('ea', 0.0001))
        decimales = int(request.form.get('decimales', 4))
        
        error_data, msg_data = util.validate_data(fn, a, b)    
        #print(error_data, "  ", msg_data)
        
        
        if not error_data:
            error_bolzano, msg_bolzano = util.teorema_bolzano(fn, a, b, decimales)
            if not error_bolzano :
                iteraciones, columnas = biseccion.bisection(fn, a, b, 0.005/100, decimales)
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
    if request.method == 'POST':
        
        fn = request.form.get('fn','')
        a = float(request.form.get('a', 0))
        b = float(request.form.get('b', 1))
        ea = float(request.form.get('ea', 0.0001))
        decimales = int(request.form.get('decimales', 4))
        
        error_data, msg_data = util.validate_data(fn, a, b)    
        #print(error_data, "  ", msg_data)
        
        #return render_template('reglafalsa.html', resultados = iteraciones, columnas = columnas,error_data = error_data, msg_data = msg_data, error_bolzano = error_bolzano, msg_bolzano = msg_bolzano)
        
        if not error_data:
            #print("primer if")
            error_bolzano, msg_bolzano = util.teorema_bolzano(fn, a, b, decimales)
            if not error_bolzano :
                #print("segundo if")
                iteraciones, columnas = regla_falsa.regla_falsa(fn, a, b, 0.005/100, decimales)
                return render_template('reglafalsa.html', resultados = iteraciones, columnas = columnas,error_data = error_data, msg_data = msg_data, error_bolzano = error_bolzano, msg_bolzano = msg_bolzano)
            else:
                pass
                return render_template('reglafalsa.html', resultados = iteraciones, columnas = columnas,error_data = error_data, msg_data = msg_data, error_bolzano = error_bolzano, msg_bolzano = msg_bolzano)
        else:
            pass
            return render_template('reglafalsa.html', resultados = iteraciones, columnas = columnas,error_data = error_data, msg_data = msg_data, error_bolzano = error_bolzano, msg_bolzano = msg_bolzano)
    
    #print(iteraciones, error_data, error_bolzano)
    return render_template('reglafalsa.html', resultados = [], columnas = [], error_data = False, msg_data = "", error_bolzano = False, msg_bolzano = "")  
    #return render_template('puntofijo.html')

@app.route('/puntofijo',  methods=['GET', 'POST'])
def puntofijo():
    return render_template('puntofijo.html')

@app.route('/secante',  methods=['GET', 'POST'])
def secante_route():
    return render_template('secante.html')

if __name__ == '__main__':
    app.run(debug=True)