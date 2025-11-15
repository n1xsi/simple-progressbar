<h1 align="center">
  <img src="https://i.imgur.com/XDHrkGN.png" align="top" alt="Logo">
</h1>

<h1 align="center">

The Simpliest Python progress bar

[![Python](https://custom-icon-badges.demolab.com/badge/3.7+-696969?logo=pythonn&label=Python&labelColor=100d11&style=for-the-badge)](https://www.python.org/downloads/release/python-370/)
[![GitHub](https://img.shields.io/badge/repo-696969?style=for-the-badge&logo=github&labelColor=100d11&label=github)](https://github.com/n1xsi/simple-progressbar/)
[![Tether](https://img.shields.io/badge/me-696969?style=for-the-badge&logo=tether&logoColor=168363&labelColor=100d11&label=tether)](https://link.trustwallet.com/send?coin=20000714&address=0x1fCb6a37Fbf9267CE33eBC9A698577fc97A532D9&token_id=0x55d398326f99059fF775485246999027B3197955)

</h1>

Небольшая Python-функция для создания текстовых индикаторов прогресса в _терминальных_ приложениях (CLI).

## ✨ Достоинства:
- Очень прост в использовании и модернизации
- Не обновляет *весь* экран (**избегает** "мерцания")
- Минималистичный

## 👉 Пример использования

```python
from progressbar import progress_bar
from time import sleep

i, count = 0, 35        # Какие-то данные
for _ in range(count):
    progress_bar(i, count)
    sleep(0.2)          # Для имитации задержки в работе
    i += 1
progress_bar(i, count)  # Для показа 100%-тного заполнения
```

## 🎬 Демонстрация работы
![gif](https://i.imgur.com/H2Luj6E.gif)
