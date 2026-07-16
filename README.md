
<p align="center">
  <img src="https://img.shields.io/badge/Python-337689?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/CustomTkinter-2B2B2B?style=for-the-badge&logo=python&logoColor=7F7F7F" alt="CustomTkinter" />
  <img src="https://img.shields.io/badge/Prolog-ED1C24?style=for-the-badge&logo=prolog&logoColor=white" alt="Prolog" />
</p>

<p align="center">
  <b>Sistema Experto Fitopatológico</b> • <b>Lógica de Primer Orden</b> • <b>Interfaz Gráfica Asíncrona</b>
</p>

---

# 📊 Aspectos Destacados de la Investigación

⚡ **Cláusulas de Horn Puras** para el modelado determinista y preciso de patologías vegetales.
🚀 **Inferencia Asíncrona** en tiempo real acoplando el motor declarativo de Prolog con una GUI moderna en Python.
🔄 **Principio de Idempotencia** garantizado mediante metaprogramación y purga dinámica de memoria en tiempo de ejecución.

---

# 🌶️ Introducción

Este repositorio aloja el código fuente de un **Sistema Experto Interactivo** orientado al diagnóstico automatizado de enfermedades en cultivos de chile jalapeño. La arquitectura del proyecto implementa un motor declarativo en Prolog basado en Lógica de Primer Orden, integrado nativamente con una interfaz gráfica de usuario (GUI) asíncrona desarrollada en Python empleando la biblioteca `customtkinter`.

---

# ⚙️ Especificación Técnica del Módulo Lógico (`reglas.pl`)

El componente de inferencia y la base de conocimiento están estructurados formalmente en tres capas operacionales:

### 1. Base de Conocimientos (Base de Reglas)
Consiste en un conjunto de cláusulas de Horn que modelan las relaciones sintomáticas mediante predicados deterministas:
* **Tizón Tardío (*Phytophthora infestans*):** Definido mediante dos variantes de reglas; se satisface por la coocurrencia de máculas foliares y necrosis en el tallo (`manchas_negras_hojas ∧ tallo_con_manchas`), o bien por la presencia aislada de necrosis apical (`punta_muerta_hoja`).
* **Mancha Bacteriana (*Xanthomonas campestris*):** Condicionada estrictamente a la intersección de lesiones hidróticas y defoliación prematura (`manchas_acuosas_hojas ∧ perdida_severa_hojas`).
* **Mosaico Viral (*Virus del Mosaico*):** Validado mediante la presencia simultánea de distorsión morfológica foliar y clorosis en patrón variegado (`deformacion_hoja ∧ patron_mosaico_amarillo`).

### 2. Motor de Inferencia (Mecanismo de Control)
Modela el flujo de evaluación transaccional de los síntomas del espécimen:
* **`tiene/2`:** Predicado de evaluación que consulta el estado actual del entorno. Valida si el axioma sintomático ya reside en la base de hechos como confirmado (retornando éxito inmediato) o descartado (provocando un fallo y retroceso o *backtracking*). En ausencia de registro previo, delega el control al flujo de captura.
* **`preguntar/1`:** Actúa como la interfaz de E/S del motor. Despliega la consulta interactiva en consola y captura la respuesta síncrona del operador. Mediante estructuras condicionales, evalúa el operando (`si.` / `no.`) e inyecta dinámicamente el hecho resultante en el espacio de memoria activa.

### 3. Persistencia Dinámica y Mutabilidad de Hechos
* **`:- dynamic confirmado/1, descartado/1.`:** Directivas de compilación que instruyen al motor Prolog a tratar dichos predicados como estructuras mutables en tiempo de ejecución, habilitando la metaprogramación.
* **`borrar_memoria/0`:** Procedimiento de saneamiento que purga de manera iterativa todas las aserciones temporales mediante el uso del predicado de orden superior `retractall/1`. Esto garantiza reiniciar el proceso diagnóstico sin acarrear estados previos.

---

# 🚀 Guía de Inicio Rápido

Sigue estos pasos para ejecutar el diagnosticador fitopatológico localmente:

### 📦 1. Instalar Dependencias
Asegúrate de tener Python y un entorno Prolog compatible instalado. Luego, instala la biblioteca gráfica ejecutando:
```bash
pip install customtkinter

```

### 🐍 2. Ejecución del Sistema

Para inicializar la interfaz gráfica e iniciar las consultas de diagnóstico, ejecuta el archivo principal desde tu terminal:

```bash
python main.py

```

---

## 👥 Colaboradores y Derechos de Autor

Este proyecto fue realizado en equipo por los siguientes integrantes:

* **Baizabal Acosta Ismael** - Desarrollo y Lógica del Sistema
* **Hernández Rodríguez Ricardo** - Diseño y Frontend
* **Morales Hernández Guadalupe Aleida** - Pruebas y Documentación
* **Trujillo Trujillo Juan Pablo** - Pruebas y Base de Datos
* **Velázquez López Guadalupe** - Desarrollo e Integración del Sistema

---

## ⚖️ Licencia

Este proyecto es de uso estrictamente académico para el Instituto Tecnológico Superior de Xalapa (ITSX).

