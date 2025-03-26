def progress_bar(done: int, undone: int, length = 25):
    """
    Отображает progress bar в консоли.

    Args:
        done: Количество выполненных задач.
        undone: Общее количество задач.
        length: Длина progressbar'a в символах.
    """
    if undone == 0:
        sharps = length
        percentage = 100
    else:
        sharps = int(round(done/undone, 2)*float(length))
        percentage = int((done/undone)*100)
    print(f'\r|{"#"*sharps}{"-"*(length-sharps)}| [{percentage}%] [{done}/{undone}]', end="")