# The Simpliest Python progressbar

![image](https://i.imgur.com/XDHrkGN.png)

Небольшая Python-функция для создания текстовых индикаторов прогресса в _терминальных_ приложениях.

## Достоинства:
- Очень простой в использовании и модернизации
- Не обновляет весь экран, избегая "мерцания"
- Минималистичный

## Пример использования

```python
from progressbar import progress_bar
from time import sleep

i, count = 0, 35
for _ in range(count):
    progress_bar(i, count)
    sleep(0.2)
    i += 1
progress_bar(i, count) # Для показа 100%-тного заполнения
```

## Демонстрация работы
![gif](https://i.imgur.com/H2Luj6E.gif)
