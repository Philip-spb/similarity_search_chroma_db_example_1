# Similarity Search with Chroma DB

Минимальный пример semantic similarity search на Python с использованием:

- `chromadb`
- `sentence-transformers`
- локальной коллекции товаров

Скрипт из [main.py](/Users/philip/Projects/LLM_TESTS/similarity_search_chroma_db_example_1/main.py):

- создаёт коллекцию Chroma;
- добавляет набор продуктовых описаний;
- выполняет similarity search по запросам `["red", "fresh"]`;
- печатает найденные документы и расстояния до них.

## Требования

- Python 3.12+
- `uv` для установки зависимостей и запуска проекта

## Установка

```bash
uv sync
```

## Запуск

```bash
uv run python main.py
```

## Что делает пример

После запуска приложение:

1. Инициализирует `SentenceTransformerEmbeddingFunction` с моделью `all-MiniLM-L6-v2`.
2. Создаёт коллекцию `my_grocery_collection`.
3. Добавляет в неё список текстов, например `fresh red apples`, `organic bananas`, `fresh salmon fillet`.
4. Выполняет поиск похожих документов для запросов `red` и `fresh`.
5. Выводит top-3 результата для каждого запроса.

## Пример структуры данных

В коллекцию добавляются:

- `documents`: текстовые описания товаров
- `ids`: идентификаторы в формате `food_1`, `food_2`, ...
- `metadatas`: общая метаинформация `source=grocery_store`, `category=food`

## Важные замечания

- При первом запуске `sentence-transformers` может скачать модель `all-MiniLM-L6-v2`, если её ещё нет в локальном кэше.
- Если коллекция с таким именем уже существует в текущем runtime, повторное создание может завершиться ошибкой.
- Значения `distance` в результате поиска зависят от конфигурации индекса и embedding-модели.

## Структура проекта

```text
.
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Настройка форматирования

В проекте настроены:

- `black`
- `isort`
- `ruff`
- `pre-commit`

Если используешь VS Code, настройки workspace лежат в [.vscode/settings.json](/Users/philip/Projects/LLM_TESTS/similarity_search_chroma_db_example_1/.vscode/settings.json).
