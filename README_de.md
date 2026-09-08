# GPT-6 Astra Praxisleitfaden

Der aktuelle GPT-6-Astra-Leitfaden des **[flaq.ai](https://flaq.ai/)-Teams**: Modellgrundlagen, Einstieg, ausführbare Beispiele, kreative Arbeitsabläufe und echte Screenshots.

<!-- languages:start -->
[English](README.md) · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · **Deutsch** · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

Zuletzt geprüft: 2026-09-08. Ein unabhängiger Leitfaden des Teams, keine offizielle OpenAI-Dokumentation. Die READMEs sind in 12 Sprachen verfügbar; ausführliche Tutorials und Diagnosemeldungen sind derzeit auf vereinfachtem Chinesisch.

[Einstieg](docs/quickstart.md) · [12 Fallbeispiele](docs/cases.md) · [6 Workflows](docs/workflows.md) · [Codebeispiele](examples/README.md)

## Was ist Astra?

Astra ist ein OpenAI-Modell für komplexes Schlussfolgern, Programmierung, Recherche und mehrstufige Aufgaben. Es verarbeitet Text und Bilder und gibt Text aus. Browserbedienung, Softwareausführung und Videoproduktion benötigen passende Werkzeuge in der Anwendung.

| Modell | `gpt-6-astra` |
| --- | --- |
| Kontext | 1,050,000 tokens |
| Maximale Ausgabe | 128,000 tokens |
| Denkaufwand | `low` · `medium` · `high` · `xhigh` · `max` |

[Offizielle Modelldokumentation](https://developers.openai.com/api/docs/models/gpt-6-astra) · [Parameter und erweiterte Funktionen](https://developers.openai.com/api/docs/guides/latest-model)

## Ohne Programmieren starten

Wähle Astra in einem Produkt mit entsprechendem Zugang, stelle Material bereit und beginne mit einem kleinen Ergebnis. Zum Beispiel:

```text
Plane eine zweitägige Aktion für ein Café. Budget: 2.000 Yuan, zwei Mitarbeitende. Liefere Regeln, Zeitplan, Einzelbudget und drei Werbetexte. Prüfe die Summe und kennzeichne Annahmen.
```

## Das erste Beispiel ausführen

Verwende Python 3.10+ oder Node.js 20+ im Stammverzeichnis des Repositorys. Die Skripte nutzen eingebaute Bibliotheken; zusätzliche Pakete sind nicht nötig. Prüfe zuerst kostenlos die Anfrage:

```bash
python3 examples/astra.py text --dry-run
node examples/quickstart.mjs --dry-run
```

Für einen echten Aufruf setzt du `OPENAI_API_KEY` im Terminal auf den Schlüssel eines OpenAI-Projekts mit Astra-Zugang. Siehe [Einrichtung](docs/quickstart.md#用-api-开始). Keine Schlüssel in Code oder Screenshots speichern. `--dry-run` bleibt offline; echte Anfragen kosten Geld. Die Beispiele verwenden direkt OpenAI. Die Modellverfügbarkeit bei Flaq.ai ist separat zu prüfen.

```bash
python3 examples/astra.py text --prompt 'Plane eine zweitägige Aktion für ein Café. Budget: 2.000 Yuan, zwei Mitarbeitende. Liefere Regeln, Zeitplan, Einzelbudget und drei Werbetexte. Prüfe die Summe und kennzeichne Annahmen.'
python3 examples/astra.py vision --image assets/screenshots/workshop-budget.png
python3 examples/astra.py research
python3 examples/astra.py extract
node examples/quickstart.mjs
```

[Codebeispiele](examples/README.md) · [Python](examples/astra.py) · [JavaScript](examples/quickstart.mjs)

## Unsere eigenen Übungen ausführen

Drei eigenständig entwickelte Übungen nutzen dieselben fiktiven Studiodaten. Die Bilder sind echte Browseraufnahmen lokal erzeugter SVG-Berichte, keine Werke Dritter oder gemessenen Astra-API-Ergebnisse.

```bash
python3 examples/field_lab.py
# Alternative scenario / 独立输出目录
python3 examples/field_lab.py --guests 32 --out outputs/field-lab-32
```

![Budget: 2.168 CNY Ausgaben, 432 CNY Reserve.](assets/screenshots/workshop-budget.png)

Budget: 2.168 CNY Ausgaben, 432 CNY Reserve.

![Storyboard: 20 Sekunden bei 30 fps, 600 lückenlose Frames.](assets/screenshots/craft-storyboard.png)

Storyboard: 20 Sekunden bei 30 fps, 600 lückenlose Frames.

![Freigabeprüfung: 3 von 5 fiktiven Prüfungen bestanden, 2 offen.](assets/screenshots/release-review.png)

Freigabeprüfung: 3 von 5 fiktiven Prüfungen bestanden, 2 offen.

[Quellcode, Reproduktion und Übungen](docs/original-lab.md) · [SVG / PNG](assets/screenshots/README.md)

## Praktische Arbeitsabläufe

Baue zuerst eine kleine funktionierende Version. Verbessere sie anhand echter Screenshots, Fehler und Abnahmekriterien. Fordere editierbare Dateien, Startanweisungen und Aufnahmen des tatsächlichen Ergebnisses an.

[6 Workflows](docs/workflows.md)

## Prüfung und Beiträge

28 Offline-Tests wurden bestanden. Es gab keine kostenpflichtigen API-Aufrufe und keine vollständige Reproduktion der Projekte. [Prüfprotokoll](docs/verification.md) · [Quellen](docs/sources.md) · [Beiträge](CONTRIBUTING.md). Eigene Inhalte und Code stehen unter [MIT](LICENSE); fremde Materialien behalten ihre Rechte.

## 3D zum Ausprobieren: ein Roboter baut sich zusammen

Sechs eigene Übungen: Tischroboter, Montageanimation, Leseecke, Papierstromkreis-Kurzfilm, Pilzmaskottchen und Szenenprüfung. Der englisch/chinesische Leitfaden enthält Prompts, Einrichtung und ein eigenes Skript. Nur die Python-Syntax wurde geprüft; kein Blender-Lauf wurde getestet.

[Blender-Praxisleitfaden](docs/blender-playbook.md) · [Python](examples/blender/desk_robot.py)

## Über flaq.ai

[flaq.ai](https://flaq.ai/) bietet einen einheitlichen API-Zugang zu Bild-, Video-, Musik- und Sprachmodellen für KI-Agenten und produktive Anwendungen. Unser Team teilt hier praktisch nutzbare Methoden. Open-Source-Workflows: [Backlink Skills](https://github.com/flaqai/backlink_skills).

## Affiliate-Marketing und Partnerunterstützung

Kreative, Entwickler und Lehrende können dem [Flaq.ai-Affiliate-Programm](https://flaq.ai/affiliate-program/) beitreten und eigene Empfehlungslinks in Tutorials, Rezensionen und Integrationsanleitungen nutzen.

**20 %** für die erste gültige bezahlte Bestellung eines empfohlenen Nutzers, danach **10 %**. Berücksichtigt werden berechtigte Bestellungen innerhalb von **60 Tagen nach seiner Registrierung**.

Nach Anmeldung und Profilvervollständigung kannst du Links, Empfehlungen und Auszahlungseinstellungen verwalten. Kennzeichne Affiliate-Links deutlich. Berechtigung, Prüfung und Auszahlung richten sich nach der aktuellen [Vereinbarung](https://flaq.ai/affiliate-agreement/); Einnahmen werden nicht garantiert.

## Quellen und Inspiration

[用GPT-6 Astra操控Blender玩3D，保姆级教程来了。](https://mp.weixin.qq.com/s/yK65CvMwzhQqu5_E5EfVVQ)

Veröffentlicht von 数字生命卡兹克; Autoren: 卡兹克、可达; 2026-09-08. Inspiration für den Ablauf; Bilder und lange Prompts des Artikels werden nicht übernommen.
