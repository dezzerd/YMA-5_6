import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from app import app  # Теперь будет работать везде

def test_example():
    assert 1 + 1 == 2  # Простейший тест для проверки