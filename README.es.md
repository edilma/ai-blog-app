


## **Escribe para humanos a la velocidad de la IA**

# AI Blog App ✍️

📖 Also available in [English](README.md)

Un framework avanzado para la creación de pipelines de generación de contenido con Inteligencia Artificial (IA). Este proyecto utiliza un sistema multiagente, basado en **Microsoft AutoGen**, para escribir, criticar y revisar artículos de forma autónoma en cuanto a calidad, cumplimiento y SEO. 

El sistema puede aceptar contexto opcional desde un PDF, que el LLM procesa para extracción de datos y contexto.  El usuario también puede especificar la longitud del artículo, con un valor predeterminado de **300 palabras**.

---

## 🧠 Cómo Funciona

AI Blog App simula un proceso colaborativo de escritura y edición mediante un equipo de agentes especializados.  
Cada agente cumple un rol único para refinar el artículo o post, comunicándose entre sí hasta lograr estándares de calidad en legibilidad, SEO y coherencia.

- **Agente Escritor:** Redacta un borrador inicial, diseñado para ser claro, atractivo y con narrativa.
- **Agente Crítico:** Revisa el borrador y ofrece retroalimentación sobre estructura, tono y fluidez.
- **Revisor SEO:** Asegura que el texto contenga palabras clave, encabezados sólidos y elementos de SEO on-page.
- **Revisor de Marketing de Contenido:** Analiza la claridad, organización y atractivo del artículo para el lector.
- **Revisor de Claridad y Ética:** Comprueba que el contenido sea comprensible, sin lenguaje problemático, y adecuado para publicación.

El sistema también permite incluir contexto desde PDFs básicos, con extracción automática de datos por el LLM.

---

## 💡 Características Principales

**🧩 Arquitectura Modular de Agentes**  
Incluye agentes especializados para:
- **Escritor** → Redacta artículos narrativos y fáciles de leer.
- **Revisor de Marketing** → Mejora estructura y atractivo.
- **Revisor de Claridad & Ética** → Garantiza comprensión y precisión.
- **Revisor SEO** → Optimiza para motores de búsqueda.

**💬 Colaboración Inteligente entre Agentes**  
Los agentes trabajan en un bucle de revisión coordinado.  
Un meta-agente central sintetiza sus aportes en un producto final coherente y pulido.

**📦 Uso como Librería o API**  
Integra este framework en tus proyectos de dos formas:
- **Librería Python** → Importa y usa las funciones directamente.
- **Servicio API** → Ejecuta la app como servicio en tiempo real.

**✅ Orientado a SEO y Lectores**  
Optimizado para destacar en buscadores y conectar con personas reales.

---

## 🔧 Instalación y Uso

### Dependencias

Este proyecto está basado en **Microsoft AutoGen**.  
Dependencias principales:

- `autogen-agentchat>=0.7.1`
- `autogen-ext[all]>=0.7.1`
- `openai>=1.98.0`

### 🚀 Instalación

Desde PyPI (próximamente):

```bash
pip install ai-blog-app
````

O directamente desde GitHub:

```bash
pip install git+https://github.com/edilma/AI_Blog_App.git
```

\<sub>Requiere Python 3.10 o superior\</sub>

---

## ✍️ Uso Básico

Ejemplo mínimo con la librería:

```python
from ai_blog_app import BlogOrchestrator

orchestrator = BlogOrchestrator()
post = orchestrator.generate(
    topic="Herramientas de IA para marketing",
    audience="emprendedores",
    length="corto"
)
print(post.markdown)
```

Ejemplo con scripts incluidos en el repositorio:

1. Ir a la carpeta `examples`:

   ```bash
   cd examples
   ```

2. Crear archivo `.env` desde plantilla:

   ```bash
   cp .env.example .env
   ```

3. Añadir credenciales:

   ```
   OPENAI_API_KEY=tu_api_key
   ```

4. Ejecutar:

   ```bash
   python main.py
   ```

---

## 📁 Estructura del Proyecto

```
.
├── ai_blog_app/       # Código fuente principal
│   ├── agents/        # Lógica de agentes individuales
│   ├── utils/         # Funciones auxiliares
│   ├── config.py
│   ├── llm_config.json
│   └── __init__.py
├── examples/          # Ejemplos de uso
├── pyproject.toml
├── README.md          # Versión en inglés
├── README.es.md       # Esta versión en español
└── LICENSE
```

---

## 📜 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).
Puedes usarlo, modificarlo y distribuirlo libremente con atribución.

---

## ✨ Autor

Creado con 💻 por **Edilma Riano**
Ayudando a negocios y creadores a usar IA para trabajar mejor y crecer más rápido.

🐙 [Sígueme en GitHub](https://github.com/edilma)


