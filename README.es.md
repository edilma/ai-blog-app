# 🧠 AI Blog App 

**Crea articulos de blogs inteligentes y de alta calidad en forma automática.**

Un framework avanzado para construir flujos de generación de contenido impulsados por IA. Este proyecto utiliza un sistema multiagente, basado en Microsoft Autogen, para redactar, criticar y revisar artículos de forma autónoma, asegurando calidad, cumplimiento y optimización SEO.
Crea blogs más inteligentes y eficaces, de forma autónoma.

Esta es una aplicación modular y lista para producción, desarrollada con AutoGen (v0.4), que genera publicaciones de blog de alta calidad a partir de cualquier tema, utilizando un sistema de agentes especializados: redactor, crítico y revisores expertos.

💡 La app es compatible con múltiples proveedores de modelos LLM desde el inicio, incluyendo:

- OpenAI (ChatGPT / GPT-4)
- Google Gemini (a través de una API compatible con OpenAI)
- Claude (Anthropic)
- Ollama (modelos locales como LLaMA 3)

🔧 La configuración se gestiona completamente mediante un archivo JSON (llm_config.json), y las credenciales se manejan de forma segura a través de .env. Puedes cambiar de proveedor o modelo sin modificar el código.

📁 La estructura del proyecto es limpia y organizada, gestionada por entornos virtuales con uv, y lista para ampliarse con funciones como RAG, almacenamiento de publicaciones o ejecución como API.

Este framework simula un equipo profesional de creación de contenido: un redactor, un crítico y varios revisores colaboran para generar artículos concisos, optimizados para SEO y con un enfoque narrativo, diseñados para atraer lectores y posicionar bien en buscadores. Aplica las mejores prácticas del marketing digital para maximizar el alcance, la estructura y el impacto de cada publicación.

Ya seas un blogger independiente, un especialista en marketing de contenidos o un desarrollador, puedes usar esta biblioteca para automatizar la creación de contenidos o integrarla en tu propia API.

---

## 🔧 Características

- **🧩 Arquitectura modular de agentes**  
  Incluye agentes especializados para:
  - **Escritor** – Crea publicaciones con lenguaje sencillo y estilo narrativo  
  - **Revisión de Marketing de Contenidos** – Mejora la estructura, claridad y atractivo del texto  
  - **Revisión de Claridad y Ética** – Verifica que el contenido sea comprensible y libre de lenguaje confuso o inapropiado  
  - **Revisión SEO** – Optimiza el contenido para mejorar su visibilidad en Google y otros motores de búsqueda

- **💬 Colaboración inteligente entre agentes**  
    Nuestro sistema emplea un modelo colaborativo en el que agentes especializados, cada uno con un rol definido, operan dentro de un ciclo de revisión estructurado. Un meta-agente central se encarga de sintetizar las contribuciones individuales en un producto final coherente y pulido. Esta orquestación permite crear publicaciones de blog altamente atractivas, aprovechando las fortalezas únicas de cada agente especializado. 

- **📦 Úsalo como biblioteca o base para una API**  
    Puedes integrar fácilmente este framework en tus proyectos existentes de las siguientes maneras:

    Librería de Python: Incorpora directamente las capacidades de generación de blogs en tus aplicaciones de Python.

    Servicio API: Construye una API en tiempo real sobre el framework para alimentar la generación de blogs en tu sitio web o servicio de contenidos.

- **✅ Contenido optimizado para buscadores y personas**  
    Diseñado para que tu contenido tenga un buen rendimiento tanto en motores de búsqueda como en herramientas de inteligencia artificial y conecte con personas reales. Todos los blogs se generan aplicando las mejores prácticas del marketing de contenidos.

---

## 🚀 Instalación

Instalar desde PyPI:

```bash
pip install blog-agent-framework
```
<sub>Requiere Python 3.11+</sub>

Instala la biblioteca directamente desde GitHub usando `pip`:

```bash
pip install git+https://github.com/edilma/AI-Agent-Orchestrator.git
````

## 📁 Estructura de la Aplicacion
La aplicacon esta estructurada como un paquete Python lo que lo hace facil de instalar y usar. 

```
    .
├── ai_blog_app/               # La libreria principal.  Source Code
│   ├── agents/                # Contiene la logica de los agentes
│   ├── config.py              # Maneja la configuracion del modelo 
│   ├── llm_config.json        # Configuración del LLM
│   └── __init__.py            # Expone la función principal de generación
│
├── examples/                 # Self-contained examples for users
│   ├── .env.example           # Plantilla para las environment variables
│   └── main.py                # Script principal para demonstrate el uso de la libreria
│
├── .gitignore                # Espefica que archivos Git debe ignorar
├── LICENSE                   # La licencia de open-source del proyecto
├── pyproject.toml            # Usa configuracion moderna para el paquete
└── README.md                 # This file!
```

## ✍️ Uso básico

Aquí te mostramos cómo ejecutar el ejemplo incluido.

### ▶️ Ejecutar el ejemplo

1. **Entra a la carpeta de ejemplos:**

```bash
cd examples
```

2. **Copia el archivo de entorno desde la plantilla:**

```bash
# En Windows
copy .env.example .env

# En macOS o Linux
cp .env.example .env
```

3. **Agrega tus credenciales de OpenAI al archivo `.env`:**
Por ejemplo:
```
GEMINI_API_KEY=your_gemini_api_key_here

# or for OpenAI
OPENAI_API_KEY=your_openai_key_here
```
```

4. **Ejecuta el script:**

```bash
python run_example.py
```

Esto activará el sistema de agentes, generará un blog y mostrará cómo se realiza el ciclo completo de redacción y revisión.

---

## 🧠 ¿Cómo funciona?

Blog Agent Framework simula un proceso de redacción colaborativo con un conjunto de agentes especializados en IA. Cada agente tiene una tarea específica:

1. **Agente Redactor**
   Genera un borrador del blog a partir de un tema. Usa lenguaje sencillo y un estilo narrativo para enganchar al lector.

2. **Agente Crítico**
   Revisa el borrador, analiza la estructura, claridad, tono y narrativa, e incorpora las sugerencias de los demás agentes para entregar una versión mejorada.

3. **Agente SEO**
   Evalúa la presencia de palabras clave, encabezados y elementos esenciales para mejorar el posicionamiento en buscadores.

4. **Agente de Marketing de Contenidos**
   Verifica que el blog tenga buena estructura, lógica y sea fácil de seguir.

5. **Agente de Claridad y Ética**
   Asegura que el texto sea comprensible para cualquier lector, sin lenguaje confuso o inadecuado.

---

## 📜 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).
Puedes usarlo, modificarlo y distribuirlo libremente, con atribución.

---

## ✨ Autor

Creado con 💻 por **Edilma Riano**
Ayudando a empresas y creadores a usar IA para trabajar de forma más inteligente y escalar más rápido.

🔗 [Visita mi perfil en GitHub](https://github.com/edilma)

```

---

