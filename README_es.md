# Guía práctica de GPT-6 Astra

La guía más reciente de GPT-6 Astra, preparada por el **equipo de [flaq.ai](https://flaq.ai/)**: conceptos básicos, primeros pasos, código ejecutable, flujos creativos y capturas reales.

<!-- languages:start -->
[English](README.md) · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · **Español** · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

Última revisión: 2026-09-08. Guía independiente del equipo, no documentación oficial de OpenAI. Hay README en 12 idiomas; los tutoriales detallados y los mensajes de diagnóstico están actualmente en chino simplificado.

[Primeros pasos](docs/quickstart.md) · [12 casos](docs/cases.md) · [6 flujos](docs/workflows.md) · [Código de ejemplo](examples/README.md)

## Qué es Astra

Astra es un modelo de OpenAI para razonamiento complejo, programación, investigación y tareas de varios pasos. Acepta texto e imágenes y genera texto. Navegar, ejecutar programas y crear vídeos requiere herramientas en la aplicación que lo utiliza.

| Modelo | `gpt-6-astra` |
| --- | --- |
| Contexto | 1,050,000 tokens |
| Salida máxima | 128,000 tokens |
| Nivel de razonamiento | `low` · `medium` · `high` · `xhigh` · `max` |

[Documentación oficial](https://developers.openai.com/api/docs/models/gpt-6-astra) · [Parámetros y funciones avanzadas](https://developers.openai.com/api/docs/guides/latest-model)

## Empieza sin programar

Selecciona Astra en un producto al que tengas acceso, aporta tus materiales y pide un resultado pequeño. Por ejemplo:

```text
Planifica un evento de dos días para una cafetería. Presupuesto: 2.000 yuanes; dos empleados. Entrega reglas, horario, presupuesto desglosado y tres mensajes promocionales. Comprueba la suma e identifica las suposiciones.
```

## Ejecuta tu primer ejemplo

Usa Python 3.10+ o Node.js 20+ desde la raíz del repositorio. Los scripts incluidos utilizan bibliotecas integradas, sin instalar paquetes. Primero consulta la petición gratis:

```bash
python3 examples/astra.py text --dry-run
node examples/quickstart.mjs --dry-run
```

Para una llamada real, configura `OPENAI_API_KEY` en la terminal con una clave de un proyecto OpenAI que tenga acceso a Astra. Consulta la [configuración](docs/quickstart.md#用-api-开始). No incluyas claves en código ni capturas. `--dry-run` no se conecta; las peticiones reales tienen coste. Los ejemplos llaman directamente a OpenAI; consulta por separado la disponibilidad del modelo en Flaq.ai.

```bash
python3 examples/astra.py text --prompt 'Planifica un evento de dos días para una cafetería. Presupuesto: 2.000 yuanes; dos empleados. Entrega reglas, horario, presupuesto desglosado y tres mensajes promocionales. Comprueba la suma e identifica las suposiciones.'
python3 examples/astra.py vision --image assets/screenshots/iphone-archive.png
python3 examples/astra.py research
python3 examples/astra.py extract
node examples/quickstart.mjs
```

[Código de ejemplo](examples/README.md) · [Python](examples/astra.py) · [JavaScript](examples/quickstart.mjs)

## Proyectos y capturas reales

Estas imágenes son capturas reales del navegador. Los derechos corresponden a sus creadores; no se han reproducido íntegramente los proyectos.

![Tren de vapor de Tom Krcha: captura de la página que muestra su vista previa.](assets/screenshots/steam-train-reference.png)

Tren de vapor de Tom Krcha: captura de la página que muestra su vista previa. [Publicación original](https://x.com/tomkrcha/status/2095756085890310311)

![iPhone Archive de bluedev: página pública abierta en el navegador.](assets/screenshots/iphone-archive.png)

iPhone Archive de bluedev: página pública abierta en el navegador. [Publicación original](https://x.com/blueemi99/status/2096917792737911131) · [Proyecto en línea](https://iphone-archive.vercel.app/)

![Seoul 3D Atlas de synabreu: se comprobaron los modos City y Sunset.](assets/screenshots/seoul-atlas.png)

Seoul 3D Atlas de synabreu: se comprobaron los modos City y Sunset. [Publicación original](https://x.com/synabreu/status/2096557555086725159) · [Proyecto en línea](https://seoul-3d-atlas.synabreu.chatgpt.site/)

[Origen de las capturas](assets/screenshots/README.md) · [12 casos](docs/cases.md)

## Flujos de trabajo

Construye primero una versión mínima que funcione y mejora a partir de capturas, errores y criterios de aceptación. Pide archivos editables, instrucciones de arranque y capturas del resultado real.

[6 flujos](docs/workflows.md)

## Verificación y contribuciones

Los ejemplos superaron 17 pruebas sin conexión. No se realizaron llamadas de pago a la API ni una reproducción completa de los proyectos. [Verificación](docs/verification.md) · [Fuentes](docs/sources.md) · [Contribuir](CONTRIBUTING.md). El contenido y código propios usan [MIT](LICENSE); los materiales de terceros conservan sus derechos.

## Acerca de flaq.ai

[flaq.ai](https://flaq.ai/) ofrece acceso mediante una API unificada a modelos de imagen, vídeo, música y lenguaje para agentes de IA y aplicaciones en producción. Nuestro equipo comparte métodos prácticos con esta guía. Flujos de código abierto: [Backlink Skills](https://github.com/flaqai/backlink_skills).

## Afiliación y apoyo a colaboradores

Creadores, desarrolladores y educadores pueden unirse al [programa de afiliados de Flaq.ai](https://flaq.ai/affiliate-program/) y compartir tutoriales, reseñas e integraciones con su propio enlace de referido.

**20%** por el primer pedido válido pagado del usuario referido y **10%** por los siguientes. Los pedidos elegibles deben realizarse en los **60 días posteriores al registro** del usuario referido.

Inicia sesión y completa el perfil para gestionar enlaces, referidos y cobros. Identifica claramente los enlaces de afiliado. La elegibilidad, revisión y liquidación siguen el [acuerdo vigente](https://flaq.ai/affiliate-agreement/); no se garantizan ingresos.
