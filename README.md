
# Entrega Práctica 2 - Seminario de Python

**Alumna:** Katerina Zanek  
**Legajo:** 25677/9
  
## ⚙️ Requisitos

* **Python 3.10** o superior.
* Sistema operativo: Windows, macOS o Linux.

---

## 📦 Instalación

Para configurar el proyecto y preparar el entorno virtual desde tu terminal:

1. **Clonar el repositorio:**
   ```bash
   git clone <https://github.com/KatZnk/Practica02.git>
   cd Practica02
   ```

2. **Crear y activar el entorno virtual (.venv):**
   * **En Windows:**
     ```bash
     python (o python3) -m venv
     python -m venv .venv
     .venv\Scripts\activate
     ```
   * **En macOS/Linux:**
     ```bash
     python (o python3) -m venv .venv
     source .venv/bin/activate
     ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Ejecución

Una vez activado el entorno virtual y cargadas las dependencias, inicia la interfaz de trabajo:

```bash
jupyter lab
```

## 📁 Estructura del Proyecto

```text
📦 Proyecto
 ┣ 📂 notebooks # Ejecuciones y visualización de tablas (Jupyter)
   ┗ 📜 ejercicio1.ipynb
    ...      
 ┃ ┗ 📜 ejercicio10.ipynb
 ┣ 📂 src                # Lógica de programación (Scripts .py)
 ┃ ┣ 📜 ejercicio1.py
    ...
 ┃ ┗ 📜 ejercicio10.py
 ┣ 📜 .gitignore         
 ┣ 📜 README.md         
 ┗ 📜 requirements.txt   # jupyterlab==4.5.6
```
