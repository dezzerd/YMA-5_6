import sys
from pathlib import Path

# Добавляем корень проекта в пути Python
sys.path.append(str(Path(__file__).parent.parent))

from app import app  # Теперь импорт будет работать

def test_example():
    assert 1 + 1 == 2