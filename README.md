# Calculadora con Conversor de Temperatura

Este proyecto consiste en una aplicación de escritorio desarrollada en Python utilizando la librería gráfica Tkinter. La herramienta combina las funciones de una calculadora aritmética estándar con un módulo específico para la conversión de unidades de temperatura.

---

## Funcionalidades Principales

### 1. Calculadora Aritmética
La interfaz principal ofrece una calculadora funcional con las siguientes capacidades:
* Operaciones básicas: suma, resta, multiplicación y división.
* Cálculo de porcentajes.
* Función de borrado de un solo carácter (retroceso) y limpieza total de la pantalla.
* Interfaz adaptativa con límite de entrada de 15 caracteres para mantener la integridad visual.
* Formateo inteligente de resultados para evitar errores de precisión decimal.

### 2. Conversor de Temperatura
A través de un acceso directo en la interfaz principal, se puede acceder a un módulo de conversión que permite:
* Transformar grados Celsius a Fahrenheit.
* Transformar grados Fahrenheit a Celsius.
* Retorno rápido a la interfaz de la calculadora mediante un botón de navegación.

---

## Estructura del Proyecto

El código está organizado de manera modular para facilitar su mantenimiento:
* **config/constantes.py**: Contiene la definición de colores, fuentes y estilos de la interfaz (modo oscuro).
* **utils/util_ventana.py**: Incluye funciones de utilidad para la gestión de las ventanas, como el centrado automático en pantalla.
* **FormularioCalculadora**: Clase principal que gestiona la lógica de la calculadora y la navegación.
* **FormularioConversor**: Clase secundaria que gestiona la lógica matemática de las conversiones de temperatura.

---

## Requisitos y Ejecución

Para ejecutar la aplicación es necesario tener instalado Python 3.x. No se requieren librerías externas adicionales ya que Tkinter forma parte de la biblioteca estándar de Python.

1. Clonar o descargar los archivos del repositorio.
2. Asegurarse de mantener la estructura de carpetas para las importaciones de `config` y `utils`.
3. Ejecutar el archivo principal:
   ```bash
   python main.py
