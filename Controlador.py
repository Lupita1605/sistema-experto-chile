"""
CONTROLADOR - Coordina modelo y vista
"""
from tkinter import messagebox


class ControladorSistemaExperto:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        self.vista.set_controlador(self)

        # Mostrar mensaje inicial
        self.vista.agregar_mensaje_sistema(
            "¡Bienvenido al sistema de diagnóstico inteligente! 🌱",
            tipo="bienvenida"
        )
        self.vista.agregar_mensaje_sistema(
            "Presione 'Iniciar Diagnóstico' para comenzar el análisis.",
            tipo="info"
        )

    def iniciar_diagnostico(self):
        """Inicia el proceso de diagnóstico"""
        # Limpiar chat
        self.vista.limpiar_chat()

        self.vista.agregar_mensaje_sistema("Iniciando diagnóstico...", tipo="info")
        self.vista.agregar_mensaje_sistema("Responda 'SÍ' o 'NO' a cada pregunta.", tipo="info")

        # Deshabilitar botón iniciar
        self.vista.habilitar_boton_iniciar(False)
        self.vista.habilitar_boton_reiniciar(False)

        # Iniciar diagnóstico
        self.modelo.iniciar_diagnostico_interactivo(
            callback_pregunta=self.vista.mostrar_pregunta,
            callback_resultado=self.mostrar_resultado
        )

    def responder(self, respuesta):
        """Usuario responde a la pregunta"""
        # Deshabilitar botones
        self.vista.habilitar_botones_respuesta(False)

        # Agregar respuesta al chat
        self.vista.agregar_respuesta(respuesta)

        # Enviar respuesta al modelo
        self.modelo.responder(respuesta)

    def mostrar_resultado(self, diagnostico, exitoso, error=None):
        """Maneja el resultado del diagnóstico"""
        # Mostrar resultado en la vista
        self.vista.mostrar_resultado(diagnostico, exitoso, error)

    def reiniciar(self):
        """Reinicia el sistema"""
        # Cancelar proceso en el modelo
        self.modelo.cancelar()

        # Limpiar interfaz
        self.vista.ocultar_pregunta_actual()
        self.vista.limpiar_chat()

        self.vista.agregar_mensaje_sistema("Sistema reiniciado correctamente.", tipo="info")
        self.vista.agregar_mensaje_sistema("Presione 'Iniciar Diagnóstico' para comenzar.", tipo="info")

        self.vista.habilitar_boton_iniciar(True)
        self.vista.habilitar_boton_reiniciar(False)