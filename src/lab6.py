"""
Основна програма для Лабораторної роботи № 6.

Цей скрипт повинен імпортувати та використовувати створений вами пакет,
щонайменше один модуль зі стандартної бібліотеки Python,
та щонайменше один сторонній пакет.
"""

import datetime  # Модуль зі стандартної бібліотеки для роботи з датою/часом
import math      # Модуль зі стандартної бібліотеки для математичних операцій
from colorama import init, Fore  # Сторонній пакет для кольорового виводу

# Імпортуємо модулі та функції зі створеного пакета geometry_2d
from geometry_2d import rectangle, circle

# Ініціалізація colorama для коректного виведення кольорів в терміналі
init(autoreset=True)


def main():
    """Основна функція для демонстрації використання модулів та пакетів."""
    print(Fore.CYAN + "=== Лабораторна робота №6: Пакет geometry_2d ===")
    print(f"Час виконання: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Використання модуля стандартної бібліотеки math
    print(f"Квадратний корінь з 16 (math.sqrt): {math.sqrt(16)}")

    # Використання функцій з власного пакета geometry_2d (модуль rectangle)
    width, height = 5.0, 3.0
    rect_area = rectangle.area(width, height)
    rect_perim = rectangle.perimeter(width, height)
    
    print(Fore.YELLOW + f"--- Прямокутник (ширина: {width}, висота: {height}) ---")
    print(f"  - Площа: {rect_area}")
    print(f"  - Периметр: {rect_perim}")

    # Використання функцій з власного пакета geometry_2d (модуль circle)
    radius = 4.0
    circ_area = circle.area(radius)
    circ_len = circle.circumference(radius)
    
    print(Fore.MAGENTA + f"\n--- Круг / Коло (радіус: {radius}) ---")
    print(f"  - Площа круга: {circ_area:.2f}")
    print(f"  - Довжина кола: {circ_len:.2f}")


if __name__ == "__main__":
    main()