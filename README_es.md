# Guía práctica de GPT-6 Astra

La guía más reciente de GPT-6 Astra, preparada por el **equipo de [flaq.ai](https://flaq.ai/)**: conceptos básicos, primeros pasos, código ejecutable, flujos creativos y capturas reales.

<!-- languages:start -->
[English](README.md) · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · **Español** · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

## Más ideas desde X

2026-09-22: ocho ejercicios derivados de siete publicaciones leídas directamente: subtítulos, color, migración de motores, recursos modulares, arte en hojas de cálculo, almacenes, fuentes históricas y criterios de finalización. Incluyen fuentes y límites de verificación; los resultados no se han reproducido. Resumen en inglés e instrucciones detalladas en chino.

[Guía de casos de X](docs/x-playbook.md) · [Registro de fuentes de X](docs/research/x-sources-2026-09-22.json)

Última revisión: 2026-09-08. Guía independiente del equipo, no documentación oficial de OpenAI. Hay README en 12 idiomas; los tutoriales detallados y los mensajes de diagnóstico están actualmente en chino simplificado.

[Primeros pasos](docs/quickstart.md) · [12 casos](docs/cases.md) · [6 flujos](docs/workflows.md) · [Código de ejemplo](examples/README.md)

## Qué es Astra

Astra es un modelo de OpenAI para razonamiento complejo, programación, investigación y tareas de varios pasos. Acepta texto e imágenes y genera texto. Navegar, ejecutar programas y crear vídeos requiere herramientas en la aplicación que lo utiliza.


[Documentación oficial](https://developers.openai.com/api/docs/models/gpt-6-astra) · [Parámetros y funciones avanzadas](https://developers.openai.com/api/docs/guides/latest-model)

## Empieza sin programar

Selecciona Astra en un producto al que tengas acceso, aporta tus materiales y pide un resultado pequeño. Por ejemplo:

```text
Planifica un evento de dos días para una cafetería. Presupuesto: 2.000 yuanes; dos empleados. Entrega reglas, horario, presupuesto desglosado y tres mensajes promocionales. Comprueba la suma e identifica las suposiciones.
```

## Úsalo directamente en tu cliente

Inicia sesión con ChatGPT; no necesitas configurar una clave API para empezar. El acceso a Astra y los límites dependen de tu cuenta y espacio de trabajo.

### ChatGPT

Inicia sesión en ChatGPT y elige Work para crear entregables. Selecciona Astra en modelo/Power; compruébalo en Advanced si aparece. Adjunta el presupuesto y pide comparar 24 y 32 asistentes.

### Codex

Inicia sesión en el cliente Codex; en la aplicación unificada, cambia a Codex. Abre una carpeta local, crea una tarea, elige Astra y pide ejecutar el laboratorio y entregar archivos con comprobaciones reales.

### Codex CLI

[Instalar CLI](https://learn.chatgpt.com/docs/cli). Instala la CLI desde la página oficial y ejecútala en tu proyecto. La primera vez elige Sign in with ChatGPT. Dentro de la sesión, usa /model para confirmar Astra y /status para ver la configuración; después describe tu tarea.

```bash
codex -m gpt-6-astra
```

[Pasos detallados (chino)](docs/quickstart.md) · [English](README.md) · [Models](https://learn.chatgpt.com/docs/models)

<details>
<summary>API opcional para integrar tu propia aplicación</summary>

[API](docs/api.md) · [Python / JavaScript](examples/README.md)

</details>

## Ejecuta nuestro laboratorio original

Tres ejercicios de creación propia comparten un caso ficticio. Las imágenes son capturas reales del navegador de informes SVG generados localmente, no obras de terceros ni resultados medidos de la API de Astra.

```bash
python3 examples/field_lab.py
# Alternative scenario / 独立输出目录
python3 examples/field_lab.py --guests 32 --out outputs/field-lab-32
```

![Presupuesto: 2.168 CNY de gasto y 432 CNY de reserva.](assets/screenshots/workshop-budget.png)

Presupuesto: 2.168 CNY de gasto y 432 CNY de reserva.

![Guion gráfico: 20 segundos a 30 fps, con 600 fotogramas continuos.](assets/screenshots/craft-storyboard.png)

Guion gráfico: 20 segundos a 30 fps, con 600 fotogramas continuos.

![Revisión: 3 de 5 comprobaciones ficticias superadas; 2 pendientes.](assets/screenshots/release-review.png)

Revisión: 3 de 5 comprobaciones ficticias superadas; 2 pendientes.

[Código, reproducción y ejercicios](docs/original-lab.md) · [SVG / PNG](assets/screenshots/README.md)

## Flujos de trabajo

Construye primero una versión mínima que funcione y mejora a partir de capturas, errores y criterios de aceptación. Pide archivos editables, instrucciones de arranque y capturas del resultado real.

[6 flujos](docs/workflows.md)

## Verificación y contribuciones

Los ejemplos superaron 28 pruebas sin conexión. No se realizaron llamadas de pago a la API ni una reproducción completa de los proyectos. [Verificación](docs/verification.md) · [Fuentes](docs/sources.md) · [Contribuir](CONTRIBUTING.md). El contenido y código propios usan [MIT](LICENSE); los materiales de terceros conservan sus derechos.

## 3D divertido: un robot que se monta solo

Seis ejercicios originales: robot de escritorio, montaje animado, rincón de lectura, corto de circuitos de papel, mascota hongo e inspección de escenas. La guía en inglés y chino incluye instrucciones, configuración y un script original. Solo se comprobó su sintaxis; no se ejecutó en Blender.

[Guía práctica de Blender](docs/blender-playbook.md) · [Python](examples/blender/desk_robot.py)

## Acerca de flaq.ai

[flaq.ai](https://flaq.ai/) ofrece acceso mediante una API unificada a modelos de imagen, vídeo, música y lenguaje para agentes de IA y aplicaciones en producción. Nuestro equipo comparte métodos prácticos con esta guía. Flujos de código abierto: [Backlink Skills](https://github.com/flaqai/backlink_skills).

## Afiliación y apoyo a colaboradores

Creadores, desarrolladores y educadores pueden unirse al [programa de afiliados de Flaq.ai](https://flaq.ai/affiliate-program/) y compartir tutoriales, reseñas e integraciones con su propio enlace de referido.

**20%** por el primer pedido válido pagado del usuario referido y **10%** por los siguientes. Los pedidos elegibles deben realizarse en los **60 días posteriores al registro** del usuario referido.

Inicia sesión y completa el perfil para gestionar enlaces, referidos y cobros. Identifica claramente los enlaces de afiliado. La elegibilidad, revisión y liquidación siguen el [acuerdo vigente](https://flaq.ai/affiliate-agreement/); no se garantizan ingresos.

## Referencias e inspiración

[用GPT-6 Astra操控Blender玩3D，保姆级教程来了。](https://mp.weixin.qq.com/s/yK65CvMwzhQqu5_E5EfVVQ)

Publicado por 数字生命卡兹克; autores: 卡兹克、可达; 2026-09-08. Inspiración para el flujo de trabajo; no se reproducen imágenes ni instrucciones largas del artículo.

[Registro de fuentes de X · 2026-09-22](docs/x-playbook.md) · [JSON](docs/research/x-sources-2026-09-22.json)
