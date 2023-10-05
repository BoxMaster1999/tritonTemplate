## Структура директорий для репозитория моделей triton

Для каждой модели, которая использует `python backend` необходимы следующие вложенности:

```
models
|   # folder with defenition of model instance
|-- model_a
    |   # model version folders
    |-- 1
    |   |-- model.py
    `-- config.pbtxt
```
``config.pbtxt`` - конфиг модели с форматом входа, выхода и параметров инференса

``model.py`` - питоновский интерфейс с обязательным методом ``execute``
