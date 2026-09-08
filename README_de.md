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
python3 examples/astra.py vision --image assets/screenshots/iphone-archive.png
python3 examples/astra.py research
python3 examples/astra.py extract
node examples/quickstart.mjs
```

[Codebeispiele](examples/README.md) · [Python](examples/astra.py) · [JavaScript](examples/quickstart.mjs)

## Projekte und echte Screenshots

Diese Bilder wurden tatsächlich im Browser aufgenommen. Die Werke gehören ihren Urhebern; die Projekte wurden nicht vollständig nachgebaut.

![Dampflokomotive von Tom Krcha: Aufnahme der Seite mit seiner Vorschau.](assets/screenshots/steam-train-reference.png)

Dampflokomotive von Tom Krcha: Aufnahme der Seite mit seiner Vorschau. [Originalbeitrag](https://x.com/tomkrcha/status/2095756085890310311)

![iPhone Archive von bluedev: im Browser geöffnete öffentliche Seite.](assets/screenshots/iphone-archive.png)

iPhone Archive von bluedev: im Browser geöffnete öffentliche Seite. [Originalbeitrag](https://x.com/blueemi99/status/2096917792737911131) · [Live-Projekt](https://iphone-archive.vercel.app/)

![Seoul 3D Atlas von synabreu: City und Sunset wurden geprüft.](assets/screenshots/seoul-atlas.png)

Seoul 3D Atlas von synabreu: City und Sunset wurden geprüft. [Originalbeitrag](https://x.com/synabreu/status/2096557555086725159) · [Live-Projekt](https://seoul-3d-atlas.synabreu.chatgpt.site/)

[Screenshot-Quellen](assets/screenshots/README.md) · [12 Fallbeispiele](docs/cases.md)

## Praktische Arbeitsabläufe

Baue zuerst eine kleine funktionierende Version. Verbessere sie anhand echter Screenshots, Fehler und Abnahmekriterien. Fordere editierbare Dateien, Startanweisungen und Aufnahmen des tatsächlichen Ergebnisses an.

[6 Workflows](docs/workflows.md)

## Prüfung und Beiträge

17 Offline-Tests wurden bestanden. Es gab keine kostenpflichtigen API-Aufrufe und keine vollständige Reproduktion der Projekte. [Prüfprotokoll](docs/verification.md) · [Quellen](docs/sources.md) · [Beiträge](CONTRIBUTING.md). Eigene Inhalte und Code stehen unter [MIT](LICENSE); fremde Materialien behalten ihre Rechte.

## Über flaq.ai

[flaq.ai](https://flaq.ai/) bietet einen einheitlichen API-Zugang zu Bild-, Video-, Musik- und Sprachmodellen für KI-Agenten und produktive Anwendungen. Unser Team teilt hier praktisch nutzbare Methoden. Open-Source-Workflows: [Backlink Skills](https://github.com/flaqai/backlink_skills).

## Affiliate-Marketing und Partnerunterstützung

Kreative, Entwickler und Lehrende können dem [Flaq.ai-Affiliate-Programm](https://flaq.ai/affiliate-program/) beitreten und eigene Empfehlungslinks in Tutorials, Rezensionen und Integrationsanleitungen nutzen.

**20 %** für die erste gültige bezahlte Bestellung eines empfohlenen Nutzers, danach **10 %**. Berücksichtigt werden berechtigte Bestellungen innerhalb von **60 Tagen nach seiner Registrierung**.

Nach Anmeldung und Profilvervollständigung kannst du Links, Empfehlungen und Auszahlungseinstellungen verwalten. Kennzeichne Affiliate-Links deutlich. Berechtigung, Prüfung und Auszahlung richten sich nach der aktuellen [Vereinbarung](https://flaq.ai/affiliate-agreement/); Einnahmen werden nicht garantiert.
