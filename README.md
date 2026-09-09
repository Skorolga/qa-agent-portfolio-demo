# QA Automation & AI-assisted Test Design — Portfolio Demo

Демонстрационный проект, показывающий подход к архитектуре QA automation и AI-assisted test design.

## Что показано

- pytest fixtures;
- API client abstraction;
- простой Page Object;
- risk-based отбор сценариев;
- pipeline обработки release notes;
- human-in-the-loop;
- классификация падений;
- CI-конфигурация;
- unit-тесты для ключевой логики.

## Что намеренно не включено

Это не production-решение и не готовый AI-агент.

Отсутствуют:
- реальные LLM API вызовы;
- production prompts;
- секреты;
- интеграции с Jira/GitLab/внутренними системами;
- реальные данные;
- production-логика генерации автотестов.

AI-слой представлен интерфейсом и детерминированной demo-реализацией.

## Архитектура

release notes
→ change analyzer
→ test plan generator
→ human review
→ automation candidate selector
→ test execution
→ failure classifier
→ QA summary

## Запуск

```bash
python -m venv .venv
pip install -r requirements.txt
pip install -e .
pytest
```

Smoke:
```bash
pytest -m smoke
```

## Почему API раньше UI

API-тесты обычно быстрее, стабильнее и дешевле в поддержке. UI оставляется для критичных пользовательских сценариев.

## Почему human-in-the-loop

Сгенерированный тест-план — черновик. Перед автоматизацией QA подтверждает корректность сценария, ожидаемый результат и бизнес-ценность.

## Почему AI вынесен за интерфейс

Чтобы pipeline не зависел от конкретной модели или провайдера. Реальную интеграцию можно заменить, не переписывая основную логику.
