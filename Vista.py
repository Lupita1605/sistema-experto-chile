import customtkinter as ctk
from tkinter import messagebox
from PIL import Image  # Importar PIL para manejar imágenes
import os


class VistaSistemaExperto:
    def __init__(self, root):
        self.root = root
        self.controlador = None

        # Configuración de CustomTkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # Título sin el emoji
        self.root.title("Sistema Experto - Diagnóstico de Chile Jalapeño")
        self.root.geometry("900x700")

        # Ruta base para encontrar la imagen
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        self.crear_interfaz()

    def set_controlador(self, controlador):
        """Establece el controlador"""
        self.controlador = controlador

    def crear_interfaz(self):
        # Frame principal con gradiente simulado
        main_frame = ctk.CTkFrame(self.root, fg_color="#1a1a1a")
        main_frame.pack(fill="both", expand=True, padx=0, pady=0)

        # ===== ENCABEZADO CON DISEÑO MEJORADO (MODIFICADO) =====
        header_frame = ctk.CTkFrame(main_frame, fg_color="#0d7377", corner_radius=0)
        header_frame.pack(fill="x", pady=0)

        # Contenedor del contenido del header (centrado)
        header_content = ctk.CTkFrame(header_frame, fg_color="transparent")
        header_content.pack(pady=20, padx=20)

        # 1. CARGA DE IMAGEN
        try:
            image_path = os.path.join(self.base_dir, "chile.png")
            pil_image = Image.open(image_path)
            # Ajusté ligeramente el tamaño para que sea más armónico
            self.chile_icon = ctk.CTkImage(light_image=pil_image,
                                           dark_image=pil_image,
                                           size=(100, 80))  # Tamaño más compacto y estético
        except Exception as e:
            print(f"Error al cargar la imagen 'chile.png': {e}")
            self.chile_icon = None

        # 2. COLUMNA DE IMAGEN (Izquierda)
        if self.chile_icon:
            icon_label = ctk.CTkLabel(
                header_content,
                text="",
                image=self.chile_icon
            )
            # padx=(0, 20) da espacio entre la imagen y el texto a la derecha
            icon_label.pack(side="left", padx=(0, 20))

        # 3. COLUMNA DE TEXTO (Derecha)
        text_container = ctk.CTkFrame(header_content, fg_color="transparent")
        text_container.pack(side="left")

        # Título Principal
        header = ctk.CTkLabel(
            text_container,
            text="Sistema Experto de Diagnóstico",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white",
            anchor="w"  # Alineado a la izquierda
        )
        header.pack(anchor="w")

        # Subtítulo
        subheader = ctk.CTkLabel(
            text_container,
            text="Chile Jalapeño · Detección Inteligente",
            font=ctk.CTkFont(size=16),
            text_color="#e0f7fa",
            anchor="w"  # Alineado a la izquierda
        )
        subheader.pack(anchor="w", pady=(5, 0))

        # ===== ÁREA DE CONVERSACIÓN (RESTO DEL CÓDIGO IGUAL) =====
        chat_container = ctk.CTkFrame(main_frame, fg_color="transparent")
        chat_container.pack(pady=20, padx=20, fill="both", expand=True)

        chat_label = ctk.CTkLabel(
            chat_container,
            text="💬 Conversación",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#0d7377",
            anchor="w"
        )
        chat_label.pack(anchor="w", pady=(0, 10))

        self.chat_frame = ctk.CTkScrollableFrame(
            chat_container,
            width=740,
            height=280,
            corner_radius=15,
            fg_color="#252525",
            border_width=2,
            border_color="#0d7377"
        )
        self.chat_frame.pack(fill="both", expand=True)

        # ===== ÁREA DE PREGUNTA ACTUAL =====
        self.pregunta_frame = ctk.CTkFrame(
            main_frame,
            corner_radius=15,
            fg_color="#1e3d59",
            border_width=2,
            border_color="#0d7377"
        )
        self.pregunta_frame.pack(pady=15, padx=20, fill="x")
        self.pregunta_frame.pack_forget()

        # Icono y etiqueta de pregunta
        pregunta_header = ctk.CTkFrame(self.pregunta_frame, fg_color="transparent")
        pregunta_header.pack(pady=(15, 10))

        icono_pregunta = ctk.CTkLabel(
            pregunta_header,
            text="🔍",
            font=ctk.CTkFont(size=24)
        )
        icono_pregunta.pack()

        self.pregunta_label = ctk.CTkLabel(
            self.pregunta_frame,
            text="",
            font=ctk.CTkFont(size=18, weight="bold"),
            wraplength=650,
            text_color="white"
        )
        self.pregunta_label.pack(pady=(0, 20), padx=30)

        # Botones de respuesta
        botones_frame = ctk.CTkFrame(self.pregunta_frame, fg_color="transparent")
        botones_frame.pack(pady=(0, 20))

        self.btn_si = ctk.CTkButton(
            botones_frame,
            text="✓ SÍ",
            command=self.responder_si,
            width=180,
            height=55,
            font=ctk.CTkFont(size=18, weight="bold"),
            fg_color="#2e7d32",
            hover_color="#1b5e20",
            corner_radius=12,
            border_width=2,
            border_color="#4caf50"
        )
        self.btn_si.pack(side="left", padx=15)

        self.btn_no = ctk.CTkButton(
            botones_frame,
            text="✗ NO",
            command=self.responder_no,
            width=180,
            height=55,
            font=ctk.CTkFont(size=18, weight="bold"),
            fg_color="#c62828",
            hover_color="#8e0000",
            corner_radius=12,
            border_width=2,
            border_color="#ef5350"
        )
        self.btn_no.pack(side="left", padx=15)

        # ===== BOTONES DE CONTROL =====
        botones_control = ctk.CTkFrame(main_frame, fg_color="transparent")
        botones_control.pack(pady=(10, 20))

        self.btn_iniciar = ctk.CTkButton(
            botones_control,
            text="🔬 Iniciar Diagnóstico",
            command=self.iniciar_diagnostico,
            width=220,
            height=50,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#0d7377",
            hover_color="#14a0a6",
            corner_radius=12,
            border_width=2,
            border_color="#32e0c4"
        )
        self.btn_iniciar.pack(side="left", padx=8)

        self.btn_reiniciar = ctk.CTkButton(
            botones_control,
            text="🔄 Reiniciar",
            command=self.reiniciar_sistema,
            width=170,
            height=50,
            font=ctk.CTkFont(size=16),
            fg_color="#424242",
            hover_color="#616161",
            corner_radius=12,
            border_width=2,
            border_color="#757575"
        )
        self.btn_reiniciar.pack(side="left", padx=8)
        self.btn_reiniciar.configure(state="disabled")
    def agregar_mensaje_sistema(self, texto, tipo="normal"):
        """Agrega un mensaje del sistema al chat con diferentes estilos"""
        # Colores según tipo
        colores = {
            "bienvenida": "#0d7377",
            "info": "#1e3d59",
            "normal": "#2b2b2b",
            "exito": "#1b5e20",
            "error": "#c62828"
        }

        color = colores.get(tipo, "#2b2b2b")

        msg_frame = ctk.CTkFrame(
            self.chat_frame,
            fg_color=color,
            corner_radius=12,
            border_width=1,
            border_color="#444444"
        )
        msg_frame.pack(pady=8, padx=15, fill="x")

        # Icono según tipo
        iconos = {
            "bienvenida": "👋",
            "info": "💡",
            "normal": "💬",
            "exito": "✅",
            "error": "⚠️"
        }
        icono = iconos.get(tipo, "💬")

        label = ctk.CTkLabel(
            msg_frame,
            text=f"{icono} {texto}",
            font=ctk.CTkFont(size=14),
            wraplength=650,
            justify="left",
            text_color="white"
        )
        label.pack(pady=12, padx=20, anchor="w")

        # Scroll automático
        self.root.update_idletasks()
        self.chat_frame._parent_canvas.yview_moveto(1.0)

    def agregar_pregunta(self, sintoma):
        """Agrega una pregunta al chat con diseño mejorado"""
        sintoma_formateado = sintoma.replace('_', ' ').title()

        msg_frame = ctk.CTkFrame(
            self.chat_frame,
            fg_color="#1e3d59",
            corner_radius=12,
            border_width=2,
            border_color="#0d7377"
        )
        msg_frame.pack(pady=8, padx=15, fill="x")

        # Frame interno para el contenido
        content_frame = ctk.CTkFrame(msg_frame, fg_color="transparent")
        content_frame.pack(fill="x", pady=12, padx=20)

        # Icono grande
        icono = ctk.CTkLabel(
            content_frame,
            text="🔍",
            font=ctk.CTkFont(size=20)
        )
        icono.pack(side="left", padx=(0, 15))

        # Texto de la pregunta
        label = ctk.CTkLabel(
            content_frame,
            text=f"¿El cultivo presenta '{sintoma_formateado}'?",
            font=ctk.CTkFont(size=15, weight="bold"),
            wraplength=550,
            justify="left",
            text_color="white"
        )
        label.pack(side="left", fill="x", expand=True)

        # Scroll automático
        self.root.update_idletasks()
        self.chat_frame._parent_canvas.yview_moveto(1.0)

    def agregar_respuesta(self, respuesta):
        """Agrega la respuesta del usuario al chat con diseño mejorado"""
        texto = "✓ Sí" if respuesta else "✗ No"
        color = "#2e7d32" if respuesta else "#c62828"
        border_color = "#4caf50" if respuesta else "#ef5350"

        msg_frame = ctk.CTkFrame(
            self.chat_frame,
            fg_color=color,
            corner_radius=12,
            border_width=2,
            border_color=border_color
        )
        msg_frame.pack(pady=8, padx=(120, 15), fill="x")

        label = ctk.CTkLabel(
            msg_frame,
            text=texto,
            font=ctk.CTkFont(size=15, weight="bold"),
            wraplength=500,
            justify="right",
            text_color="white"
        )
        label.pack(pady=10, padx=20, anchor="e")

        # Scroll automático
        self.root.update_idletasks()
        self.chat_frame._parent_canvas.yview_moveto(1.0)

    def mostrar_pregunta(self, sintoma):
        """Callback cuando hay una nueva pregunta"""
        sintoma_formateado = sintoma.replace('_', ' ').title()

        self.agregar_pregunta(sintoma)

        # Mostrar frame de pregunta
        self.pregunta_label.configure(
            text=f"¿El cultivo presenta '{sintoma_formateado}'?"
        )
        self.pregunta_frame.pack(pady=10, padx=10, fill="x")

        # Habilitar botones
        self.btn_si.configure(state="normal")
        self.btn_no.configure(state="normal")

    def mostrar_resultado(self, diagnostico, exitoso, error=None):
        """Callback cuando se obtiene un resultado con diseño mejorado"""
        # Ocultar pregunta actual
        self.pregunta_frame.pack_forget()

        if error:
            self.agregar_mensaje_sistema(f"Error: {error}", tipo="error")
        elif exitoso and diagnostico:
            diagnostico_formateado = diagnostico.replace('_', ' ').upper()

            # Mensaje de éxito con diseño especial
            resultado_frame = ctk.CTkFrame(
                self.chat_frame,
                fg_color="#1b5e20",
                corner_radius=15,
                border_width=3,
                border_color="#4caf50"
            )
            resultado_frame.pack(pady=15, padx=15, fill="x")

            # Título
            titulo = ctk.CTkLabel(
                resultado_frame,
                text="✅ DIAGNÓSTICO ENCONTRADO",
                font=ctk.CTkFont(size=18, weight="bold"),
                text_color="white"
            )
            titulo.pack(pady=(15, 10))

            # Separador
            sep = ctk.CTkFrame(resultado_frame, height=2, fg_color="#4caf50")
            sep.pack(fill="x", padx=30, pady=5)

            # Diagnóstico
            diag_label = ctk.CTkLabel(
                resultado_frame,
                text=f"🔬 {diagnostico_formateado}",
                font=ctk.CTkFont(size=20, weight="bold"),
                text_color="#a5d6a7"
            )
            diag_label.pack(pady=15)

            # Recomendación
            rec_label = ctk.CTkLabel(
                resultado_frame,
                text="💡 Se recomienda consultar con un especialista\npara confirmar el diagnóstico y tratamiento.",
                font=ctk.CTkFont(size=13),
                text_color="#e8f5e9",
                justify="center"
            )
            rec_label.pack(pady=(0, 15))

        else:
            # Mensaje de no encontrado
            resultado_frame = ctk.CTkFrame(
                self.chat_frame,
                fg_color="#c62828",
                corner_radius=15,
                border_width=3,
                border_color="#ef5350"
            )
            resultado_frame.pack(pady=15, padx=15, fill="x")

            titulo = ctk.CTkLabel(
                resultado_frame,
                text="❌ NO SE ENCONTRÓ DIAGNÓSTICO",
                font=ctk.CTkFont(size=18, weight="bold"),
                text_color="white"
            )
            titulo.pack(pady=(15, 10))

            mensaje = ctk.CTkLabel(
                resultado_frame,
                text="Los síntomas no coinciden con ninguna\nenfermedad en la base de conocimientos.",
                font=ctk.CTkFont(size=14),
                text_color="#ffcdd2",
                justify="center"
            )
            mensaje.pack(pady=(0, 15))

        # Scroll automático
        self.root.update_idletasks()
        self.chat_frame._parent_canvas.yview_moveto(1.0)

        # Habilitar botón de reinicio
        self.btn_iniciar.configure(state="normal")
        self.btn_reiniciar.configure(state="normal")

    # Métodos de control que llaman al controlador
    def iniciar_diagnostico(self):
        if self.controlador:
            self.controlador.iniciar_diagnostico()

    def responder_si(self):
        if self.controlador:
            self.controlador.responder(True)

    def responder_no(self):
        if self.controlador:
            self.controlador.responder(False)

    def reiniciar_sistema(self):
        if self.controlador:
            self.controlador.reiniciar()

    def limpiar_chat(self):
        """Limpia el área de chat"""
        for widget in self.chat_frame.winfo_children():
            widget.destroy()

    def habilitar_botones_respuesta(self, habilitar=True):
        """Habilita o deshabilita los botones de respuesta"""
        estado = "normal" if habilitar else "disabled"
        self.btn_si.configure(state=estado)
        self.btn_no.configure(state=estado)

    def habilitar_boton_iniciar(self, habilitar=True):
        """Habilita o deshabilita el botón de iniciar"""
        estado = "normal" if habilitar else "disabled"
        self.btn_iniciar.configure(state=estado)

    def habilitar_boton_reiniciar(self, habilitar=True):
        """Habilita o deshabilita el botón de reiniciar"""
        estado = "normal" if habilitar else "disabled"
        self.btn_reiniciar.configure(state=estado)

    def ocultar_pregunta_actual(self):
        """Oculta el frame de pregunta actual"""
        self.pregunta_frame.pack_forget()

    def mostrar_error(self, mensaje):
        """Muestra un mensaje de error"""
        messagebox.showerror("Error", mensaje)

    def ejecutar(self):
        """Inicia la aplicación"""
        self.root.mainloop()