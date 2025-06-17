import sys
import os
# Добавляем корень проекта в пути поиска модулей
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app  # Теперь импорт должен работать

def test_example():
    assert 1 + 1 == 2  # Простейший тест для проверки