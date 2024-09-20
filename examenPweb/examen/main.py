from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)

        resultado = f"Nombre: {nombre}<br>"
        resultado += f"Total sin descuento: ${total_sin_descuento:,.0f}<br>"
        resultado += f"Total a pagar con descuento: ${total_con_descuento:,.0f}"

        return render_template('ejercicio1.html', resultado=resultado)

    return render_template('ejercicio1.html')


usuarios = {
    "juan": {"contrasena": "admin", "tipo": "administrador"},
    "pepe": {"contrasena": "user", "tipo": "usuario"}
}


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario in usuarios and usuarios[usuario]["contrasena"] == contrasena:
            tipo = usuarios[usuario]["tipo"]
            mensaje = f"Bienvenido {tipo} {usuario}"
            return render_template('ejercicio2.html', mensaje=mensaje)
        else:
            mensaje = "Usuario o contraseña incorrectos"
            return render_template('ejercicio2.html', mensaje=mensaje, error=True)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run()