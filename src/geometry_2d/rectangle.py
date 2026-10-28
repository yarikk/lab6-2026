"""Модуль для роботи з прямокутниками (Geometry 2D)."""

def area(width: float, height: float) -> float:
    """Обчислює площу прямокутника за шириною та висотою."""
    if width < 0 or height < 0:
        raise ValueError("Сторони прямокутника не можуть бути від'ємними.")
    return width * height

def perimeter(width: float, height: float) -> float:
    """Обчислює периметр прямокутника за шириною та висотою."""
    if width < 0 or height < 0:
        raise ValueError("Сторони прямокутника не можуть бути від'ємними.")
    return 2 * (width + height)