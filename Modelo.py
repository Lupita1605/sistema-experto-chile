"""
MODELO - Sistema Experto Prolog (Corrección de Error de Permisos)
"""
from pyswip import Prolog
import os
import threading
import re
import time

class SistemaExpertoPrologInteractivo:
    def __init__(self, archivo_prolog):
        self.prolog = Prolog()
        self.archivo_prolog = archivo_prolog
        self.reglas = []

        self.cargar_base_conocimiento()
        self.extraer_reglas_de_texto()

        self.proceso_activo = False
        self.callback_pregunta = None
        self.callback_resultado = None

    def cargar_base_conocimiento(self):
        if not os.path.exists(self.archivo_prolog):
            raise FileNotFoundError(f"No se encuentra el archivo: {self.archivo_prolog}")

        # 1. Cargar el archivo Prolog original
        ruta = self.archivo_prolog.replace("\\", "/")
        self.prolog.consult(ruta)

        # ===================================================================
        # CORRECCIÓN DEL ERROR DE PERMISOS
        # ===================================================================
        try:
            # Paso 1: Forzamos el borrado de la regla 'preguntar' original.
            # Esto elimina el bloqueo de "static_procedure".
            list(self.prolog.query("abolish(preguntar/1)"))

            # Paso 2: Ahora sí podemos inyectar nuestra regla falsa.
            # Esto evita que Prolog intente usar la consola negra.
            list(self.prolog.query("asserta((preguntar(_) :- fail))"))
        except Exception as e:
            print(f"Advertencia al modificar Prolog: {e}")

    def extraer_reglas_de_texto(self):
        """Lee el archivo .pl como texto para saber qué preguntar"""
        self.reglas = []
        try:
            with open(self.archivo_prolog, "r", encoding="utf-8") as f:
                contenido = f.read()

            # Regex para encontrar: enfermedad(X, 'Nombre') :- ...
            regex_regla = r"enfermedad\s*\([^,]+,\s*['\"]?([^'\")]+)['\"]?\)\s*:-(.*?)\."
            coincidencias = re.findall(regex_regla, contenido, re.DOTALL)

            for enfermedad, cuerpo in coincidencias:
                # Regex para encontrar: tiene(X, sintoma)
                regex_sintoma = r"tiene\s*\([^,]+,\s*([a-z0-9_]+)\)"
                sintomas = re.findall(regex_sintoma, cuerpo)

                if sintomas:
                    self.reglas.append({
                        "enfermedad": enfermedad,
                        "sintomas": sintomas
                    })

            print(f"DEBUG: Reglas cargadas correctamente: {len(self.reglas)}")

        except Exception as e:
            print(f"Error leyendo archivo Prolog: {e}")

    def limpiar_memoria(self):
        """Limpia hechos anteriores"""
        try:
            list(self.prolog.query("borrar_memoria"))
        except:
            self.prolog.retractall("confirmado(_)")
            self.prolog.retractall("descartado(_)")

        # IMPORTANTE: Re-asegurar que preguntar siga desactivado
        try:
            list(self.prolog.query("abolish(preguntar/1)"))
            list(self.prolog.query("asserta((preguntar(_) :- fail))"))
        except:
            pass

    def iniciar_diagnostico_interactivo(self, callback_pregunta, callback_resultado):
        self.callback_pregunta = callback_pregunta
        self.callback_resultado = callback_resultado
        self.limpiar_memoria()

        thread = threading.Thread(target=self._motor_de_inferencia, daemon=True)
        thread.start()

    def _motor_de_inferencia(self):
        self.proceso_activo = True

        try:
            while self.proceso_activo:
                time.sleep(0.1)

                # 1. CONSULTAR PROLOG
                soluciones = list(self.prolog.query("enfermedad(_, Diagnostico)"))

                if soluciones:
                    nombre = soluciones[0]['Diagnostico']
                    if isinstance(nombre, bytes):
                        nombre = nombre.decode('utf-8')
                    self.callback_resultado(str(nombre), True)
                    return

                # 2. BUSCAR SIGUIENTE PREGUNTA
                sintoma = self._obtener_siguiente_pregunta()

                if not sintoma:
                    self.callback_resultado(None, False)
                    return

                # 3. INTERACCIÓN GUI
                respuesta = self._preguntar_sintoma(sintoma)

                # 4. GUARDAR RESPUESTA EN PROLOG
                if respuesta is True:
                    self.prolog.assertz(f"confirmado({sintoma})")
                elif respuesta is False:
                    self.prolog.assertz(f"descartado({sintoma})")
                else:
                    return # Cancelado

        except Exception as e:
            print(f"Error crítico en motor: {e}")
            self.callback_resultado(None, False, str(e))
        finally:
            self.proceso_activo = False

    def _obtener_siguiente_pregunta(self):
        for regla in self.reglas:
            posible = True
            for sintoma in regla['sintomas']:
                if list(self.prolog.query(f"descartado({sintoma})")):
                    posible = False
                    break

                if list(self.prolog.query(f"confirmado({sintoma})")):
                    continue

                return sintoma

        return None

    def _preguntar_sintoma(self, sintoma):
        self.respuesta_usuario = None
        self.callback_pregunta(sintoma)

        while self.respuesta_usuario is None and self.proceso_activo:
            time.sleep(0.1)

        return self.respuesta_usuario

    def responder(self, respuesta):
        self.respuesta_usuario = respuesta

    def cancelar(self):
        self.proceso_activo = False
        self.respuesta_usuario = False
        self.limpiar_memoria()