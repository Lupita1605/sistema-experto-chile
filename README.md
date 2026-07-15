# Sistema Experto Basado en Lógica de Primer Orden para el Diagnóstico Fitopatológico del Chile Jalapeño

Este repositorio aloja el código fuente de un **Sistema Experto Interactivo** orientado al diagnóstico automatizado de enfermedades en cultivos de chile jalapeño. La arquitectura del proyecto implementa un motor lúdico y declarativo en **Prolog** basado en Lógica de Primer Orden, integrado nativamente con una interfaz gráfica de usuario (GUI) asíncrona desarrollada en **Python** empleando la biblioteca `customtkinter`.

## Especificación Técnica del Módulo Lógico (`reglas.pl`)

El componente de inferencia y base de conocimiento está estructurado formalmente en tres capas operacionales:

### 1. Base de Conocimientos (Base de Reglas)
Consiste en un conjunto de cláusulas de Horn que modelan las relaciones sintomáticas de las patologías vegetales mediante predicados deterministas:
*   **Tizón Tardío (*Phytophthora infestans*):** Definido mediante dos variantes de reglas; se satisface por la coocurrencia de máculas foliares y necrosis en el tallo (`manchas_negras_hojas` $\land$ `tallo_con_manchas`), o bien por la presencia aislada de necrosis apical (`punta_muerta_hoja`).
*   **Mancha Bacteriana (*Xanthomonas campestris*):** Condicionada estrictamente a la intersección de lesiones hidróticas y defoliación prematura (`manchas_acuosas_hojas` $\land$ `perdida_severa_hojas`).
*   **Mosaico Viral (Virus del Mosaico):** Validado mediante la presencia simultánea de distorsión morfológica foliar y clorosis en patrón variegado (`deformacion_hoja` $\land$ `patron_mosaico_amarillo`).

### 2. Motor de Inferencia (Mecanismo de Control)
Modela el flujo de evaluación transaccional de los síntomas del espécimen:
*   **`tiene/2`:** Predicado de evaluación que consulta el estado actual del entorno lúdico. Valida si el axioma sintomático ya reside en la base de hechos como `confirmado` (retornando éxito inmediato) o `descartado` (provocando un fallo y retroceso o *backtracking*). En ausencia de registro previo, delega el control al flujo de captura.
*   **`preguntar/1`:** Actúa como la interfaz de E/S del motor lúdico. Despliega la consulta interactiva en consola y captura la respuesta síncrona del operador. Mediante estructuras condicionales, evalúa el operando (`si.` / `no.`) e inyecta dinámicamente el hecho resultante en el espacio de memoria activa.

### 3. Persistencia Dinámica y Mutabilidad de Hechos
*   **`:- dynamic confirmado/1, descartado/1.`:** Directivas de compilación que instruyen al motor Prolog a tratar dichos predicados como estructuras mutables en tiempo de ejecución, habilitando la metaprogramación.
*   **`borrar_memoria/0`:** Procedimiento de saneamiento que purga de manera iterativa todas las aserciones temporales mediante el uso del predicado de orden superior `retractall/1`. Esto garantiza el principio de idempotencia del sistema al reiniciar el proceso diagnóstico sin acarrear estados previos.
