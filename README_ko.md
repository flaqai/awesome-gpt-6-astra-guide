# GPT-6 Astra 실전 가이드

**[flaq.ai](https://flaq.ai/) 팀이 정리한 최신 GPT-6 Astra 가이드**입니다. 모델 소개, 시작 방법, 실행 가능한 코드, 제작 워크플로와 실제 스크린샷을 제공합니다.

<!-- languages:start -->
[English](README.md) · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · [日本語](README_ja.md) · **한국어** · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

최종 확인: 2026-09-08. OpenAI 공식 문서가 아닌 독립적인 팀 가이드입니다. README는 12개 언어를 지원하며, 상세 튜토리얼과 예제 진단 메시지는 현재 중국어 간체로 제공됩니다.

[시작 안내](docs/quickstart.md) · [사례 12개](docs/cases.md) · [워크플로 6개](docs/workflows.md) · [코드 예제](examples/README.md)

## Astra 소개

Astra는 복잡한 추론, 코딩, 조사와 여러 단계의 작업을 위한 OpenAI 모델입니다. 텍스트와 이미지를 입력받고 텍스트를 출력합니다. 브라우저 조작, 프로그램 실행, 영상 제작에는 실행 환경의 별도 도구가 필요합니다.

| 모델 | `gpt-6-astra` |
| --- | --- |
| 컨텍스트 | 1,050,000 tokens |
| 최대 출력 | 128,000 tokens |
| 추론 강도 | `low` · `medium` · `high` · `xhigh` · `max` |

[공식 모델 문서](https://developers.openai.com/api/docs/models/gpt-6-astra) · [설정과 고급 기능](https://developers.openai.com/api/docs/guides/latest-model)

## 코드 없이 시작하기

이용 권한이 있는 제품에서 Astra를 선택하고 자료와 작은 목표를 전달하세요. 다음 요청으로 시작할 수 있습니다.

```text
카페의 이틀짜리 행사를 계획해 주세요. 예산은 2,000위안, 직원은 두 명입니다. 행사 규칙, 일정, 항목별 예산, 홍보 문구 세 개를 작성하고 합계와 가정을 확인해 주세요.
```

## 첫 예제 실행하기

Python 3.10+ 또는 Node.js 20+를 사용하고 저장소 루트에서 실행하세요. 포함된 스크립트는 기본 라이브러리만 사용하므로 패키지 설치가 필요하지 않습니다. 먼저 요청을 무료로 미리 봅니다.

```bash
python3 examples/astra.py text --dry-run
node examples/quickstart.mjs --dry-run
```

실제 호출 전에는 Astra 권한이 있는 OpenAI 프로젝트 키를 현재 터미널의 `OPENAI_API_KEY`에 설정하세요. [설정 안내](docs/quickstart.md#用-api-开始)를 참고하고 키를 코드나 스크린샷에 넣지 마세요. `--dry-run`은 통신하지 않으며 실제 요청은 유료입니다. 예제는 OpenAI API를 직접 호출합니다. Flaq.ai의 모델 제공 여부는 별도로 확인해야 합니다.

```bash
python3 examples/astra.py text --prompt '카페의 이틀짜리 행사를 계획해 주세요. 예산은 2,000위안, 직원은 두 명입니다. 행사 규칙, 일정, 항목별 예산, 홍보 문구 세 개를 작성하고 합계와 가정을 확인해 주세요.'
python3 examples/astra.py vision --image assets/screenshots/iphone-archive.png
python3 examples/astra.py research
python3 examples/astra.py extract
node examples/quickstart.mjs
```

[코드 예제](examples/README.md) · [Python](examples/astra.py) · [JavaScript](examples/quickstart.mjs)

## 작품과 실제 스크린샷

아래 이미지는 실제 브라우저에서 촬영했습니다. 작품의 권리는 원작자에게 있으며 제작 프로젝트 전체를 재현한 것은 아닙니다.

![Tom Krcha의 증기 기관차: 원작자 미리보기가 표시된 페이지.](assets/screenshots/steam-train-reference.png)

Tom Krcha의 증기 기관차: 원작자 미리보기가 표시된 페이지. [원본 게시물](https://x.com/tomkrcha/status/2095756085890310311)

![bluedev의 iPhone Archive: 실제로 연 공개 사이트.](assets/screenshots/iphone-archive.png)

bluedev의 iPhone Archive: 실제로 연 공개 사이트. [원본 게시물](https://x.com/blueemi99/status/2096917792737911131) · [온라인 작품](https://iphone-archive.vercel.app/)

![synabreu의 Seoul 3D Atlas: City와 Sunset 전환 확인.](assets/screenshots/seoul-atlas.png)

synabreu의 Seoul 3D Atlas: City와 Sunset 전환 확인. [원본 게시물](https://x.com/synabreu/status/2096557555086725159) · [온라인 작품](https://seoul-3d-atlas.synabreu.chatgpt.site/)

[스크린샷 출처](assets/screenshots/README.md) · [사례 12개](docs/cases.md)

## 실전 워크플로

가장 작은 작동 버전부터 만들고 실제 화면과 오류를 바탕으로 개선하세요. 편집 가능한 파일, 실행 방법, 실제 스크린샷을 결과물에 포함하도록 요청하세요.

[워크플로 6개](docs/workflows.md)

## 검증과 기여

오프라인 테스트 17개를 통과했습니다. 유료 API 호출과 전체 커뮤니티 작품의 재현 검증은 하지 않았습니다. [검증 기록](docs/verification.md) · [출처](docs/sources.md) · [기여 안내](CONTRIBUTING.md). 자체 문서와 코드는 [MIT](LICENSE)를 따르며 타사 자료에는 각각의 권리가 적용됩니다.

## flaq.ai 소개

[flaq.ai](https://flaq.ai/)는 AI 에이전트와 운영 애플리케이션을 위한 이미지, 영상, 음악, 언어 모델 통합 API를 제공합니다. 팀은 이 가이드를 통해 실용적인 AI 활용 방법을 공유합니다. 오픈 소스 워크플로: [Backlink Skills](https://github.com/flaqai/backlink_skills).

## 제휴 마케팅 및 파트너 지원

크리에이터, 개발자, 교육자는 [Flaq.ai 제휴 프로그램](https://flaq.ai/affiliate-program/)에 참여해 자신의 추천 링크로 튜토리얼, 리뷰, 통합 가이드를 공유할 수 있습니다.

추천 사용자의 첫 유효 유료 주문은 **20%**, 이후 유효 유료 주문은 **10%**입니다. 주문 인정 기간은 추천 사용자가 가입한 후 **60일**입니다.

로그인 후 제휴 프로필을 작성하면 링크, 추천 내역, 지급 설정을 관리할 수 있습니다. 공유 시 제휴 관계를 명확히 밝히세요. 자격, 심사, 지급은 현행 [제휴 약관](https://flaq.ai/affiliate-agreement/)을 따르며 수익을 보장하지 않습니다.
