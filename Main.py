"""
ARCHIVO PRINCIPAL - Main.py (Con cierre limpio)
"""
import customtkinter as ctk
from Modelo import SistemaExpertoPrologInteractivo
from Vista import VistaSistemaExperto
from Controlador import ControladorSistemaExperto
from tkinter import messagebox
import os

def main():
    root = ctk.CTk()

    # Rutas dinámicas
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_prolog = os.path.join(directorio_actual, "youtube.pl")

    if not os.path.exists(archivo_prolog):
        archivo_prolog = r"C:\Users\Administrator\Downloads\youtube (1).pl"

    try:
        modelo = SistemaExpertoPrologInteractivo(archivo_prolog)
        vista = VistaSistemaExperto(root)
        controlador = ControladorSistemaExperto(vista, modelo)

        # === AGREGAR ESTA FUNCIÓN DE CIERRE ===
        def cerrar_aplicacion():
            # 1. Detenemos el cerebro (el hilo del modelo)
            if modelo:
                modelo.cancelar()
            # 2. Destruimos la ventana
            root.destroy()
            # 3. Forzamos salida del sistema (opcional)
            os._exit(0)

        # Conectar la X de la ventana a nuestra función
        root.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)
        # ======================================

        vista.ejecutar()

    except Exception as e:
        messagebox.showerror("Error crítico", f"No se pudo cargar el sistema:\n{e}")
        root.destroy()

if __name__ == "__main__":
    main()