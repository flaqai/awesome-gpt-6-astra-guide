# Guide pratique de GPT-6 Astra

Le dernier guide GPT-6 Astra préparé par **l’équipe [flaq.ai](https://flaq.ai/)** : présentation du modèle, prise en main, exemples exécutables, méthodes de création et captures réelles.

<!-- languages:start -->
[English](README.md) · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · **Français** · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

Dernière vérification : 2026-09-08. Ce guide indépendant ne constitue pas la documentation officielle d’OpenAI. Les README existent en 12 langues ; les tutoriels détaillés et les messages de diagnostic sont actuellement en chinois simplifié.

[Prise en main](docs/quickstart.md) · [12 exemples](docs/cases.md) · [6 workflows](docs/workflows.md) · [Exemples de code](examples/README.md)

## Comprendre Astra

Astra est un modèle OpenAI conçu pour le raisonnement complexe, le code, la recherche et les tâches en plusieurs étapes. Il reçoit du texte et des images et produit du texte. La navigation, l’exécution de logiciels et la création vidéo nécessitent des outils dans l’application utilisée.


[Documentation officielle](https://developers.openai.com/api/docs/models/gpt-6-astra) · [Paramètres et fonctions avancées](https://developers.openai.com/api/docs/guides/latest-model)

## Commencer sans coder

Sélectionnez Astra dans un produit auquel vous avez accès, fournissez vos documents et demandez un petit livrable. Par exemple :

```text
Prépare un événement de deux jours pour un café. Budget : 2 000 yuans, avec deux employés. Fournis les règles, le planning, un budget détaillé et trois messages promotionnels. Vérifie le total et indique les hypothèses.
```

## Utiliser directement dans votre client

Connectez-vous avec ChatGPT, sans configurer de clé API au préalable. L’accès à Astra et les limites dépendent du compte et de l’espace de travail.

### ChatGPT

Connectez-vous à ChatGPT et choisissez Work pour les livrables. Sélectionnez Astra dans modèle/Power, puis Advanced si nécessaire. Joignez le budget et demandez une comparaison entre 24 et 32 personnes.

### Codex

Connectez-vous au client Codex ; dans l’application unifiée, passez à Codex. Ouvrez un dossier local, créez une tâche, choisissez Astra et demandez l’exécution du laboratoire avec fichiers et vérifications réelles.

### Codex CLI

[Installer la CLI](https://learn.chatgpt.com/docs/cli). Installez la CLI depuis la page officielle et lancez-la dans votre projet. Choisissez Sign in with ChatGPT au premier lancement. Dans la session, /model permet de confirmer Astra et /status de vérifier les réglages ; décrivez ensuite votre tâche.

```bash
codex -m gpt-6-astra
```

[Étapes détaillées (chinois)](docs/quickstart.md) · [English](README.md) · [Models](https://learn.chatgpt.com/docs/models)

<details>
<summary>API facultative pour intégrer votre application</summary>

[API](docs/api.md) · [Python / JavaScript](examples/README.md)

</details>

## Exécuter nos exercices originaux

Trois exercices conçus pour ce guide partagent un dossier fictif. Les images sont de vraies captures de rapports SVG générés localement, et non des œuvres de tiers ou des résultats mesurés de l’API Astra.

```bash
python3 examples/field_lab.py
# Alternative scenario / 独立输出目录
python3 examples/field_lab.py --guests 32 --out outputs/field-lab-32
```

![Budget : 2 168 CNY dépensés, 432 CNY en réserve.](assets/screenshots/workshop-budget.png)

Budget : 2 168 CNY dépensés, 432 CNY en réserve.

![Storyboard : 20 secondes à 30 fps, soit 600 images continues.](assets/screenshots/craft-storyboard.png)

Storyboard : 20 secondes à 30 fps, soit 600 images continues.

![Revue : 3 contrôles fictifs sur 5 réussis, 2 à corriger.](assets/screenshots/release-review.png)

Revue : 3 contrôles fictifs sur 5 réussis, 2 à corriger.

[Code, reproduction et exercices](docs/original-lab.md) · [SVG / PNG](assets/screenshots/README.md)

## Méthodes pratiques

Commencez par une version minimale fonctionnelle, puis corrigez-la à partir des captures, erreurs et critères de validation. Demandez des fichiers modifiables, une procédure de lancement et des captures du résultat réel.

[6 workflows](docs/workflows.md)

## Vérification et contributions

Les exemples ont passé 28 tests hors ligne. Aucun appel API payant ni reproduction complète des projets n’a été effectué. [Vérification](docs/verification.md) · [Sources](docs/sources.md) · [Contribuer](CONTRIBUTING.md). Les textes et le code originaux sont sous [MIT](LICENSE) ; les contenus tiers conservent leurs droits.

## 3D ludique : un robot qui s’assemble

Six exercices originaux : robot de bureau, assemblage animé, coin lecture, court métrage de circuits en papier, mascotte champignon et inspection de scène. Le guide anglais/chinois propose des consignes, la configuration et un script original. Seule sa syntaxe a été vérifiée ; il n’a pas été exécuté dans Blender.

[Guide pratique Blender](docs/blender-playbook.md) · [Python](examples/blender/desk_robot.py)

## À propos de flaq.ai

[flaq.ai](https://flaq.ai/) fournit une API unifiée pour des modèles d’image, de vidéo, de musique et de langage, destinée aux agents IA et aux applications en production. Notre équipe partage ici des méthodes concrètes. Workflows open source : [Backlink Skills](https://github.com/flaqai/backlink_skills).

## Affiliation et accompagnement des partenaires

Créateurs, développeurs et formateurs peuvent rejoindre le [programme d’affiliation Flaq.ai](https://flaq.ai/affiliate-program/) pour partager tutoriels, évaluations et guides d’intégration avec leur propre lien de parrainage.

**20 %** sur la première commande payante valide du filleul, puis **10 %** sur les suivantes. Les commandes éligibles doivent être passées dans les **60 jours suivant son inscription**.

Connectez-vous et complétez votre profil pour gérer les liens, les parrainages et les paramètres de versement. Signalez clairement les liens affiliés. Éligibilité, vérification et paiement suivent l’[accord en vigueur](https://flaq.ai/affiliate-agreement/) ; aucun revenu n’est garanti.

## Références et inspiration

[用GPT-6 Astra操控Blender玩3D，保姆级教程来了。](https://mp.weixin.qq.com/s/yK65CvMwzhQqu5_E5EfVVQ)

Publication : 数字生命卡兹克 ; auteurs : 卡兹克、可达 ; 2026-09-08. Source d’inspiration pour la méthode, sans reprise des images ni des longues consignes de l’article.
