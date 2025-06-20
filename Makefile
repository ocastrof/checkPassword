.PHONY: test test-verbose coverage clean install-dev

# Instalar dependencias de desarrollo
install-dev:
	pip install -r requirements-test.txt

# Ejecutar todas las pruebas
test:
	pytest

# Ejecutar pruebas con salida verbose
test-verbose:
	pytest -v

# Ejecutar pruebas con coverage
coverage:
	pytest --cov=validador_contraseñas --cov-report=html --cov-report=term-missing

# Ejecutar pruebas específicas
test-basic:
	pytest test_validador_contraseñas.py::TestValidadorContraseñas -v

test-edge:
	pytest test_validador_contraseñas.py::TestCasosEspeciales -v

# Limpiar archivos generados
clean:
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf __pycache__/
	rm -f .coverage

# Ejecutar pruebas y generar reporte HTML
test-report:
	pytest --cov=validador_contraseñas --cov-report=html --html=report.html --self-contained-html