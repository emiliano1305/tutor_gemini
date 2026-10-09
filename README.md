# Tutor guiado de Python

Aplicación sencilla en Streamlit para estudiantes que comienzan con Python. Incluye lecciones y ejercicios locales que funcionan sin claves ni servicios externos. De manera opcional, se puede habilitar un chat generativo con Google Gemini.

## Qué incluye

- 12 lecciones, desde los primeros pasos hasta una introducción a clases y objetos.
- Búsqueda por palabras clave entre los temas incluidos.
- Ejemplos de código para descargar como archivos `.py`.
- Ejercicios de autoevaluación con corrección inmediata.
- Chat opcional con Gemini para explicaciones, ayuda con código y depuración de Python.

El tutor guiado utiliza contenido preparado en `core.py`. El chat IA está configurado para tratar exclusivamente programación en Python; el filtro local rechaza preguntas que claramente no mencionan programación. Como todo modelo generativo, puede equivocarse y las instrucciones de alcance no garantizan una clasificación perfecta de cada consulta.

## Ejecutar en tu computadora

Se necesita Python 3.10 o posterior. En PowerShell, dentro de la carpeta del proyecto:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Las lecciones y prácticas funcionan inmediatamente. Para usar el chat Gemini en tu computadora, definí `GEMINI_API_KEY` en una variable de entorno antes de iniciar Streamlit.

## Habilitar Gemini en Streamlit Community Cloud

1. En Google AI Studio, iniciá sesión y creá una clave API desde la página de [claves de Google AI Studio](https://aistudio.google.com/app/apikey). Copiala en un lugar seguro. No la compartas en el chat ni la publiques en GitHub.
2. En Streamlit Community Cloud, abrí la app y entrá a **App settings → Secrets**.
3. En el cuadro de secretos, agregá esta línea y reemplazá el texto de ejemplo por tu propia clave:

   ```toml
   GEMINI_API_KEY = "PEGÁ_ACÁ_TU_CLAVE"
   ```

4. Guardá los cambios, esperá a que Streamlit los aplique y recargá la app. No hace falta poner la clave en `app.py`, en GitHub ni en un archivo `secrets.toml` subido al repositorio.
5. En la barra lateral, elegí **Tutor IA (Gemini)**. Si la clave falta, las otras secciones siguen disponibles.

La clave pertenece al dueño de la app. Las consultas de quienes usan la app consumen los límites del mismo proyecto/API. La disponibilidad y los límites pueden cambiar según el modelo y la cuenta; si se alcanza una cuota, el chat mostrará un mensaje simple para esperar y volver a probar. Gemini ofrece un nivel gratuito con límites, no uso ilimitado. Google indica que los datos del nivel gratuito pueden usarse para mejorar sus productos; para una app escolar, no ingresen nombres completos, contraseñas, notas ni información privada de estudiantes. Revisá los [precios y condiciones de Gemini API](https://ai.google.dev/gemini-api/docs/pricing) y los [límites vigentes](https://ai.google.dev/gemini-api/docs/rate-limits).

## Publicar la app

Subí `app.py`, `ai_tutor.py`, `core.py`, `requirements.txt` y este `README.md` a la rama `main` de GitHub. En Streamlit Community Cloud elegí ese repositorio, la rama `main` y `app.py` como archivo principal. Usá Python 3.12. Para las lecciones básicas no hace falta configurar Secrets. Solo agregá `GEMINI_API_KEY` en **App settings → Secrets** si querés habilitar el chat IA.

## Seguridad y límites

No guardes claves API en el repositorio ni las muestres en la app. Esta integración oculta los detalles técnicos de los errores para evitar revelar datos sensibles. No ejecuta código escrito por los alumnos y no consulta la web. Las consultas al chat se envían a Google Gemini; consultá sus condiciones antes de usarlo con estudiantes.
