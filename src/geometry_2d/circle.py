"""Модуль для роботи з кругами та колами (Geometry 2D)."""
import math

def area(radius: float) -> float:
    """Обчислює площу круга за радіусом."""
    if radius < 0:
        raise ValueError("Радіус не може бути від'ємним.")
    return math.pi * (radius ** 2)

def circumference(radius: float) -> float:
    """Обчислює довжину кола за радіусом."""
    if radius < 0:
        raise ValueError("Радіус не може бути від'ємним.")
    return 2 * math.pi * radius