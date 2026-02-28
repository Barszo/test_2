import pytest
import sys
import os

# Dodaj parent directory do sys.path aby zaimportować app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_import():
    """Test czy można zaimportować moduł app"""
    try:
        import app
        assert True
    except ImportError:
        assert False, "Nie można zaimportować modułu app"

def test_basic_math():
    """Prosty test matematyczny"""
    assert 1 + 1 == 2
    assert 2 * 2 == 4

def test_string_operations():
    """Test operacji na stringach"""
    test_string = "hello world"
    assert test_string.upper() == "HELLO WORLD"
    assert len(test_string) == 11

# Jeśli chcesz testować Flask app bez bazy danych:
def test_flask_app_exists():
    """Test czy aplikacja Flask istnieje"""
    try:
        from app import app as flask_app
        assert flask_app is not None
    except ImportError:
        pytest.skip("Nie można zaimportować Flask app bez zmiennych środowiskowych")
