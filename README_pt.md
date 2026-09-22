# Guia prático do GPT-6 Astra

O guia mais recente do GPT-6 Astra, organizado pela **equipe da [flaq.ai](https://flaq.ai/)**: conceitos essenciais, primeiros passos, código executável, fluxos criativos e capturas reais.

<!-- languages:start -->
[English](README.md) · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · **Português** · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

## Mais ideias do X

2026-09-22: oito exercícios a partir de sete publicações lidas diretamente: legendas, cor, migração de motores, recursos modulares, pixel art em planilhas, armazém, fontes históricas e critérios de conclusão. Incluem fontes e limites de verificação; os resultados não foram reproduzidos. Resumo em inglês, instruções detalhadas em chinês.

[Guia de casos do X](docs/x-playbook.md) · [Registro de fontes do X](docs/research/x-sources-2026-09-22.json)

Última revisão: 2026-09-08. Este é um guia independente da equipe, não a documentação oficial da OpenAI. Os READMEs estão disponíveis em 12 idiomas; os tutoriais detalhados e as mensagens de diagnóstico estão atualmente em chinês simplificado.

[Primeiros passos](docs/quickstart.md) · [12 casos](docs/cases.md) · [6 fluxos](docs/workflows.md) · [Exemplos de código](examples/README.md)

## O que é Astra

Astra é um modelo da OpenAI para raciocínio complexo, programação, pesquisa e tarefas com várias etapas. Recebe texto e imagens e produz texto. Navegação, execução de software e criação de vídeos exigem ferramentas no aplicativo utilizado.


[Documentação oficial](https://developers.openai.com/api/docs/models/gpt-6-astra) · [Parâmetros e recursos avançados](https://developers.openai.com/api/docs/guides/latest-model)

## Comece sem programar

Selecione Astra em um produto ao qual você tenha acesso, forneça materiais e peça uma entrega pequena. Por exemplo:

```text
Planeje um evento de dois dias para uma cafeteria. Orçamento: 2.000 yuans, com dois funcionários. Entregue regras, cronograma, orçamento detalhado e três mensagens promocionais. Confira o total e indique as suposições.
```

## Use diretamente no cliente

Entre com sua conta ChatGPT; não é necessário configurar uma chave API para começar. O acesso ao Astra e os limites dependem da conta e do espaço de trabalho.

### ChatGPT

Entre no ChatGPT e escolha Work para criar entregáveis. Selecione Astra em modelo/Power, conferindo Advanced se disponível. Anexe o orçamento e peça uma comparação entre 24 e 32 participantes.

### Codex

Entre no cliente Codex; no aplicativo unificado, mude para Codex. Abra uma pasta local, crie uma tarefa com Astra e peça a execução do laboratório com arquivos e verificações reais.

### Codex CLI

[Instalar CLI](https://learn.chatgpt.com/docs/cli). Instale a CLI pela página oficial e inicie no projeto. Na primeira vez, escolha Sign in with ChatGPT. Na sessão, use /model para confirmar Astra e /status para consultar a configuração; depois descreva a tarefa.

```bash
codex -m gpt-6-astra
```

[Etapas detalhadas (chinês)](docs/quickstart.md) · [English](README.md) · [Models](https://learn.chatgpt.com/docs/models)

<details>
<summary>API opcional para integrar seu próprio aplicativo</summary>

[API](docs/api.md) · [Python / JavaScript](examples/README.md)

</details>

## Execute nosso laboratório original

Três exercícios de autoria própria compartilham um caso fictício. As imagens são capturas reais no navegador de relatórios SVG gerados localmente, não obras de terceiros nem resultados medidos da API Astra.

```bash
python3 examples/field_lab.py
# Alternative scenario / 独立输出目录
python3 examples/field_lab.py --guests 32 --out outputs/field-lab-32
```

![Orçamento: 2.168 CNY gastos e 432 CNY de reserva.](assets/screenshots/workshop-budget.png)

Orçamento: 2.168 CNY gastos e 432 CNY de reserva.

![Storyboard: 20 segundos a 30 fps, com 600 quadros contínuos.](assets/screenshots/craft-storyboard.png)

Storyboard: 20 segundos a 30 fps, com 600 quadros contínuos.

![Revisão: 3 de 5 verificações fictícias aprovadas; 2 pendentes.](assets/screenshots/release-review.png)

Revisão: 3 de 5 verificações fictícias aprovadas; 2 pendentes.

[Código, reprodução e exercícios](docs/original-lab.md) · [SVG / PNG](assets/screenshots/README.md)

## Fluxos de trabalho

Crie uma versão mínima funcional e melhore com base em capturas, erros e critérios de aceitação. Peça arquivos editáveis, instruções de execução e capturas do resultado real.

[6 fluxos](docs/workflows.md)

## Verificação e contribuições

Os exemplos passaram em 28 testes offline. Não houve chamadas pagas à API nem reprodução completa dos projetos. [Verificação](docs/verification.md) · [Fontes](docs/sources.md) · [Contribuir](CONTRIBUTING.md). O conteúdo e o código originais usam [MIT](LICENSE); os materiais de terceiros mantêm seus direitos.

## 3D divertido: um robô que se monta

Seis exercícios originais: robô de mesa, montagem animada, canto de leitura, curta de circuitos de papel, mascote cogumelo e inspeção de cenas. O guia em inglês/chinês inclui prompts, configuração e um script original. Apenas a sintaxe foi verificada; não houve execução no Blender.

[Guia prático de Blender](docs/blender-playbook.md) · [Python](examples/blender/desk_robot.py)

## Sobre a flaq.ai

[flaq.ai](https://flaq.ai/) oferece acesso por uma API unificada a modelos de imagem, vídeo, música e linguagem para agentes de IA e aplicações em produção. Nossa equipe compartilha métodos práticos neste guia. Fluxos de código aberto: [Backlink Skills](https://github.com/flaqai/backlink_skills).

## Programa de afiliados e apoio a parceiros

Criadores, desenvolvedores e educadores podem participar do [programa de afiliados da Flaq.ai](https://flaq.ai/affiliate-program/) e compartilhar tutoriais, avaliações e integrações com seu próprio link de indicação.

**20%** no primeiro pedido válido pago do usuário indicado e **10%** nos seguintes. Os pedidos elegíveis devem ocorrer em até **60 dias após o cadastro** do usuário indicado.

Entre na conta e complete o perfil para gerenciar links, indicações e configurações de pagamento. Identifique claramente os links de afiliado. Elegibilidade, análise e pagamento seguem o [acordo vigente](https://flaq.ai/affiliate-agreement/); não há garantia de ganhos.

## Referências e inspiração

[用GPT-6 Astra操控Blender玩3D，保姆级教程来了。](https://mp.weixin.qq.com/s/yK65CvMwzhQqu5_E5EfVVQ)

Publicado por 数字生命卡兹克; autores: 卡兹克、可达; 2026-09-08. Inspiração para o fluxo de trabalho; sem reprodução das imagens ou dos prompts longos do artigo.

[Registro de fontes do X · 2026-09-22](docs/x-playbook.md) · [JSON](docs/research/x-sources-2026-09-22.json)
