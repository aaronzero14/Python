import tkinter as tk
import platform
import socket
import requests
import webbrowser  # Importar el módulo webbrowser para abrir el enlace

# Función para abrir el enlace al portafolio
def abrir_portafolio():
    webbrowser.open("https://aaron-dev-fullstack.vercel.app/")  # Reemplaza esto con la URL de tu portafolio
def abrir_portafolio_1():
    webbrowser.open("https://github.com/aaronzero14")  # Reemplaza esto con la URL de tu portafolio


# comando para crear ---> exe pyinstaller --onefile tu_script.py
# Función para obtener y mostrar los datos del sistema
def mostrar_info_sistema():
    sistema_operativo = platform.system()
    version = platform.version()
    arquitectura = platform.architecture()
    procesador = platform.processor()
    direccion_ip = socket.gethostbyname(socket.gethostname())
    realese = platform.release()
   
    Version = 0.1
    Lemua = "Aaron Padilla"
    price =  "Version en Desarrollo - Codigo Abierto"
    Texto_Unido = "\n Version :  {} \n Diseñado por :  {} \n Software : {} " # usa el metodo format para unir los elementos con las llaves --> {}
    #Puede utilizar números de índice {0} {2} {1} para asegurarse de que los argumentos se coloquen en los marcadores de posición correctos

    # Obtener la dirección IP pública utilizando httpbin.org
    try:
        response = requests.get("https://httpbin.org/ip")
        data = response.json()
        direccion_ip_publica = data["origin"]
    except Exception as e:
        direccion_ip_publica = "Error al obtener IP pública"

    texto_info.config(text=f"Sistema Operativo: {sistema_operativo}\n"
                            f"Versión: {version}\n"
                            f"Arquitectura: {arquitectura}\n"
                            f"Procesador: {procesador}\n"
                            f"Dirección IP Local: {direccion_ip}\n"
                            f"Dirección IP Pública: {direccion_ip_publica}\n"
                            f"Versión del sistema operativo. :  {realese}\n"
                            f"{(Texto_Unido.format(Version, Lemua, price))}"
                            )

# Configuración de la ventana principal
root = tk.Tk()
root.title("Información del Host")
root.configure(bg="black")  # Configurar fondo negro para la ventana principal

# Etiqueta para mostrar los datos del sistema
texto_info = tk.Label(root, font=("Arial", 12), justify='left', bg="black", fg="lime green")
texto_info.pack(padx=20, pady=20)

# Enlace a tu portafolio
enlace_portafolio = tk.Label(root, text="Visita mi portafolio",bg="black", fg="green", cursor="hand2")
enlace_portafolio.pack()
enlace_portafolio.bind("<Button-1>", lambda e: abrir_portafolio())  # Abrir enlace al hacer clic

enlace_portafolio_1 = tk.Label(root, text="Proyectos en Github",bg="black", fg="green", cursor="hand2")
enlace_portafolio_1.pack()
enlace_portafolio_1.bind("<Button-1>", lambda e: abrir_portafolio_1())  # Abrir enlace al hacer clic

# Botón para obtener la información del sistema
boton_mostrar_info = tk.Button(root, text="Mostrar Información del Sistema", command=mostrar_info_sistema, bg="black", fg="lime green")
boton_mostrar_info.pack(padx=40, pady=20)




# Iniciar el bucle principal de la aplicación
root.mainloop()