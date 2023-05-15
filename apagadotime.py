import tkinter as tk
import os
import ctypes
import subprocess
import sys

   # Establecer la ventana principal de la consola de comandos como oculta
if hasattr(sys, 'frozen'):
    
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
   # Se define el mensaje a mostrar si se presiona un boton
def mostrar_mensaje():
    etiqueta.config(text="TAMBIEN PUEDES CANCELAR EL APAGADO")
    etiqueta.config(fg="white")


ventana = tk.Tk()
ventana.title("ApagadoTime")
ventana.geometry("400x500")
ventana.configure(bg="#333333")

fuente_grande2 = ("Arial", 18)
fuente_grande = ("Arial", 14)

boton = tk.Button(ventana, text="INGRESA EN CUANTO TIEMPO DEBE APAGARSE LA PC", command=mostrar_mensaje)
boton.pack(pady=10)

etiqueta = tk.Label(ventana, text="")
etiqueta.configure(bg="#333333")
etiqueta.pack(pady=10)


def apagar_equipo():
    horas = entry_horas.get()
    minutos = entry_minutos.get()
    tiempo_apagado = f"{horas}:{minutos}:00"
    
    segundos = int(horas) * 3600 + int(minutos) * 60

    # Ejecutar el comando de apagado con el tiempo especificado en segundos
    os.system(f"shutdown -s -t {segundos}")



def cancelar_apagado():
    os.system("shutdown -a")
    etiqueta_mensaje.config(text="El apagado ha sido cancelado")

etiqueta_mensaje = tk.Label(ventana, text="", font=fuente_grande)
etiqueta_mensaje.configure(bg="#333333")
etiqueta_mensaje.pack(pady=10)


label_horas = tk.Label(ventana, text="Horas:", font=fuente_grande)
label_horas.pack()

entry_horas = tk.Entry(ventana)
entry_horas.insert(0, "0")  # Establecer el valor predeterminado en "0"
entry_horas.pack()

label_minutos = tk.Label(ventana, text="Minutos:", font=fuente_grande)
label_minutos.pack()

entry_minutos = tk.Entry(ventana)
entry_minutos.insert(0, "15")  # Establecer el valor predeterminado en "15"
entry_minutos.pack()

boton_apagar = tk.Button(ventana, text="Apagar", font=fuente_grande2, command=apagar_equipo)
boton_apagar.pack()

boton_cancelar = tk.Button(ventana, text="Cancelar Apagado", command=cancelar_apagado, font=fuente_grande)
boton_cancelar.pack()




ventana.mainloop()
