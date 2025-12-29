"""
Sofia Rivera Workspace - Enhanced Version
Workspace mejorado con galería y generador de imágenes
"""

import gradio as gr
import os
from datetime import datetime
from huggingface_hub import InferenceClient
import random

# Initialize Inference Client
client = InferenceClient()

# Sofia Rivera - Perfil Completo
PROFILE = {
    "nombre": "Sofia Rivera",
    "edad": 25,
    "origen": "Miami, Florida",
    "etnia": "Latina (Cubana-Americana)",
    "profesion": "Influencer de Lifestyle & Fitness",
    "nichos": ["Fitness", "Wellness", "Fashion", "Lifestyle", "Motivación"],
    "idiomas": ["Español", "Inglés"],
    "instagram_bio": "✨ Sofia Rivera | Miami 🌴\n💪 Fitness & Wellness Journey\n🎯 Lifestyle Content Creator\n👗 Fashion | Beauty | Motivation\n📩 DM for collabs\n🔥 Premium content below ⬇️"
}

# Prompts para generar imágenes
PROMPTS = [
    {
        "id": 1,
        "tipo": "Lifestyle - Golden Hour Selfie",
        "prompt": "professional iphone selfie photo of sofia rivera, beautiful 25 year old latina cuban-american woman, long dark wavy hair, warm genuine smile, hazel eyes, natural makeup, wearing white crop tank top, black yoga pants, taken in luxury miami apartment with ocean view, golden hour lighting from floor-to-ceiling windows, bokeh background, shot on iPhone 15 Pro Max, instagram influencer aesthetic, fitness lifestyle content creator, authentic candid moment",
        "negative_prompt": "blurry, low quality, distorted, deformed, ugly, bad anatomy",
        "uso": "Instagram feed, posts casuales, get to know me"
    },
    {
        "id": 2,
        "tipo": "Fitness - Gym Mirror Selfie",
        "prompt": "full body mirror selfie of sofia rivera, 25 year old latina fitness influencer, toned athletic body, wearing black sports bra and matching high-waist leggings, taken in modern home gym with mirrors, natural window lighting, confident pose showing fitness results, authentic instagram fitness post, shot on iphone, miami lifestyle content creator",
        "negative_prompt": "blurry, low quality, distorted, bad proportions",
        "uso": "Contenido fitness/wellness, Stories, motivación"
    },
    {
        "id": 3,
        "tipo": "Premium - Boudoir",
        "prompt": "sofia rivera bedroom selfie, 25 year old latina influencer, wearing delicate white lace lingerie set, soft morning light through sheer curtains, sitting on edge of luxurious bed with silk sheets, natural messy hair, sultry confident expression, shot on iPhone 15 Pro, premium onlyfans content style, tasteful boudoir photography aesthetic, professional quality, authentic intimate moment",
        "negative_prompt": "explicit, blurry, low quality, distorted",
        "uso": "Contenido premium monetizable, Fansly/OF, PPV"
    },
    {
        "id": 4,
        "tipo": "Fashion - Street Style",
        "prompt": "sofia rivera street style photo, 25 year old latina fashion influencer, wearing trendy miami outfit, designer sunglasses, natural confident pose, urban miami background, golden hour street photography, instagram fashion aesthetic, professional quality",
        "negative_prompt": "blurry, low quality, bad lighting",
        "uso": "Fashion content, Instagram feed"
    },
    {
        "id": 5,
        "tipo": "Beach Lifestyle",
        "prompt": "sofia rivera beach lifestyle photo, 25 year old latina influencer, miami beach background, sunset lighting, casual beach outfit, natural happy expression, tropical vibes, instagram lifestyle content",
        "negative_prompt": "blurry, low quality, distorted",
        "uso": "Lifestyle content, Stories, feed"
    }


# Modelos disponibles para generación
MODELS = [
    "black-forest-labs/FLUX.1-dev",
    "black-forest-labs/FLUX.1-schnell",
    "stabilityai/stable-diffusion-xl-base-1.0",
    "runwayml/stable-diffusion-v1-5"
]

# Función para generar imagen
def generate_image(prompt, negative_prompt="", model="black-forest-labs/FLUX.1-dev", seed=None):
    try:
        if seed is None:
            seed = random.randint(0, 2147483647)
        
        image = client.text_to_image(
            prompt=prompt,
            negative_prompt=negative_prompt,
            model=model,
            guidance_scale=7.5,
            num_inference_steps=50
        )
        
        status = f"✅ Imagen generada exitosamente\nModelo: {model}\nSeed: {seed}"
        return image, status
    
    except Exception as e:
        error_msg = f"❌ Error al generar imagen: {str(e)}"
        return None, error_msg

# Función de perfil
def show_profile():
    profile_text = f"""# 👤 Perfil de Sofia Rivera

**Nombre:** {PROFILE['nombre']}
**Edad:** {PROFILE['edad']} años
**Origen:** {PROFILE['origen']}
**Etnia:** {PROFILE['etnia']}
**Profesión:** {PROFILE['profesion']}

**Nichos:** {', '.join(PROFILE['nichos'])}
**Idiomas:** {', '.join(PROFILE['idiomas'])}

---

## 📱 Bio de Instagram:
```
{PROFILE['instagram_bio']}
```
"""
    return profile_text]

