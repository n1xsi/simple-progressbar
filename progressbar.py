def progress_bar(done: int, undone: int, length: int = 50) -> None:
    """
    Отображает progressbar в консоли.

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
