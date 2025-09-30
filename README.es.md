


## **Escribe para humanos a la velocidad de la IA**

# AI Blog App ✍️

📖 Also available in [English](README.md)

***Crea blogs y artículos inteligentes de forma autónoma.***

AI Blog App proporciona un potente motor de generación de contenido impulsado por un sistema multiagente. Su función principal, `generate_blog_post_with_review()`, solo requiere que se le de un tema para producir contenido de blogs y artículos de alta calidad e interesantes. Los usuarios pueden mejorar el resultado proporcionando contexto opcional (como texto) para una generación fundamentada en hechos, y pueden especificar el número máximo de palabras (por defecto: 300 palabras). El sistema aprovecha agentes de IA especializados —escritor, crítico y múltiples revisores— que trabajan en colaboración para garantizar que el contenido final cumpla con estándares profesionales de legibilidad, SEO y participación.

> **Nota para Desarrolladores:** Esta biblioteca está construida sobre el framework Microsoft AutoGen, que abre emocionantes posibilidades para personalización avanzada. Puedes extender el sistema de agentes con tus propios agentes especializados, modificar flujos de conversación o adaptar el proceso de revisión para tipos de contenido específicos. La arquitectura flexible de AutoGen te permite ajustar comportamientos de agentes, plantillas de instrucciones y patrones de interacción para satisfacer tus requisitos específicos. El sistema es ideal para construir aplicaciones RAG (Generación Aumentada por Recuperación)—la API ya está configurada para aceptar contexto externo, facilitando la integración con recuperadores de documentos, bases de conocimiento o fuentes de datos personalizadas. Consulta la [documentación de AutoGen](https://microsoft.github.io/autogen/) para explorar todo el potencial de este poderoso framework.

---

## 🧠 Cómo Funciona

AI Blog App simula un proceso colaborativo de escritura y edición mediante un equipo de agentes especializados de IA. Cada agente cumple un rol único para refinar el artículo o post, comunicándose entre sí hasta lograr estándares de calidad en legibilidad, SEO y coherencia.

-   **Agente Escritor:** Redacta un borrador inicial de blog o artículo basado en un tema, diseñado para ser claro, atractivo y con narrativa.
-   **Agente Crítico:** Revisa el borrador del escritor y ofrece retroalimentación directa y procesable sobre estructura, claridad, tono y fluidez.
-   **Revisor SEO:** Asegura que el blog incluya palabras clave relevantes, encabezados sólidos y otros elementos de SEO para mejorar la visibilidad en motores de búsqueda.
-   **Revisor de Marketing de Contenido:** Analiza la estructura, el engagement y la presentación para asegurar que el blog sea claro, esté organizado lógicamente y sea convincente para los lectores.
-   **Revisor de Claridad y Ética:** Comprueba que el contenido sea fácil de entender para un público general, libre de lenguaje confuso o problemático, y apropiado para consumo público.

Aunque la biblioteca en sí no procesa PDFs directamente, su diseño consciente del contexto permite que las aplicaciones que usan esta biblioteca le proporcionen datos extraídos de PDFs u otras fuentes de documentos, haciéndola versátil para diversos flujos de trabajo de generación de contenido.

---

## 💡 Características Principales

**🧩 Arquitectura Modular de Agentes**
- Agentes especializados con roles distintos en el proceso de creación de contenido
- Personalización de agentes a través de ingeniería de prompts
- Clara separación de responsabilidades entre agentes escritores, críticos y revisores

**💬 Pipeline de Revisión Multi-etapa**
- Flujo de trabajo secuencial de agentes para generación confiable de contenido
- Múltiples tipos de revisores especializados examinando diferentes aspectos del contenido
- Consolidación de retroalimentación a través del agente crítico para mejoras coherentes

**📦 Integración Simple**
- API Python asíncrona y limpia con docstrings completas
- Fácil importación y uso en proyectos Python existentes
- Llamada directa a funciones para generar blogs y artículos completos

**⚙️ Configuración Amigable para Desarrolladores**
- Configuración de proveedores y modelos basada en JSON
- Gestión de credenciales mediante variables de entorno
- Limitaciones configurables de recuento de palabras
- Cambio de modelos en tiempo de ejecución entre múltiples proveedores de LLM

---

## 🔧 Instalación y Uso

### Dependencias

Este proyecto está basado en **Microsoft AutoGen**, aprovechando sus capacidades multiagente. Las dependencias principales son:

-   `autogen-agentchat>=0.7.1`
-   `autogen-ext[all]>=0.7.1`
-   `openai>=1.98.0`
-   `tiktoken>=0.11.0`

### Soporte Flexible para LLM

La aplicación admite múltiples proveedores de Modelos de Lenguaje Grande (LLM) de forma inmediata:
-   **OpenAI:** Funciona con modelos como ChatGPT y GPT-4.
-   **Google Gemini:** Se conecta a través de una API compatible con OpenAI.
-   **Claude:** Compatible con modelos de Anthropic.
-   **Ollama:** Permite el uso de modelos locales como LLaMA 3.

La configuración es sencilla y completamente **basada en JSON** (`llm_config.json`), lo que te permite cambiar fácilmente de proveedores o modelos sin modificar el código. Todas las credenciales se gestionan de forma segura mediante archivos `.env`.

### 🚀 Instalación

Instalar desde PyPI:
```bash
pip install ai-blog-app
````

<sub>Requiere Python 3.10+</sub>

O instala el Framework de Agentes de Blog directamente desde GitHub usando `pip`:

```bash
pip install git+https://github.com/edilma/ai-blog-app.git
```

🌐 Enlaces del Proyecto

Página principal: https://github.com/edilma/AI_Blog_App

Documentación: https://github.com/edilma/AI_Blog_App/blob/main/README.md

Seguimiento de errores: https://github.com/edilma/AI_Blog_App/issues

### ✍️ Uso Básico

Usar esta biblioteca en tus proyectos es sencillo:

1. **Configurar Variables de Entorno**

Crea un archivo `.env` en el directorio de tu proyecto con tus claves API:

```plaintext
# Elige el proveedor que quieres usar y añade su clave API
OPENAI_API_KEY=sk-...tu-clave-aquí...
# O para otros proveedores:
# GEMINI_API_KEY=...tu-clave-aquí...
# ANTHROPIC_API_KEY=...tu-clave-aquí...
```

2. **Generar Contenido**

Este ejemplo muestra cómo generar un post de blog usando el modelo Gemini:

```python
import asyncio
from dotenv import load_dotenv
from ai_blog_app import generate_blog_post_with_review

# Cargar variables de entorno desde archivo .env
load_dotenv()

async def generate_post():
    topic = "El Futuro de la IA en el Marketing de Contenidos"
    
    print(f"Iniciando pipeline de agentes para el tema: {topic}...")

    final_post = await generate_blog_post_with_review(
        topic=topic,
        provider="gemini",  # Opciones: "openai", "gemini", "claude", "ollama"
        model="gemini-1.5-flash",
        max_words=500  # Opcional: controlar longitud de salida
    )
    
    print("\n--- ARTÍCULO GENERADO ---\n")
    print(final_post)
    
    # Ahora puedes guardar, mostrar o procesar el contenido generado
    return final_post

if __name__ == "__main__":
    # Ejecutar la función asíncrona
    asyncio.run(generate_post())
```

### 3. Características Adicionales

**Generación Basada en Contexto**

Puedes proporcionar contexto adicional para fundamentar el contenido en información específica:

```python
final_post = await generate_blog_post_with_review(
    topic="Beneficios de la Agricultura Sostenible",
    provider="openai",
    model="gpt-4o",
    context="La agricultura sostenible se enfoca en la salud del ecosistema a largo plazo...",
    max_words=700
)
```

**Script de Ejemplo Completo**

Para ejemplos completos y ejecutables con todas las opciones de configuración, consulta el directorio `examples/` en el repositorio de GitHub:

[🔗 Ver la Carpeta de Ejemplos en GitHub](https://github.com/edilma/AI_Blog_App/tree/main/examples)

---

## 📁 Estructura del Proyecto

El proyecto está estructurado como un paquete Python estándar, lo que facilita su instalación y uso.

```
.
├── ai_blog_app/            # Código fuente principal de la biblioteca
│   ├── agents/             # Contiene la lógica de agentes individuales
│   │   ├── __init__.py
│   │   ├── critic.py
│   │   ├── reviewers.py
│   │   └── writer.py
│   ├── utils/              # Contiene funciones auxiliares
│   │   ├── __init__.py
│   │   └── helpers.py
│   ├── config.py           # Maneja la configuración del cliente de modelos
│   ├── llm_config.json     # Configuración del proveedor de LLM
│   └── __init__.py
│
├── examples/               # Ejemplos autocontenidos para usuarios
│   ├── .env                # Archivo de entorno para variables
│   ├── .env.example        # Plantilla para variables de entorno
│   └── main.py             # Script principal para demostrar el uso
│
├── .gitignore              # Especifica qué archivos debe ignorar Git
├── LICENSE                 # La licencia de código abierto del proyecto
├── pyproject.toml          # Archivo de configuración moderno para el paquete
├── README.es.md            # Esta versión en español
├── README.md               # Versión en inglés
└── uv.lock                 # Archivo de bloqueo para gestión de dependencias
```

-----

## 📜 Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).

-----

## ✨ Autor

Creado por **Edilma Riano** — Arquitecta y Desarrolladora de Sistemas de IA

Me especializo en construir herramientas prácticas de IA que ayudan a empresas y creadores de contenido a escalar sus operaciones. Con experiencia en sistemas basados en agentes e IA generativa, me enfoco en crear soluciones que combinan excelencia técnica con valor empresarial.

### Conectar y Colaborar

- 🐙 [GitHub](https://github.com/edilma)
- 💼 [LinkedIn](https://www.linkedin.com/in/edilma/)
- 🌐 [Portafolio](https://edilmariano.com/)

*¿Interesado en soluciones personalizadas de contenido con IA o en extender esta biblioteca? Contacta para oportunidades de colaboración.*