# Función para mostrar prompts
def show_prompts():
    prompts_text = "# 🎨 Prompts para Generación de Contenido\n\n"
    for p in PROMPTS:
        prompts_text += f"""## {p['tipo']}\n**ID:** {p['id']}\n**Uso:** {p['uso']}\n\n**Prompt:**\n```\n{p['prompt']}\n```\n\n**Negative Prompt:**\n```\n{p['negative_prompt']}\n```\n\n---\n\n"""
    return prompts_text

# Función para mostrar información de monetización
def show_monetization():
    return """# 💰 Estrategia de Monetización\n\n## Plataformas de Contenido Premium:\n- **OnlyFans**: Contenido exclusivo de fitness y lifestyle\n- **Fansly**: Contenido premium variado\n- **Patreon**: Acceso a rutinas y planes personalizados\n\n## Tipos de Contenido:\n1. **Free Feed (Instagram/TikTok)**: Contenido motivacional, fitness tips, lifestyle\n2. **Premium Content**: Fotos profesionales, behind-the-scenes, contenido más personal\n3. **PPV (Pay-Per-View)**: Contenido exclusivo de alta calidad\n\n## Precios Sugeridos:\n- Suscripción mensual: $9.99 - $19.99\n- PPV individual: $5 - $25\n- Custom content: $50+\n"""

# Función para mostrar herramientas
def show_tools():
    return """# 🛠️ Herramientas y Apps HuggingFace\n\n## Generadores de Imágenes:\n- **FLUX.1-dev**: Modelo principal de alta calidad\n- **FLUX.1-schnell**: Generación rápida\n- **Stable Diffusion XL**: Alternativa de alta resolución\n\n## Otras Herramientas Recomendadas:\n- **Upscaling**: Mejorar calidad de imágenes\n- **Background Removal**: Remover fondos\n- **Face Enhancement**: Mejorar detalles faciales\n"""

# Función para mostrar estadísticas
def show_stats():
    return f"""# 📊 Estadísticas del Workspace\n\n**Fecha de creación:** {datetime.now().strftime('%Y-%m-%d')}\n**Prompts disponibles:** {len(PROMPTS)}\n**Modelos de IA:** {len(MODELS)}\n\n## Actividad Reciente:\n- Workspace inicializado correctamente\n- Sistema de generación de imágenes activo\n- Todos los prompts configurados\n"""

# Crear la interfaz de Gradio
with gr.Blocks(title="Sofia Rivera Workspace") as demo:
    gr.Markdown("# ✨ Sofia Rivera - AI Influencer Workspace")
    gr.Markdown("Workspace profesional para creación de contenido con IA")
    
    with gr.Tabs():
        # Tab 1: Galería de Contenido
        with gr.Tab("🖼️ Galería"):
            gr.Markdown("## Galería de Contenido Generado")
            gr.Markdown("Aquí se mostrarán las imágenes generadas. Por ahora, usa el Generador para crear contenido.")
            gallery_output = gr.Gallery(label="Imágenes Generadas", columns=3, height="auto")
        
        # Tab 2: Generador de Imágenes
        with gr.Tab("🎨 Generador"):
            gr.Markdown("## Generador de Imágenes de Sofia Rivera")
            
            with gr.Row():
                with gr.Column():
                    prompt_input = gr.Textbox(label="Prompt", lines=5, placeholder="Escribe tu prompt aquí...")
                    negative_prompt_input = gr.Textbox(label="Negative Prompt", lines=2, value="blurry, low quality, distorted")
                    model_dropdown = gr.Dropdown(choices=MODELS, value=MODELS[0], label="Modelo")
                    seed_input = gr.Number(label="Seed (opcional)", value=None)
                    generate_btn = gr.Button("🚀 Generar Imagen", variant="primary")
                
                with gr.Column():
                    image_output = gr.Image(label="Imagen Generada")
                    status_output = gr.Textbox(label="Estado", lines=3)
            
            generate_btn.click(
                fn=generate_image,
                inputs=[prompt_input, negative_prompt_input, model_dropdown, seed_input],
                outputs=[image_output, status_output]
            )
        
        # Tab 3: Perfil
        with gr.Tab("👤 Perfil"):
            profile_display = gr.Markdown(show_profile())
        
        # Tab 4: Prompts
        with gr.Tab("📝 Prompts"):
            prompts_display = gr.Markdown(show_prompts())
        
        # Tab 5: Monetización
        with gr.Tab("💰 Monetización"):
            monetization_display = gr.Markdown(show_monetization())
        
        # Tab 6: Herramientas
        with gr.Tab("🛠️ Herramientas"):
            tools_display = gr.Markdown(show_tools())
        
        # Tab 7: Estadísticas
        with gr.Tab("📊 Estadísticas"):
            stats_display = gr.Markdown(show_stats())

# Lanzar la aplicación
if __name__ == "__main__":
    demo.launch()
