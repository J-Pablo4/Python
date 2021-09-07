# Estacionamiento Inteligente
# Juan Pablo López Zúñiga
# Santiago Jacques Valenzuela
from tkinter import *
from tkinter import messagebox
from tkinter import ttk, font
import webbrowser
from tkcalendar import *
from PIL import ImageTk, Image
import qrcode
import random

ventana = Tk()
ventana.title("Inicio de sesión")
ventana.iconbitmap('C:/archivos_proyecto/game.ico')
ventana.geometry("500x500")

frame_inicio = ttk.Frame(ventana)
frame_registro = ttk.Frame(ventana)
frame_cambioCon = ttk.Frame(ventana)
toolbar = ttk.Frame(ventana)
frame_Mainmenu = ttk.Frame(ventana)
frame_Reglas = ttk.Frame(ventana)
frame_Ayuda = ttk.Frame(ventana)
frame_Qrcode = ttk.Frame(ventana)
frame_Renta = ttk.Frame(ventana)
frame_Mapa = ttk.Frame(ventana)

frame_list = [frame_Mainmenu, frame_Mapa, frame_Reglas, frame_Ayuda, frame_Renta, frame_Qrcode]
toolbar.grid(row=0, column=0)
for frame in frame_list:
    frame.grid(row=0, column=1)
for frame in (frame_inicio, frame_registro, frame_cambioCon):
    frame.grid(row=1, column=3)

fuente = font.Font(weight='bold')

