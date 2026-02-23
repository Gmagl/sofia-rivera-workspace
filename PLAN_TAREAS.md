# Plan de tareas propuesto

## 1) Corregir error tipográfico
- **Problema detectado:** En el `README.md` aparece `trackingpremium.` en la lista de próximos pasos, lo que parece un error de escritura/espaciado.
- **Tarea:** Corregir `trackingpremium.` por `tracking premium.` (o `tracking premium` según estilo elegido) para mejorar claridad.
- **Archivo afectado:** `README.md`.
- **Criterio de aceptación:** El texto queda legible y coherente con el resto del documento.

## 2) Solucionar un fallo funcional
- **Problema detectado:** `app_enhanced.py` contiene errores de sintaxis que impiden ejecutar la app:
  - Falta el cierre de la lista `PROMPTS`.
  - `show_profile()` retorna `profile_text]` (corchete extra) en lugar de `profile_text`.
- **Tarea:** Corregir la sintaxis y validar que el archivo compile.
- **Archivo afectado:** `app_enhanced.py`.
- **Criterio de aceptación:** `python -m py_compile app_enhanced.py` finaliza sin errores.

## 3) Corregir comentario de código / discrepancia documental
- **Problema detectado:** El comentario `# Función para generar imagen` puede resultar ambiguo; la función genera imágenes y devuelve además un estado, por lo que conviene que el comentario describa mejor su responsabilidad. Adicionalmente, README menciona estado “Funcionando 100%”, inconsistente con el error de sintaxis actual en la app.
- **Tarea:**
  1. Mejorar el comentario de la función `generate_image` para reflejar comportamiento real.
  2. Ajustar en `README.md` la afirmación de estado para que sea verificable y alineada con el estado real del código.
- **Archivos afectados:** `app_enhanced.py`, `README.md`.
- **Criterio de aceptación:** Comentarios/documentación consistentes con el comportamiento verificable del proyecto.

## 4) Mejorar una prueba
- **Problema detectado:** No hay pruebas automáticas que detecten regresiones básicas de estructura o sintaxis.
- **Tarea:** Añadir una prueba mínima (por ejemplo con `pytest`) que valide:
  - Que `show_profile()`, `show_prompts()`, `show_monetization()`, `show_tools()` y `show_stats()` retornan `str` no vacíos.
  - Que la estructura principal de `PROMPTS` y `MODELS` no esté vacía.
- **Archivo sugerido:** `tests/test_app_enhanced_smoke.py`.
- **Criterio de aceptación:** `pytest` pasa localmente y falla si se rompe la estructura base.
