# Guide pratique de GPT-6 Astra

Le dernier guide GPT-6 Astra préparé par **l’équipe [flaq.ai](https://flaq.ai/)** : présentation du modèle, prise en main, exemples exécutables, méthodes de création et captures réelles.

<!-- languages:start -->
[English](README.md) · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · **Français** · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

Dernière vérification : 2026-09-08. Ce guide indépendant ne constitue pas la documentation officielle d’OpenAI. Les README existent en 12 langues ; les tutoriels détaillés et les messages de diagnostic sont actuellement en chinois simplifié.

[Prise en main](docs/quickstart.md) · [12 exemples](docs/cases.md) · [6 workflows](docs/workflows.md) · [Exemples de code](examples/README.md)

## Comprendre Astra

Astra est un modèle OpenAI conçu pour le raisonnement complexe, le code, la recherche et les tâches en plusieurs étapes. Il reçoit du texte et des images et produit du texte. La navigation, l’exécution de logiciels et la création vidéo nécessitent des outils dans l’application utilisée.

| Modèle | `gpt-6-astra` |
| --- | --- |
| Contexte | 1,050,000 tokens |
| Sortie maximale | 128,000 tokens |
| Effort de raisonnement | `low` · `medium` · `high` · `xhigh` · `max` |

[Documentation officielle](https://developers.openai.com/api/docs/models/gpt-6-astra) · [Paramètres et fonctions avancées](https://developers.openai.com/api/docs/guides/latest-model)

## Commencer sans coder

Sélectionnez Astra dans un produit auquel vous avez accès, fournissez vos documents et demandez un petit livrable. Par exemple :

```text
Prépare un événement de deux jours pour un café. Budget : 2 000 yuans, avec deux employés. Fournis les règles, le planning, un budget détaillé et trois messages promotionnels. Vérifie le total et indique les hypothèses.
```

## Exécuter un premier exemple

Utilisez Python 3.10+ ou Node.js 20+ depuis la racine du dépôt. Les scripts utilisent les bibliothèques intégrées et ne nécessitent aucune installation de paquet. Prévisualisez d’abord la requête gratuitement :

```bash
python3 examples/astra.py text --dry-run
node examples/quickstart.mjs --dry-run
```

Pour un appel réel, définissez `OPENAI_API_KEY` dans le terminal avec la clé d’un projet OpenAI ayant accès à Astra. Consultez la [configuration](docs/quickstart.md#用-api-开始). Ne mettez pas de clé dans le code ou les captures. `--dry-run` ne se connecte pas ; les appels réels sont payants. Les exemples utilisent directement OpenAI. Vérifiez séparément les modèles proposés sur Flaq.ai.

```bash
python3 examples/astra.py text --prompt 'Prépare un événement de deux jours pour un café. Budget : 2 000 yuans, avec deux employés. Fournis les règles, le planning, un budget détaillé et trois messages promotionnels. Vérifie le total et indique les hypothèses.'
python3 examples/astra.py vision --image assets/screenshots/iphone-archive.png
python3 examples/astra.py research
python3 examples/astra.py extract
node examples/quickstart.mjs
```

[Exemples de code](examples/README.md) · [Python](examples/astra.py) · [JavaScript](examples/quickstart.mjs)

## Projets et captures réelles

Ces images ont été capturées dans le navigateur. Les œuvres appartiennent à leurs créateurs ; les projets n’ont pas été reproduits intégralement.

![Train à vapeur de Tom Krcha : capture de la page présentant son aperçu.](assets/screenshots/steam-train-reference.png)

Train à vapeur de Tom Krcha : capture de la page présentant son aperçu. [Publication originale](https://x.com/tomkrcha/status/2095756085890310311)

![iPhone Archive de bluedev : page publique ouverte dans le navigateur.](assets/screenshots/iphone-archive.png)

iPhone Archive de bluedev : page publique ouverte dans le navigateur. [Publication originale](https://x.com/blueemi99/status/2096917792737911131) · [Projet en ligne](https://iphone-archive.vercel.app/)

![Seoul 3D Atlas de synabreu : les modes City et Sunset ont été vérifiés.](assets/screenshots/seoul-atlas.png)

Seoul 3D Atlas de synabreu : les modes City et Sunset ont été vérifiés. [Publication originale](https://x.com/synabreu/status/2096557555086725159) · [Projet en ligne](https://seoul-3d-atlas.synabreu.chatgpt.site/)

[Origine des captures](assets/screenshots/README.md) · [12 exemples](docs/cases.md)

## Méthodes pratiques

Commencez par une version minimale fonctionnelle, puis corrigez-la à partir des captures, erreurs et critères de validation. Demandez des fichiers modifiables, une procédure de lancement et des captures du résultat réel.

[6 workflows](docs/workflows.md)

## Vérification et contributions

Les exemples ont passé 17 tests hors ligne. Aucun appel API payant ni reproduction complète des projets n’a été effectué. [Vérification](docs/verification.md) · [Sources](docs/sources.md) · [Contribuer](CONTRIBUTING.md). Les textes et le code originaux sont sous [MIT](LICENSE) ; les contenus tiers conservent leurs droits.

## À propos de flaq.ai

[flaq.ai](https://flaq.ai/) fournit une API unifiée pour des modèles d’image, de vidéo, de musique et de langage, destinée aux agents IA et aux applications en production. Notre équipe partage ici des méthodes concrètes. Workflows open source : [Backlink Skills](https://github.com/flaqai/backlink_skills).

## Affiliation et accompagnement des partenaires

Créateurs, développeurs et formateurs peuvent rejoindre le [programme d’affiliation Flaq.ai](https://flaq.ai/affiliate-program/) pour partager tutoriels, évaluations et guides d’intégration avec leur propre lien de parrainage.

**20 %** sur la première commande payante valide du filleul, puis **10 %** sur les suivantes. Les commandes éligibles doivent être passées dans les **60 jours suivant son inscription**.

Connectez-vous et complétez votre profil pour gérer les liens, les parrainages et les paramètres de versement. Signalez clairement les liens affiliés. Éligibilité, vérification et paiement suivent l’[accord en vigueur](https://flaq.ai/affiliate-agreement/) ; aucun revenu n’est garanti.