def regreso_inicio_de_sesion():
    frame_inicio.grid_remove()
    frame_registro.grid_remove()
    frame_cambioCon.grid_remove()
    frame_Mapa.grid_remove()
    frame_Ayuda.grid_remove()
    frame_Qrcode.grid_remove()
    frame_Renta.grid_remove()
    frame_Reglas.grid_remove()
    frame_Mainmenu.grid_remove()
    toolbar.grid_remove()
    for widget in frame_inicio.winfo_children():
        widget.destroy()
    frame_inicio.grid()

    def inicio():
        frame_inicio.grid_remove()
        frame_Mainmenu.grid_remove()
        frame_Qrcode.grid_remove()
        frame_Ayuda.grid_remove()
        frame_Reglas.grid_remove()
        frame_Renta.grid_remove()
        frame_Mapa.grid_remove()
        toolbar.grid_remove()
        for widget in frame_Mainmenu.winfo_children():
            widget.destroy()
        frame_inicio.grid()

        correo = in_putU.get()
        in_putC.get()
        email_contra_correcto = 0
        input_vacio = 0
        email_contra_incorrecto = 0
        archivo = open("C:/archivos_proyecto/usuario_y_contrasena.txt", "r")
        for linea in archivo.readlines():
            datos = linea.split(':')
            email = datos[0]
            contrasena = datos[1]
            correo_de_input = in_putU.get()
            contrasena_de_input = in_putC.get()

            if correo_de_input == email.strip() and contrasena_de_input == contrasena.strip():
                email_contra_correcto = 1

            elif len(in_putU.get()) == 0 and len(in_putC.get()) == 0:
                input_vacio = 1

            elif in_putU.get() != email.strip() or in_putC.get() != contrasena.strip():
                email_contra_incorrecto = 1

        archivo.close()
        if email_contra_correcto == 1:
            # Adentro del sistema
            frame_inicio.grid_remove()
            frame_Mainmenu.grid_remove()
            for widget in frame_inicio.winfo_children():
                widget.destroy()
            toolbar.grid()
            frame_Mainmenu.grid()

            foto_de_astronauta = ImageTk.PhotoImage(Image.open("C:/archivos_proyecto/descarga.png"))
            foto_de_mapa = ImageTk.PhotoImage(Image.open("C:/archivos_proyecto/mapa_1.jpg"))

            def Inicio():
                frame_inicio.grid_remove()
                frame_Mainmenu.grid_remove()
                frame_Qrcode.grid_remove()
                frame_Ayuda.grid_remove()
                frame_Reglas.grid_remove()
                frame_Renta.grid_remove()
                frame_Mapa.grid_remove()
                for widget in frame_Mainmenu.winfo_children():
                    widget.destroy()
                frame_Mainmenu.grid()

                global etiqueta_de_foto_de_astronauta
                global mi_etiN
                global mi_etiA
                global mi_etiP
                global mi_etiCl
                global mi_etiMr
                global mi_etiSMr
                global mi_etiE
                global mi_etiM
                global mi_etiC

                etiqueta_de_foto_de_astronauta = Label(frame_Mainmenu, image=foto_de_astronauta).pack()
                archivo_informacion = open("C:/archivos_proyecto/info_registro.txt", 'r')
                archivo_informacion.seek(0)
                for linea in archivo_informacion.readlines():
                    datos = linea.split(':')
                    email = datos[0]
                    if correo == email:
                        nombre = datos[1]
                        matricula = datos[2]
                        carrera = datos[3]
                        edificio = datos[4]
                        marca = datos[5]
                        sub_marca = datos[6]
                        color = datos[7]
                        anyo = datos[8]
                        placas = datos[9]

                        mi_etiN = Label(frame_Mainmenu, text=f"Nombre: {nombre.strip()}").pack()
                        mi_etiM = Label(frame_Mainmenu, text=f"Matricula: {matricula.strip()}").pack()
                        mi_etiC = Label(frame_Mainmenu, text=f"Carrera: {carrera.strip()}").pack()
                        mi_etiE = Label(frame_Mainmenu, text=f"Edificio más concurrido: {edificio.strip()}").pack()
                        mi_etiMr = Label(frame_Mainmenu, text=f"Marca: {marca.strip()}").pack()
                        mi_etiSMr = Label(frame_Mainmenu, text=f"Submarca: {sub_marca.strip()}").pack()
                        mi_etiCl = Label(frame_Mainmenu, text=f"Color: {color.strip()}").pack()
                        mi_etiA = Label(frame_Mainmenu, text=f"Año: {anyo.strip()}").pack()
                        mi_etiP = Label(frame_Mainmenu, text=f"Placas: {placas.strip()}").pack()
                archivo_informacion.close()

                boton_salir = ttk.Button(frame_Mainmenu, text="Cerrar Sesión", command=regreso_inicio_de_sesion)
                boton_salir.pack(side=BOTTOM)

            def Mapa():
                frame_inicio.grid_remove()
                frame_Mainmenu.grid_remove()
                frame_Qrcode.grid_remove()
                frame_Ayuda.grid_remove()
                frame_Reglas.grid_remove()
                frame_Renta.grid_remove()
                frame_Mapa.grid_remove()
                for widget in frame_Mapa.winfo_children():
                    widget.destroy()
                frame_Mapa.grid()
                etiqueta_de_foto_de_mapa = Label(frame_Mapa, image=foto_de_mapa).pack()
                letra = ttk.Label(frame_Mapa, text="Letra: Representa la zona.")
                numero = ttk.Label(frame_Mapa, text="Número: Representa una fila.")
                letra.pack()
                numero.pack()

                hay_en_lugares = False
                hay_en_renta = False
                lugar_en_lugares = ""
                lugar_en_renta = ""

                archivo_lugares = open("C:/archivos_proyecto/lugares_de_estacionamiento.txt", 'r')
                archivo_lugares.seek(0)
                for linea in archivo_lugares.readlines():
                    datos = linea.split(':')
                    email = datos[0]
                    if correo == email:
                        hay_en_lugares = True
                        lugar_en_lugares = datos[1]
                archivo_lugares.close()

                archivo_renta = open("C:/archivos_proyecto/lugares_de_renta.txt", 'r')
                archivo_renta.seek(0)
                for linea in archivo_renta.readlines():
                    datos = linea.split(':')
                    email = datos[0]
                    if correo == email:
                        hay_en_renta = True
                        lugar_en_renta = datos[1]
                archivo_renta.close()

                if hay_en_renta == True:
                    lugar_de_estacionamiento = Label(frame_Mapa,
                                                     text=f"Lugar asignado: {lugar_en_renta.strip()}").pack()
                elif hay_en_lugares == True:
                    lugar_de_estacionamiento = Label(frame_Mapa,
                                                     text=f"Lugar asignado: {lugar_en_lugares.strip()}").pack()

                boton_regreso_inicio = ttk.Button(frame_Mapa, text="Cerrar Sesión", command=regreso_inicio_de_sesion)
                boton_regreso_inicio.pack(side=BOTTOM)

            def Reglas():
                frame_inicio.grid_remove()
                frame_Mainmenu.grid_remove()
                frame_Qrcode.grid_remove()
                frame_Ayuda.grid_remove()
                frame_Reglas.grid_remove()
                frame_Renta.grid_remove()
                frame_Mapa.grid_remove()
                for widget in frame_Reglas.winfo_children():
                    widget.destroy()
                frame_Reglas.grid()

                regla = ttk.Label(frame_Reglas, text="Reglas del usos", font=fuente).pack()
                regla_1 = ttk.Label(frame_Reglas,
                                    text="1.No usar otro lugar que no sea el que se le haya asignado.").pack()
                regla_2 = ttk.Label(frame_Reglas,
                                    text="2.Asegurarse de que el codigo usado si corresponda al usuario y al vehiculo que ingreso.").pack()
                regla_3 = ttk.Label(frame_Reglas, text="3.No estorbar otros lugares de estacionamiento.").pack()
                regla_4 = ttk.Label(frame_Reglas, text="4.Evitar permanecer en el vehiculo al estacionarse.").pack()
                regla_5 = ttk.Label(frame_Reglas, text="5.Tener preparado el codigo al ingresar al campus.").pack()
                regla_6 = ttk.Label(frame_Reglas,
                                    text="6.En caso de incumplir alguna de estas reglas sera acredor de una sancion.").pack()
                boton_salir = ttk.Button(frame_Reglas, text="Cerrar Sesión", command=regreso_inicio_de_sesion)
                boton_salir.pack(side=BOTTOM)

            def Ayuda():
                frame_inicio.grid_remove()
                frame_Mainmenu.grid_remove()
                frame_Qrcode.grid_remove()
                frame_Ayuda.grid_remove()
                frame_Reglas.grid_remove()
                frame_Renta.grid_remove()
                frame_Mapa.grid_remove()
                for widget in frame_Ayuda.winfo_children():
                    widget.destroy()
                frame_Ayuda.grid()

                ayuda = Label(frame_Ayuda, text="Ayuda y Comentarios", font=fuente).pack()
                linea_1 = Label(frame_Ayuda, text="En caso de tener algun problema con").pack()
                linea_2 = Label(frame_Ayuda, text="el codigo generado, su informacion personal").pack()
                linea_3 = Label(frame_Ayuda, text="o con el uso de este servicio.").pack()
                linea_4 = Label(frame_Ayuda, text="Favor de comunicarse al siguiente mail:").pack()

                # Función para utilizar link
                def callback(url):
                    webbrowser.open_new(url)

                link1 = Label(frame_Ayuda, text="generico@iteso.mx", fg="blue", cursor="hand2")
                link1.pack()
                link1.bind("<Button-1>", lambda e: callback("https://www.iteso.mx/contacto"))

                comentarios = Label(frame_Ayuda, text="Comentarios y Sugerencias", font=fuente).pack()
                linea_5 = Label(frame_Ayuda, text="Mandanos tu opinion sobre el servicio al siguiente mail").pack()
                linea_6 = Label(frame_Ayuda, text="Queremos escucharte:").pack()
                link1 = Label(frame_Ayuda, text="generico@iteso.mx", fg="blue", cursor="hand2")
                link1.pack()
                link1.bind("<Button-1>", lambda e: callback("https://www.iteso.mx/contacto"))

                boton_salir = ttk.Button(frame_Ayuda, text="Cerrar Sesión", command=regreso_inicio_de_sesion)
                boton_salir.pack(side=BOTTOM)

            def Renta():
                frame_inicio.grid_remove()
                frame_Mainmenu.grid_remove()
                frame_Qrcode.grid_remove()
                frame_Ayuda.grid_remove()
                frame_Reglas.grid_remove()
                frame_Renta.grid_remove()
                frame_Mapa.grid_remove()
                for widget in frame_Renta.winfo_children():
                    widget.destroy()
                frame_Renta.grid()

                myLabel = Label(frame_Renta, text="Servicio de renta")
                myLabel.pack()

                linea_1 = Label(frame_Renta, text="Instrucciones para rentar:").pack()
                linea_2 = Label(frame_Renta,
                                text="En la primera casilla escriba la letra, en mayúsculas, de la zona").pack()
                linea_3 = Label(frame_Renta, text=" donde desea estacionarse.").pack()
                linea_4 = Label(frame_Renta,
                                text="En las casillas restantes escriba simplente los números de lo que se "
                                     "le solicita").pack()
                linea_5 = Label(frame_Renta, text="Seleccione una fecha en el calendario, y a continuación "
                                                  "pulse Guardar.").pack()

                texto = Label(frame_Renta, text="Ingrese los datos para apartar el cajon de estacionamiento.")
                texto.pack()

                letra_etiqueta = ttk.Label(frame_Renta, text="Letra: Representa la zona.").pack()
                zona = Entry(frame_Renta, width=55, borderwidth=2)
                zona.pack()
                zona.insert(0, "Letra")

                numero_etiqueta = ttk.Label(frame_Renta, text="Número: Representa una fila.").pack()
                numero = Entry(frame_Renta, width=55, borderwidth=2)
                numero.pack()
                numero.insert(0, "Número")

                horas_etiqueta = ttk.Label(frame_Renta,
                                           text="Horas: Representa las horas que planea rentar el espacio.").pack()
                horas = Entry(frame_Renta, width=55, borderwidth=2)
                horas.pack()
                horas.insert(0, "Horas")

                cal = Calendar(frame_Renta, selectmode="day", year=2020, month=12, day=3)
                cal.pack()

                def guardar_fecha():
                    lugar_letra_numero = zona.get() + numero.get()
                    diccionario_renta_de_lugares = {}
                    diccionario_renta_de_lugares["lugar"] = lugar_letra_numero
                    diccionario_renta_de_lugares["hora"] = horas.get()
                    lista_de_otros = []
                    archivo_lugares = open("C:/archivos_proyecto/lugares_de_estacionamiento.txt", 'r')
                    archivo_lugares.seek(0)
                    for linea in archivo_lugares.readlines():
                        datos = linea.split(':')
                        email = datos[0]
                        if correo == email:
                            diccionario_renta_de_lugares["correo"] = email
                    archivo_lugares.close()

                    archivo_renta = open("C:/archivos_proyecto/lugares_de_renta.txt", 'r')
                    archivo_renta.seek(0)
                    for linea in archivo_renta.readlines():
                        datos = linea.split(':')
                        email = datos[0]
                        lista_de_otros.append(email)
                        archivo_renta.close()
                    if correo not in lista_de_otros:
                        linea1 = (diccionario_renta_de_lugares.get(
                            "correo") + ':' + diccionario_renta_de_lugares.get(
                            "lugar")
                                  + ':' + diccionario_renta_de_lugares.get("hora") + "hr" + ":" + cal.get_date())
                        archivo_renta = open("C:/archivos_proyecto/lugares_de_renta.txt", "a")
                        archivo_renta.writelines(f"{linea1}\n")
                        archivo_renta.close()
                        correcto = messagebox.showinfo("Popup",
                                                       "La información de su renta se ha guardado en el sistema correctamente. "
                                                       "Favor de seleccionar una opción de pago.")
                    else:
                        respuesta = messagebox.showerror("Popup",
                                                         "Ya se ha rentado un lugar con este correo. Por favor, espere"
                                                         " hasta el día de mañana para volver a rentar.")

                texto = Label(frame_Renta, text="")
                texto.pack()

                linea_1 = Label(frame_Renta, text="Usted va a el cajon con la ubicacion").pack()
                linea_2 = Label(frame_Renta, text="que ingreso previamente. Por X  horas con un costo de").pack()
                linea_3 = Label(frame_Renta, text=" 15 pesos la hora.").pack()
                linea_4 = Label(frame_Renta, text="En caso de sobrepasar el tiempo ingresado").pack()
                linea_5 = Label(frame_Renta, text=" se le hara un cargo de 35 pesos por cada hora extra.").pack()

                boton = ttk.Button(frame_Renta, text="Guardar", command=guardar_fecha)
                boton.pack()

                def callback(url):
                    webbrowser.open_new(url)

                link1 = Label(frame_Renta, text="Pagar ahora", fg="blue", cursor="hand2")
                link1.pack()
                link1.bind("<Button-1>",
                           lambda e: callback("https://servicios.iteso.mx/apps/alumno/estado_cuenta/index.jsp"))

                link1 = Label(frame_Renta, text="Agregar pago a colegiatura", fg="blue", cursor="hand2")
                link1.pack()
                link1.bind("<Button-1>",
                           lambda e: callback("https://servicios.iteso.mx/apps/alumno/estado_cuenta/index.jsp"))

                boton_salir = ttk.Button(frame_Renta, text="Cerrar Sesión", command=regreso_inicio_de_sesion)
                boton_salir.pack(side=BOTTOM)

            def Qrcode():
                frame_inicio.grid_remove()
                frame_Mainmenu.grid_remove()
                frame_Qrcode.grid_remove()
                frame_Ayuda.grid_remove()
                frame_Reglas.grid_remove()
                frame_Renta.grid_remove()
                frame_Mapa.grid_remove()
                for widget in frame_Qrcode.winfo_children():
                    widget.destroy()
                frame_Qrcode.grid()

                informacion_de_usuario_en_QR = []
                archivo_informacion = open("C:/archivos_proyecto/info_registro.txt", 'r')
                archivo_informacion.seek(0)
                for linea in archivo_informacion.readlines():
                    datos = linea.split(':')
                    email = datos[0]
                    if correo == email:
                        informacion_de_usuario_en_QR.append(f"Nombre: {datos[1]}")
                        informacion_de_usuario_en_QR.append(f"Matrícula: {datos[2]}")
                        informacion_de_usuario_en_QR.append(f"Carrera: {datos[3]}")
                        informacion_de_usuario_en_QR.append(f"Edificio más concurrido: {datos[4]}")
                        informacion_de_usuario_en_QR.append(f"Marca: {datos[5]}")
                        informacion_de_usuario_en_QR.append(f"Sub marca: {datos[6]}")
                        informacion_de_usuario_en_QR.append(f"Color: {datos[7]}")
                        informacion_de_usuario_en_QR.append(f"Año: {datos[8]}")
                        informacion_de_usuario_en_QR.append(f"Placas: {datos[9]}")
                archivo_informacion.close()

                titulo = Label(frame_Qrcode, text="Codigo QR", font=fuente).grid(row=0, column=0)

                qr = qrcode.QRCode(
                    version=1,
                    box_size=8,
                    border=1,
                )
                informacion = informacion_de_usuario_en_QR
                qr.add_data(informacion)
                imagen = qr.make_image(fill="black", back_color="white")
                imagen.save("prueba_qrcode.jpg")
                my_img = ImageTk.PhotoImage(Image.open("prueba_qrcode.jpg"))
                foto = Label(frame_Qrcode, image=my_img).grid(row=1, column=0)

                instrucciones_1 = ttk.Label(frame_Qrcode, text="Con este código QR usted podrá").grid(row=2, column=0)
                instrucciones_2 = ttk.Label(frame_Qrcode, text="entrar a las instalaciones del ITESO.").grid(row=3,
                                                                                                             column=0)

                boton_salir = ttk.Button(frame_Qrcode, text="Cerrar Sesión", command=regreso_inicio_de_sesion)
                boton_salir.grid(row=4, column=0)
                frame_Qrcode.mainloop()

            etiqueta_de_foto_de_astronauta = Label(frame_Mainmenu, image=foto_de_astronauta).pack()
            archivo_informacion = open("C:/archivos_proyecto/info_registro.txt", 'r')
            archivo_informacion.seek(0)
            for linea in archivo_informacion.readlines():
                datos = linea.split(':')
                email = datos[0]
                if correo == email:
                    nombre = datos[1]
                    matricula = datos[2]
                    carrera = datos[3]
                    edificio = datos[4]
                    marca = datos[5]
                    sub_marca = datos[6]
                    color = datos[7]
                    anyo = datos[8]
                    placas = datos[9]

                    mi_etiN = Label(frame_Mainmenu, text=f"Nombre: {nombre.strip()}").pack()
                    mi_etiM = Label(frame_Mainmenu, text=f"Matricula: {matricula.strip()}").pack()
                    mi_etiC = Label(frame_Mainmenu, text=f"Carrera: {carrera.strip()}").pack()
                    mi_etiE = Label(frame_Mainmenu, text=f"Edificio más concurrido: {edificio.strip()}").pack()
                    mi_etiMr = Label(frame_Mainmenu, text=f"Marca: {marca.strip()}").pack()
                    mi_etiSMr = Label(frame_Mainmenu, text=f"Submarca: {sub_marca.strip()}").pack()
                    mi_etiCl = Label(frame_Mainmenu, text=f"Color: {color.strip()}").pack()
                    mi_etiA = Label(frame_Mainmenu, text=f"Año: {anyo.strip()}").pack()
                    mi_etiP = Label(frame_Mainmenu, text=f"Placas: {placas.strip()}").pack()
            archivo_informacion.close()

            boton_MainMenu = ttk.Button(toolbar, text="Inicio", command=Inicio)
            boton_MainMenu.grid(row=0, column=0)
            boton_CodigoQr = ttk.Button(toolbar, text="Código QR", command=Qrcode)
            boton_CodigoQr.grid(row=1, column=0)
            boton_Mapa = ttk.Button(toolbar, text="Mapa", command=Mapa)
            boton_Mapa.grid(row=2, column=0)
            boton_Ayuda = ttk.Button(toolbar, text="Ayuda", command=Ayuda)
            boton_Ayuda.grid(row=3, column=0)
            boton_Reglas = ttk.Button(toolbar, text="Reglas", command=Reglas)
            boton_Reglas.grid(row=4, column=0)
            boton_Renta = ttk.Button(toolbar, text="Renta", command=Renta)
            boton_Renta.grid(row=5, column=0)

            boton_salir = ttk.Button(frame_Mainmenu, text="Cerrar Sesión", command=regreso_inicio_de_sesion)
            boton_salir.pack(side=BOTTOM)

        elif input_vacio == 1:
            respuesta = messagebox.showerror("Popup", "Las casillas de Usuario y Contraseña están vacias.")

        elif email_contra_incorrecto == 1:
            respuesta = messagebox.showerror("Popup", "El usuario o la contraseña no coinciden. Favor de reintentar.")

    mi_eti = Label(frame_inicio, text="Inicio de Sesión").pack()
    mi_etiU = Label(frame_inicio, text="Correo del ITESO:", font=fuente)
    mi_etiU.pack()
    in_putU = Entry(frame_inicio, width=55, borderwidth=2)
    in_putU.pack()

    mi_etiC = Label(frame_inicio, text="Contraseña:", font=fuente)
    mi_etiC.pack()
    in_putC = Entry(frame_inicio, width=55, borderwidth=2)
    in_putC.pack()

    botonInicio = ttk.Button(frame_inicio, text="Ingresar", command=inicio)
    botonInicio.pack()
    botonInicio.focus_set()
    botonRegistro = ttk.Button(frame_inicio, text="¿Nuevo Usuario?", command=Registro)
    botonRegistro.pack()

    etiqueta1 = Label(frame_inicio, text="¿Tienes problemas para acceder?").pack()
    etiqueta2 = Label(frame_inicio, text="Por favor envía un correo electrónico a:").pack()

    # Función para utilizar link
    def callback(url):
        webbrowser.open_new(url)

    link1 = Label(frame_inicio, text="generico@iteso.mx", fg="blue", cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.iteso.mx/contacto"))

    boton_NuevaContra = ttk.Button(frame_inicio, text="¿Deseas cambiar tu contraseña?", command=cambioCon)
    boton_NuevaContra.pack()

# Inicio de Sesión
def inicio():
    correo = in_putU.get()
    in_putC.get()
    email_contra_correcto = 0
    input_vacio = 0
    email_contra_incorrecto = 0
    archivo = open("C:/archivos_proyecto/usuario_y_contrasena.txt", "r")
    for linea in archivo.readlines():
        datos = linea.split(':')
        email = datos[0]
        contrasena = datos[1]
        correo_de_input = in_putU.get()
        contrasena_de_input = in_putC.get()

        if correo_de_input == email.strip() and contrasena_de_input == contrasena.strip():
            email_contra_correcto = 1

        elif len(in_putU.get()) == 0 and len(in_putC.get()) == 0:
            input_vacio = 1

        elif in_putU.get() != email.strip() or in_putC.get() != contrasena.strip():
            email_contra_incorrecto = 1

    archivo.close()
    if email_contra_correcto == 1:
        # Adentro del sistema
        frame_inicio.grid_remove()
        frame_Mainmenu.grid_remove()
        for widget in frame_inicio.winfo_children():
            widget.destroy()
        frame_Mainmenu.grid()

        foto_de_astronauta = ImageTk.PhotoImage(Image.open("C:/archivos_proyecto/descarga.png"))
        foto_de_mapa = ImageTk.PhotoImage(Image.open("C:/archivos_proyecto/mapa_1.jpg"))

        def Inicio():
            frame_inicio.grid_remove()
            frame_Mainmenu.grid_remove()
            frame_Qrcode.grid_remove()
            frame_Ayuda.grid_remove()
            frame_Reglas.grid_remove()
            frame_Renta.grid_remove()
            frame_Mapa.grid_remove()
            for widget in frame_Mainmenu.winfo_children():
                widget.destroy()
            frame_Mainmenu.grid()
            global etiqueta_de_foto_de_astronauta
            global mi_etiN
            global mi_etiA
            global mi_etiP
            global mi_etiCl
            global mi_etiMr
            global mi_etiSMr
            global mi_etiE
            global mi_etiM
            global mi_etiC

            etiqueta_de_foto_de_astronauta = Label(frame_Mainmenu, image=foto_de_astronauta).pack()
            archivo_informacion = open("C:/archivos_proyecto/info_registro.txt", 'r')
            archivo_informacion.seek(0)
            for linea in archivo_informacion.readlines():
                datos = linea.split(':')
                email = datos[0]
                if correo == email:
                    nombre = datos[1]
                    matricula = datos[2]
                    carrera = datos[3]
                    edificio = datos[4]
                    marca = datos[5]
                    sub_marca = datos[6]
                    color = datos[7]
                    anyo = datos[8]
                    placas = datos[9]

                    mi_etiN = Label(frame_Mainmenu, text=f"Nombre: {nombre.strip()}").pack()
                    mi_etiM = Label(frame_Mainmenu, text=f"Matricula: {matricula.strip()}").pack()
                    mi_etiC = Label(frame_Mainmenu, text=f"Carrera: {carrera.strip()}").pack()
                    mi_etiE = Label(frame_Mainmenu, text=f"Edificio más concurrido: {edificio.strip()}").pack()
                    mi_etiMr = Label(frame_Mainmenu, text=f"Marca: {marca.strip()}").pack()
                    mi_etiSMr = Label(frame_Mainmenu, text=f"Submarca: {sub_marca.strip()}").pack()
                    mi_etiCl = Label(frame_Mainmenu, text=f"Color: {color.strip()}").pack()
                    mi_etiA = Label(frame_Mainmenu, text=f"Año: {anyo.strip()}").pack()
                    mi_etiP = Label(frame_Mainmenu, text=f"Placas: {placas.strip()}").pack()
            archivo_informacion.close()

            boton_salir = ttk.Button(frame_Mainmenu, text="Cerrar Sesión", command=regreso_inicio_de_sesion)
            boton_salir.pack(side=BOTTOM)

        def Mapa():
            frame_inicio.grid_remove()
            frame_Mainmenu.grid_remove()
            frame_Qrcode.grid_remove()
            frame_Ayuda.grid_remove()
            frame_Reglas.grid_remove()
            frame_Renta.grid_remove()
            frame_Mapa.grid_remove()
            for widget in frame_Mapa.winfo_children():
                widget.destroy()
            frame_Mapa.grid()
            etiqueta_de_foto_de_mapa = Label(frame_Mapa, image=foto_de_mapa).pack()
            letra = ttk.Label(frame_Mapa, text="Letra: Representa la zona.")
            numero = ttk.Label(frame_Mapa, text="Número: Representa una fila.")
            letra.pack()
            numero.pack()

            hay_en_lugares = False
            hay_en_renta = False
            lugar_en_lugares = ""
            lugar_en_renta = ""

            archivo_lugares = open("C:/archivos_proyecto/lugares_de_estacionamiento.txt", 'r')
            archivo_lugares.seek(0)
            for linea in archivo_lugares.readlines():
                datos = linea.split(':')
                email = datos[0]
                if correo == email:
                    hay_en_lugares = True
                    lugar_en_lugares = datos[1]
            archivo_lugares.close()

            archivo_renta = open("C:/archivos_proyecto/lugares_de_renta.txt", 'r')
            archivo_renta.seek(0)
            for linea in archivo_renta.readlines():
                datos = linea.split(':')
                email = datos[0]
                if correo == email:
                    hay_en_renta = True
                    lugar_en_renta = datos[1]
            archivo_renta.close()

            if hay_en_renta == True:
                lugar_de_estacionamiento = Label(frame_Mapa, text=f"Lugar asignado: {lugar_en_renta.strip()}").pack()
            elif hay_en_lugares == True:
                lugar_de_estacionamiento = Label(frame_Mapa, text=f"Lugar asignado: {lugar_en_lugares.strip()}").pack()

            boton_regreso_inicio = ttk.Button(frame_Mapa, text="Cerrar Sesión", command=regreso_inicio_de_sesion)
            boton_regreso_inicio.pack(side=BOTTOM)

        def Reglas():
            frame_inicio.grid_remove()
            frame_Mainmenu.grid_remove()
            frame_Qrcode.grid_remove()
            frame_Ayuda.grid_remove()
            frame_Reglas.grid_remove()
            frame_Renta.grid_remove()
            frame_Mapa.grid_remove()
            for widget in frame_Reglas.winfo_children():
                widget.destroy()
            frame_Reglas.grid()

            regla = ttk.Label(frame_Reglas, text="Reglas del usos", font=fuente).pack()
            regla_1 = ttk.Label(frame_Reglas,
                                text="1.No usar otro lugar que no sea el que se le haya asignado.").pack()
            regla_2 = ttk.Label(frame_Reglas,
                                text="2.Asegurarse de que el codigo usado si corresponda al usuario y al vehiculo que ingreso.").pack()
            regla_3 = ttk.Label(frame_Reglas, text="3.No estorbar otros lugares de estacionamiento.").pack()
            regla_4 = ttk.Label(frame_Reglas, text="4.Evitar permanecer en el vehiculo al estacionarse.").pack()
            regla_5 = ttk.Label(frame_Reglas, text="5.Tener preparado el codigo al ingresar al campus.").pack()
            regla_6 = ttk.Label(frame_Reglas,
                                text="6.En caso de incumplir alguna de estas reglas sera acredor de una sancion.").pack()
            boton_salir = ttk.Button(frame_Reglas, text="Cerrar Sesión", command=regreso_inicio_de_sesion)
            boton_salir.pack(side=BOTTOM)

        def Ayuda():
            frame_inicio.grid_remove()
            frame_Mainmenu.grid_remove()
            frame_Qrcode.grid_remove()
            frame_Ayuda.grid_remove()
            frame_Reglas.grid_remove()
            frame_Renta.grid_remove()
            frame_Mapa.grid_remove()
            for widget in frame_Ayuda.winfo_children():
                widget.destroy()
            frame_Ayuda.grid()

            ayuda = Label(frame_Ayuda, text="Ayuda y Comentarios", font=fuente).pack()
            linea_1 = Label(frame_Ayuda, text="En caso de tener algun problema con").pack()
            linea_2 = Label(frame_Ayuda, text="el codigo generado, su informacion personal").pack()
            linea_3 = Label(frame_Ayuda, text="o con el uso de este servicio.").pack()
            linea_4 = Label(frame_Ayuda, text="Favor de comunicarse al siguiente mail:").pack()

            # Función para utilizar link
            def callback(url):
                webbrowser.open_new(url)

            link1 = Label(frame_Ayuda, text="generico@iteso.mx", fg="blue", cursor="hand2")
            link1.pack()
            link1.bind("<Button-1>", lambda e: callback("https://www.iteso.mx/contacto"))

            comentarios = Label(frame_Ayuda, text="Comentarios y Sugerencias", font=fuente).pack()
            linea_5 = Label(frame_Ayuda, text="Mandanos tu opinion sobre el servicio al siguiente mail").pack()
            linea_6 = Label(frame_Ayuda, text="Queremos escucharte:").pack()
            link1 = Label(frame_Ayuda, text="generico@iteso.mx", fg="blue", cursor="hand2")
            link1.pack()
            link1.bind("<Button-1>", lambda e: callback("https://www.iteso.mx/contacto"))

            boton_salir = ttk.Button(frame_Ayuda, text="Cerrar Sesión", command=regreso_inicio_de_sesion)
            boton_salir.pack(side=BOTTOM)

        def Renta():
            frame_inicio.grid_remove()
            frame_Mainmenu.grid_remove()
            frame_Qrcode.grid_remove()
            frame_Ayuda.grid_remove()
            frame_Reglas.grid_remove()
            frame_Renta.grid_remove()
            frame_Mapa.grid_remove()
            for widget in frame_Renta.winfo_children():
                widget.destroy()
            frame_Renta.grid()

            myLabel = Label(frame_Renta, text="Servicio de renta")
            myLabel.pack()

            linea_1 = Label(frame_Renta, text="Instrucciones para rentar:").pack()
            linea_2 = Label(frame_Renta,
                            text="En la primera casilla escriba la letra, en mayúsculas, de la zona").pack()
            linea_3 = Label(frame_Renta, text=" donde desea estacionarse.").pack()
            linea_4 = Label(frame_Renta, text="En las casillas restantes escriba simplente los números de lo que se "
                                              "le solicita").pack()
            linea_5 = Label(frame_Renta, text="Seleccione una fecha en el calendario, y a continuación "
                                              "pulse Guardar.").pack()

            texto = Label(frame_Renta, text="Ingrese los datos para apartar el cajon de estacionamiento.")
            texto.pack()

            letra_etiqueta = ttk.Label(frame_Renta, text="Letra: Representa la zona.").pack()
            zona = Entry(frame_Renta, width=55, borderwidth=2)
            zona.pack()
            zona.insert(0, "Letra")

            numero_etiqueta = ttk.Label(frame_Renta, text="Número: Representa una fila.").pack()
            numero = Entry(frame_Renta, width=55, borderwidth=2)
            numero.pack()
            numero.insert(0, "Número")

            horas_etiqueta = ttk.Label(frame_Renta, text="Horas: Representa las horas que planea rentar el espacio.").pack()
            horas = Entry(frame_Renta, width=55, borderwidth=2)
            horas.pack()
            horas.insert(0, "Horas")

            cal = Calendar(frame_Renta, selectmode="day", year=2020, month=12, day=3)
            cal.pack()

            # Función para el calendario
            def guardar_fecha():
                lugar_letra_numero = zona.get() + numero.get()
                diccionario_renta_de_lugares = {}
                diccionario_renta_de_lugares["lugar"] = lugar_letra_numero
                diccionario_renta_de_lugares["hora"] = horas.get()
                lista_de_otros = []
                archivo_lugares = open("C:/archivos_proyecto/lugares_de_estacionamiento.txt", 'r')
                archivo_lugares.seek(0)
                for linea in archivo_lugares.readlines():
                    datos = linea.split(':')
                    email = datos[0]
                    if correo == email:
                        diccionario_renta_de_lugares["correo"] = email
                archivo_lugares.close()

                archivo_renta = open("C:/archivos_proyecto/lugares_de_renta.txt", 'r')
                archivo_renta.seek(0)
                for linea in archivo_renta.readlines():
                    datos = linea.split(':')
                    email = datos[0]
                    lista_de_otros.append(email)
                    archivo_renta.close()
                if correo not in lista_de_otros:
                    linea1 = (diccionario_renta_de_lugares.get(
                        "correo") + ':' + diccionario_renta_de_lugares.get(
                        "lugar")
                              + ':' + diccionario_renta_de_lugares.get("hora") + "hr" + ":" + cal.get_date())
                    archivo_renta = open("C:/archivos_proyecto/lugares_de_renta.txt", "a")
                    archivo_renta.writelines(f"{linea1}\n")
                    archivo_renta.close()
                    correcto = messagebox.showinfo("Popup",
                                                   "La información de su renta se ha guardado en el sistema correctamente. "
                                                   "Favor de seleccionar una opción de pago.")
                else:
                    respuesta = messagebox.showerror("Popup",
                                                     "Ya se ha rentado un lugar con este correo. Por favor, espere"
                                                     " hasta el día de mañana para volver a rentar.")

            texto = Label(frame_Renta, text="")
            texto.pack()

            linea_1 = Label(frame_Renta, text="Usted va a el cajon con la ubicacion").pack()
            linea_2 = Label(frame_Renta, text="que ingreso previamente. Por X  horas con un costo de").pack()
            linea_3 = Label(frame_Renta, text=" 15 pesos la hora.").pack()
            linea_4 = Label(frame_Renta, text="En caso de sobrepasar el tiempo ingresado").pack()
            linea_5 = Label(frame_Renta, text=" se le hara un cargo de 35 pesos por cada hora extra.").pack()

            boton = ttk.Button(frame_Renta, text="Guardar", command=guardar_fecha)
            boton.pack()

            def callback(url):
                webbrowser.open_new(url)

            link1 = Label(frame_Renta, text="Pagar ahora", fg="blue", cursor="hand2")
            link1.pack()
            link1.bind("<Button-1>",
                       lambda e: callback("https://servicios.iteso.mx/apps/alumno/estado_cuenta/index.jsp"))

            link1 = Label(frame_Renta, text="Agregar pago a colegiatura", fg="blue", cursor="hand2")
            link1.pack()
            link1.bind("<Button-1>",
                       lambda e: callback("https://servicios.iteso.mx/apps/alumno/estado_cuenta/index.jsp"))

            boton_salir = ttk.Button(frame_Renta, text="Cerrar Sesión", command=regreso_inicio_de_sesion)
            boton_salir.pack(side=BOTTOM)

        def Qrcode():
            frame_inicio.grid_remove()
            frame_Mainmenu.grid_remove()
            frame_Qrcode.grid_remove()
            frame_Ayuda.grid_remove()
            frame_Reglas.grid_remove()
            frame_Renta.grid_remove()
            frame_Mapa.grid_remove()
            for widget in frame_Qrcode.winfo_children():
                widget.destroy()
            frame_Qrcode.grid()

            informacion_de_usuario_en_QR = []
            archivo_informacion = open("C:/archivos_proyecto/info_registro.txt", 'r')
            archivo_informacion.seek(0)
            for linea in archivo_informacion.readlines():
                datos = linea.split(':')
                email = datos[0]
                if correo == email:
                    informacion_de_usuario_en_QR.append(f"Nombre: {datos[1]}")
                    informacion_de_usuario_en_QR.append(f"Matrícula: {datos[2]}")
                    informacion_de_usuario_en_QR.append(f"Carrera: {datos[3]}")
                    informacion_de_usuario_en_QR.append(f"Edificio más concurrido: {datos[4]}")
                    informacion_de_usuario_en_QR.append(f"Marca: {datos[5]}")
                    informacion_de_usuario_en_QR.append(f"Sub marca: {datos[6]}")
                    informacion_de_usuario_en_QR.append(f"Color: {datos[7]}")
                    informacion_de_usuario_en_QR.append(f"Año: {datos[8]}")
                    informacion_de_usuario_en_QR.append(f"Placas: {datos[9]}")
            archivo_informacion.close()

            titulo = Label(frame_Qrcode, text="Codigo QR", font=fuente).grid(row=0, column=0)

            qr = qrcode.QRCode(
                version=1,
                box_size=8,
                border=1,
            )
            informacion = informacion_de_usuario_en_QR
            qr.add_data(informacion)
            imagen = qr.make_image(fill="black", back_color="white")
            imagen.save("prueba_qrcode.jpg")
            my_img = ImageTk.PhotoImage(Image.open("prueba_qrcode.jpg"))
            foto = Label(frame_Qrcode, image=my_img).grid(row=1, column=0)

            instrucciones_1 = ttk.Label(frame_Qrcode, text="Con este código QR usted podrá").grid(row=2, column=0)
            instrucciones_2 = ttk.Label(frame_Qrcode, text="entrar a las instalaciones del ITESO.").grid(row=3, column=0)

            boton_salir = ttk.Button(frame_Qrcode, text="Cerrar Sesión", command=regreso_inicio_de_sesion)
            boton_salir.grid(row=4, column=0)
            frame_Qrcode.mainloop()

        etiqueta_de_foto_de_astronauta = Label(frame_Mainmenu, image=foto_de_astronauta).pack()
        archivo_informacion = open("C:/archivos_proyecto/info_registro.txt", 'r')
        archivo_informacion.seek(0)
        for linea in archivo_informacion.readlines():
            datos = linea.split(':')
            email = datos[0]
            if correo == email:
                nombre = datos[1]
                matricula = datos[2]
                carrera = datos[3]
                edificio = datos[4]
                marca = datos[5]
                sub_marca = datos[6]
                color = datos[7]
                anyo = datos[8]
                placas = datos[9]

                mi_etiN = Label(frame_Mainmenu, text=f"Nombre: {nombre.strip()}").pack()
                mi_etiM = Label(frame_Mainmenu, text=f"Matricula: {matricula.strip()}").pack()
                mi_etiC = Label(frame_Mainmenu, text=f"Carrera: {carrera.strip()}").pack()
                mi_etiE = Label(frame_Mainmenu, text=f"Edificio más concurrido: {edificio.strip()}").pack()
                mi_etiMr = Label(frame_Mainmenu, text=f"Marca: {marca.strip()}").pack()
                mi_etiSMr = Label(frame_Mainmenu, text=f"Submarca: {sub_marca.strip()}").pack()
                mi_etiCl = Label(frame_Mainmenu, text=f"Color: {color.strip()}").pack()
                mi_etiA = Label(frame_Mainmenu, text=f"Año: {anyo.strip()}").pack()
                mi_etiP = Label(frame_Mainmenu, text=f"Placas: {placas.strip()}").pack()
        archivo_informacion.close()

        boton_MainMenu = ttk.Button(toolbar, text="Inicio", command=Inicio)
        boton_MainMenu.grid(row=0, column=0)
        boton_CodigoQr = ttk.Button(toolbar, text="Código QR", command=Qrcode)
        boton_CodigoQr.grid(row=1, column=0)
        boton_Mapa = ttk.Button(toolbar, text="Mapa", command=Mapa)
        boton_Mapa.grid(row=2, column=0)
        boton_Ayuda = ttk.Button(toolbar, text="Ayuda", command=Ayuda)
        boton_Ayuda.grid(row=3, column=0)
        boton_Reglas = ttk.Button(toolbar, text="Reglas", command=Reglas)
        boton_Reglas.grid(row=4, column=0)
        boton_Renta = ttk.Button(toolbar, text="Renta", command=Renta)
        boton_Renta.grid(row=5, column=0)

        boton_salir = ttk.Button(frame_Mainmenu, text="Cerrar Sesión", command=regreso_inicio_de_sesion)
        boton_salir.pack(side=BOTTOM)

    elif input_vacio == 1:
        respuesta = messagebox.showerror("Popup", "Las casillas de Usuario y Contraseña están vacias.")

    elif email_contra_incorrecto == 1:
        respuesta = messagebox.showerror("Popup", "El usuario o la contraseña no coinciden. Favor de reintentar.")

def Registro():
    frame_inicio.grid_remove()
    frame_registro.grid_remove()
    for widget in frame_registro.winfo_children():
        widget.destroy()
    frame_registro.grid()
    mylabel = Label(frame_registro, text="Ingrese todos los datos siguientes")
    mylabel.pack()
    contra_instrucciones = Label(frame_registro, text="Instrucciones para crear contraseña:").pack()
    info_caracteres = Label(frame_registro, text="La contraseña debe contener al menos 10 caractes.").pack()
    info_numero = Label(frame_registro, text="La contraseña deberá ser alfanumérico.").pack()
    info_mayus = Label(frame_registro, text="Al menos un carácter deberá ser letra mayúscula.").pack()
    info_usuario = Label(frame_registro, text="Informacíon del usuario:")
    info_usuario.pack()

    nombre_Completo = Label(frame_registro, text="Nombre Completo:").pack()
    usuario = Entry(frame_registro, width=55, borderwidth=2)
    usuario.pack()

    correo_del_ITESO = Label(frame_registro, text="Correo del ITESO:").pack()
    correo = Entry(frame_registro, width=55, borderwidth=2)
    correo.pack()

    contrasena = Label(frame_registro, text="Contraseña:").pack()
    contrasena = Entry(frame_registro, width=55, borderwidth=2)
    contrasena.pack()

    matricula = Label(frame_registro, text="Matricula").pack()
    matricula = Entry(frame_registro, width=55, borderwidth=2)
    matricula.pack()

    seleccionado = StringVar()
    carrera_texto= Label(frame_registro, text="Carrera").pack()
    seleccionado.set("Elija una opción")
    carrera = OptionMenu(frame_registro, seleccionado, "Elija una opcion","Arquitectura", "Arte y Creación", "Ciencias de la Comunicación",
                         "Ciencias de la Educación", "Comunicación y Artes Audiovisuales", "Derecho",
                         "Desarollo Inmobiliario Sustentable"
                         , "Diseño", "Diseño de Indumentaira y Moda", "Diseño Urbano y Arquitectura del Paisaje",
                         "Filosofia y Ciencias Sociales", "Gestión Cultural", "Nutrición y Ciencia de los Alimentos",
                         "Periodismo y Comunicación Pública"
                         , "Pscicología", "Relaciones Internacionales", "Publicidad y Comunicación Estratégica",
                         "Ingeniería de Alimentos", "Ingeniería Ambiental", "Ingeniería de Biotecnología",
                         "Ingeniería y CIencia de Datos"
                         , "Ingeniería Civil", "Ingeniería Electrónica", "Ingeniería en Empresas de Servicio",
                         "Ingeniería Financiera", "Ingeniería Industrial", "Ingeniería Mecánica",
                         "Ingeniería en Nanotecnología", "Ingeniería Química"
                         , "Ingeniería en Seguridad Informática y Redes", "Ingeniería en Sistemas Computacionales",
                         "Administración de Empresas y Emprendimiento", "Administración Financiera",
                         "Comercio y Negocios Globales"
                         , "Hospitalidad y Turismo", "Mercadoctenica", "Negocios y Mercados Digitales",
                         "Relaciones Industriales")
    carrera.pack()

    seleccionado1 = StringVar()
    seleccionado1.set("Elija una opción")
    edificio_texto = Label(frame_registro, text="Edificio más concurrido").pack()
    edificio = OptionMenu(frame_registro, seleccionado1,"Elija una opcion", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "Cafeteria (K)",
                          "M", "Ñ", "O", "Bibliotca (P)", "Q", "R", "S", "T", "Domo (U)", "W")
    edificio.pack()

    info_carro = Label(frame_registro, text="Informacion del vehículo:")
    info_carro.pack()

    seleccionado2 = StringVar()
    seleccionado2.set("Elija una opción")
    cmarca = Label(frame_registro, text="Marca").pack()
    marca = OptionMenu(frame_registro, seleccionado2, "Elija una opcion", "Acura", "Alfa Romeo", "Audi", "Bajaj", "BMW", "Buick",
                       "Cadillac", "Chevrolet", "Chysler", "Dinamo"
                       , "Dodge", "Ducati", "Ferrari", "Fiat", "Ford", "Harley Davidson", "Honda", "Hyundai", "Isuzu",
                       "Jaguar", "Jeep", "Kawasaki", "Kia",
                       "Land Rover", "Lincoln", "Mazda", "Mercedes Benz", "Mitsubishi", "Nissan", "Opel", "Peugeot",
                       "Pontiac", "Porsche", "RAM", "Renault", "Rover"
                       , "Saturn", "Seat", "Smart", "Subaru", "Suzuki", "Tesla", "Toyota", "Vespa", "VolksWagen",
                       "Volvo", "Yamaha")
    marca.pack()

    sub_marca = Label(frame_registro, text="Submarca (Modelo):").pack()
    sub_marca = Entry(frame_registro, width=55, borderwidth=2)
    sub_marca.pack()

    color = Label(frame_registro, text="Color:").pack()
    color = Entry(frame_registro, width=55, borderwidth=2)
    color.pack()

    anio = Label(frame_registro, text="Año:").pack()
    anio = Entry(frame_registro, width=55, borderwidth=2)
    anio.pack()

    placas = Label(frame_registro, text="Placas:").pack()
    placas = Entry(frame_registro, width=55, borderwidth=2)
    placas.pack()

    def myClick():
        contMayus = 0
        contMin = 0
        contAlfanum = 0
        correo_usado = False
        lugar_estacionamiento = ""
        lista_edificios_seccion_AEFB = ["T", "F", "I", "D", "J", "E", "G"]
        lugares_AEFB = ["A1", "A2", "A3", "E1", "E2", "B1", "B2", "B3", "F1", "F2", "F3"]
        lista_edificios_seccion_CGDH = ["W", "C", "B", "A", "M", "Ñ", "Domo (U)", "O"]
        lugares_CGDH = ["C1", "C2", "C3", "D1", "D2", "G1", "G2", "G3", "H1"]
        lista_edificios_seccion_JKM = ["R", "S", "Q", "H"]
        lugares_JKM = ["J1", "J2", "J3", "J4", "J5", "K1", "K2", "K3", "M1", "M2", "M3", "M4"]
        lista_edificios_seccion_NLHI = ["Cafeteria (K)", "Bibliotca (P)"]
        lugares_NLHI = ["L1", "L2", "N1", "N2", "N3", "H2", "H3", "I1", "I2", "I3", "I4"]

        if seleccionado1.get() in lista_edificios_seccion_AEFB:
            if seleccionado1.get() == "T" or seleccionado1.get() == "F":
                lugar_estacionamiento = lugares_AEFB[random.randint(0, 4)]
            elif seleccionado1.get() == "I" or seleccionado1.get() == "D" or seleccionado1.get() == "J":
                lugar_estacionamiento = lugares_AEFB[random.randint(0, 4)]
            elif seleccionado1.get() == "E" or seleccionado1.get() == "G":
                lugar_estacionamiento = lugares_AEFB[random.randint(5, 10)]

        elif seleccionado1.get() in lista_edificios_seccion_CGDH:
            if seleccionado1.get() == "W" or seleccionado1.get() == "C" or seleccionado1.get() == "B":
                lugar_estacionamiento = lugares_CGDH[random.randint(0, 5)]
            elif seleccionado1.get() == "A" or seleccionado1.get() == "M" or seleccionado1.get() == "Domo (U)":
                lugar_estacionamiento = lugares_CGDH[random.randint(2, 7)]
            elif seleccionado1.get() == "Ñ" or seleccionado1.get() == "O":
                lugar_estacionamiento = lugares_CGDH[random.randint(3, 8)]

        elif seleccionado1.get() in lista_edificios_seccion_JKM:
            if seleccionado1.get() == "R" or seleccionado1.get() == "H":
                lugar_estacionamiento = lugares_JKM[random.randint(3, 11)]
            elif seleccionado1.get() == "S" or seleccionado1.get() == "Q":
                lugar_estacionamiento = lugares_JKM[random.randint(0, 7)]

        elif seleccionado1.get() in lista_edificios_seccion_NLHI:
            if seleccionado1.get() == "Cafeteria (K)" or seleccionado1.get() == "Bibliotca (P)":
                lugar_estacionamiento = lugares_NLHI[random.randint(0, 10)]

        if len(contrasena.get()) >= 10:
            for letra in contrasena.get():
                if letra.isupper():
                    contMayus += 1
                if letra.islower():
                    contMin += 1
                if letra.isalnum():
                    contAlfanum += 1

        archivo_informacion = open("C:/archivos_proyecto/info_registro.txt", "r")
        for linea in archivo_informacion.readlines():
            datos = linea.split(":")
            correo_de_archivo = datos[0]
            if correo.get() == correo_de_archivo:
                correo_usado = True
        archivo_informacion.close()

        if contMayus > 0 and contMin > 0 and contAlfanum > 0 and '@iteso.mx' in correo.get() and correo_usado == False:
            global correcto
            correcto = messagebox.showinfo("Popup", "La información se ha guardado en el sistema correctamente.")

            correo.get()
            contrasena.get()
            usuario.get()
            matricula.get()
            seleccionado.get()
            seleccionado1.get()
            seleccionado2.get()
            sub_marca.get()
            color.get()
            anio.get()
            placas.get()
            dicc_Registro = {}
            dicc_Registro["correo"] = correo.get()
            dicc_Registro["contraseña"] = contrasena.get()
            dicc_Registro["usuario"] = usuario.get()
            dicc_Registro["matricula"] = matricula.get()
            dicc_Registro["seleccion"] = seleccionado.get()
            dicc_Registro["seleccion1"] = seleccionado1.get()
            dicc_Registro["seleccion2"] = seleccionado2.get()
            dicc_Registro["sub marca"] = sub_marca.get()
            dicc_Registro["color"] = color.get()
            dicc_Registro["año"] = anio.get()
            dicc_Registro["placas"] = placas.get()
            linea = (dicc_Registro.get("correo") + ':' + dicc_Registro.get("usuario") + ':' + dicc_Registro.get(
                "matricula")
                     + ':' + dicc_Registro.get("seleccion") + ':' + dicc_Registro.get("seleccion1") + ':'
                     + dicc_Registro.get("seleccion2") + ':' + dicc_Registro.get("sub marca") + ':'
                     + dicc_Registro.get("color") + ':' + dicc_Registro.get("año") + ':' + dicc_Registro.get("placas"))
            linea2 = dicc_Registro.get("correo") + ':' + dicc_Registro.get("contraseña")
            linea3 = dicc_Registro.get("correo") + ':' + lugar_estacionamiento
            archivo_informacion = open("C:/archivos_proyecto/info_registro.txt", "a")
            archivo_informacion.writelines(f"{linea}\n")
            archivo_informacion.close()
            archivo_usuario_y_contra = open("C:/archivos_proyecto/usuario_y_contrasena.txt", "a")
            archivo_usuario_y_contra.writelines(f"{linea2}\n")
            archivo_usuario_y_contra.close()
            archivo_lugares = open("C:/archivos_proyecto/lugares_de_estacionamiento.txt", "a")
            archivo_lugares.writelines(f"{linea3}\n")
            archivo_lugares.close()
        elif contMayus == 0 and contMin == 0 and contAlfanum == 0:
            global error_caracteres_contra
            error_caracteres_contra = messagebox.showerror("Popup",
                                                           "La contraseña no es segura porque no sigue con los parametros indicados.")

        if correo_usado == True:
            respuesta = messagebox.showerror("Popup",
                                             "El correo ya ha sido registrado, por favor utilice otro correo.")

        if '@iteso.mx' not in correo.get():
            global error_caracteres_correo
            error_caracteres_correo = messagebox.showerror("Popup",
                                                        "El correo debe contener @iteso.mx.")

        if seleccionado.get() == "Elija una opción" or seleccionado1.get() == "Elija una opción" or seleccionado2.get() == "Elija una opción":
            respuesta = messagebox.showerror("Popup","Alguna de las casillas de las listas desplegables están vacias, favor de elegir alguna opcion.")

    myButton = ttk.Button(frame_registro, text="Guardar", command=myClick)
    myButton.pack()

    boton_regreso_InicioS = ttk.Button(frame_registro, text="Iniciar Sesión", command=regreso_inicio_de_sesion)
    boton_regreso_InicioS.pack()


def cambioCon():
    frame_inicio.grid_remove()
    frame_cambioCon.grid_remove()
    for widget in frame_cambioCon.winfo_children():
        widget.destroy()
    frame_cambioCon.grid()

    myLabel = Label(frame_cambioCon, text="Cambio de contraseña", font=fuente)
    myLabel.pack()

    contra_instrucciones = Label(frame_cambioCon, text="Instrucciones para crear contraseña:").pack()
    info_caracteres = Label(frame_cambioCon, text="La contraseña debe contener al menos 10 caractes.").pack()
    info_numero = Label(frame_cambioCon, text="La contraseña deberá ser alfanumérico.").pack()
    info_mayus = Label(frame_cambioCon, text="Al menos un carácter deberá ser letra mayúscula.").pack()

    etiqueta_de_correo = Label(frame_cambioCon, text="Correo del ITESO:")
    etiqueta_de_correo.pack()
    correo_input = Entry(frame_cambioCon, width=55, borderwidth=2)
    correo_input.pack()

    etiqueta_contrasena_antigua = Label(frame_cambioCon, text="Ingrese la contraseña que desea cambiar:")
    etiqueta_contrasena_antigua.pack()
    contrasena_antigua = Entry(frame_cambioCon, width=55, borderwidth=2)
    contrasena_antigua.pack()
    contrasena_antigua.get()

    etiqueta_contrasena_nueva = Label(frame_cambioCon, text="Ingrese su nueva contraseña:")
    etiqueta_contrasena_nueva.pack()
    nueva_contrasena = Entry(frame_cambioCon, width=55, borderwidth=2)
    nueva_contrasena.pack()
    nueva_contrasena.get()

    def cambiar_contra():
        lista_otros_datos = []
        cambio_correcto = False
        hay_algo = False
        contra_nueva_correcta = False
        vacio = False
        contrasena_incorrecta = False
        nueva_linea = ""
        contMayus = 0
        contMin = 0
        contAlfanum = 0

        if len(contrasena_antigua.get()) == 0 or len(correo_input.get()) == 0 or len(nueva_contrasena.get()) == 0:
            respuesta = messagebox.showerror("Popup", "Alguna o todas las casillas están vacias.")
            vacio = True

        if len(nueva_contrasena.get()) >= 10:
            for letra in nueva_contrasena.get():
                if letra.isupper():
                    contMayus += 1
                if letra.islower():
                    contMin += 1
                if letra.isalnum():
                    contAlfanum += 1

        if contMayus > 0 and contMin > 0 and contAlfanum > 0:
            contra_nueva_correcta = True

        elif contra_nueva_correcta == False:
            global error_caracteres_contra
            error_caracteres_contra = messagebox.showerror("Popup",
                                                           "La contraseña no es segura porque no sigue con los parametros indicados.")
            contrasena_incorrecta = True

        if contra_nueva_correcta == True and vacio == False and contrasena_incorrecta == False:
            archivo_cambio_contra_leer = open("C:/archivos_proyecto/usuario_y_contrasena.txt", "r")
            archivo_cambio_contra_leer.seek(0)
            for linea in archivo_cambio_contra_leer.readlines():
                datos = linea.split(":")
                correo = datos[0]
                contrasena = datos[1]
                if correo.strip() == correo_input.get() and contrasena_antigua.get() == contrasena.strip():
                    nueva_linea = f"{correo}:{nueva_contrasena.get()}\n"
                    cambio_correcto = True
                else:
                    lista_otros_datos.append(correo)
                    lista_otros_datos.append(contrasena)
                    hay_algo = True
            archivo_cambio_contra_leer.close()

            if cambio_correcto == True:
                archivo_cambio_contra_escribir = open("C:/archivos_proyecto/usuario_y_contrasena.txt", "w")
                archivo_cambio_contra_escribir.write(nueva_linea)
                if hay_algo == True:
                    contador_lista = len(lista_otros_datos)
                    correo_de_lista = 0
                    contrasena_de_lista = 1
                    while contador_lista >= 2:
                        nueva_linea_de_lista = f"{lista_otros_datos[correo_de_lista]}:{lista_otros_datos[contrasena_de_lista]}"
                        archivo_cambio_contra_escribir.write(nueva_linea_de_lista)
                        correo_de_lista += 2
                        contrasena_de_lista += 2
                        contador_lista -= 2
                correcto = messagebox.showinfo("Popup",
                                                   "El correo y la contraseña nueva se han guardado en el sistema correctamente.")
                archivo_cambio_contra_escribir.close()
            else:
                respuesta = messagebox.showerror("Popup", "El correo y la contraseña antigua no coinciden.")



    boton_guardar_contrasena = ttk.Button(frame_cambioCon, text="Guardar", command=cambiar_contra)
    boton_guardar_contrasena.pack()

    boton_regreso_inicio = ttk.Button(frame_cambioCon, text="Iniciar Sesión", command=regreso_inicio_de_sesion)
    boton_regreso_inicio.pack()

mi_eti = Label(frame_inicio, text="Inicio de Sesión").pack()
mi_etiU = Label(frame_inicio, text="Correo del ITESO:", font=fuente)
mi_etiU.pack()
in_putU = Entry(frame_inicio, width=55, borderwidth=2)
in_putU.pack()

mi_etiC = Label(frame_inicio, text="Contraseña:", font=fuente)
mi_etiC.pack()
in_putC = Entry(frame_inicio, width=55, borderwidth=2)
in_putC.pack()

botonInicio = ttk.Button(frame_inicio, text="Ingresar", command=inicio)
botonInicio.pack()
botonInicio.focus_set()
botonRegistro = ttk.Button(frame_inicio, text="¿Nuevo Usuario?", command=Registro)
botonRegistro.pack()

etiqueta1 = Label(frame_inicio, text="¿Tienes problemas para acceder?").pack()
etiqueta2 = Label(frame_inicio, text="Por favor envía un correo electrónico a:").pack()

# Función para utilizar link
def callback(url):
    webbrowser.open_new(url)


link1 = Label(frame_inicio, text="generico@iteso.mx", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://www.iteso.mx/contacto"))

boton_NuevaContra = ttk.Button(frame_inicio, text="¿Deseas cambiar tu contraseña?", command=cambioCon)
boton_NuevaContra.pack()

ventana.mainloop()
