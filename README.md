# Validador de Contraseñas

Un sistema completo de validación de contraseñas en Python con criterios de seguridad robustos y una suite exhaustiva de pruebas unitarias.

## 📋 Descripción

Este proyecto implementa un validador de contraseñas que verifica el cumplimiento de criterios de seguridad esenciales. Incluye tanto una función de validación como una interfaz interactiva de línea de comandos, complementado con un sistema completo de testing y generación automática de reportes.

## ✨ Características

### Criterios de Validación
- **Longitud mínima**: 8 caracteres
- **Diversidad de caracteres**:
  - Al menos una letra mayúscula (A-Z)
  - Al menos una letra minúscula (a-z)
  - Al menos un dígito numérico (0-9)
- **Soporte Unicode**: Compatible con caracteres especiales y emojis
- **Validación de tipos**: Manejo robusto de errores para entradas inválidas

### Sistema de Testing
- **37 pruebas unitarias** que cubren todos los escenarios
- **Pruebas parametrizadas** para eficiencia en testing
- **Casos límite (edge cases)** incluyendo Unicode y caracteres especiales
- **Generación automática de reportes** en formatos TXT y XML
- **Cobertura completa** de funcionalidad

## 🛠️ Requisitos

- **Python 3.7+**
- **pytest** (para ejecutar las pruebas)
- **pytest-cov** (para reportes de cobertura)
- **pytest-html** (para reportes HTML)

## 📦 Instalación

### 1. Clonar o descargar el proyecto
```bash
cd /ruta/al/proyecto/contraseñas
```

### 2. Crear entorno virtual (recomendado)
```bash
python3 -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate     # En Windows
```

### 3. Instalar dependencias
```bash
make install-dev
# o manualmente:
pip install -r requirements-test.txt
```

## 🚀 Uso

### Validación Interactiva
Ejecutar el validador en modo interactivo:
```bash
python validador_contraseñas.py
```

**Ejemplo de uso:**
```
$ python validador_contraseñas.py
Ingrese su contraseña: MiPassword123
La contraseña es correcta
```

### Uso Programático
```python
from validador_contraseñas import validar_contraseña

# Ejemplos de validación
print(validar_contraseña("Password123"))    # True
print(validar_contraseña("password"))       # False (sin mayúscula ni número)
print(validar_contraseña("PASSWORD123"))    # False (sin minúscula)
print(validar_contraseña("Password"))       # False (sin número)
print(validar_contraseña("Pass1"))          # False (muy corta)
```

## 🧪 Ejecutar Pruebas

### Comandos Disponibles

#### Pruebas básicas
```bash
make test                    # Ejecutar todas las pruebas
make test-verbose            # Pruebas con salida detallada
make test-basic              # Solo pruebas básicas
make test-edge               # Solo casos especiales
```

#### Reportes y cobertura
```bash
make coverage                # Pruebas con reporte de cobertura
make test-report             # Generar reportes HTML
```

#### Generación automática de reportes detallados
```bash
source venv/bin/activate
python test_validador_contraseñas.py
```

Este comando genera automáticamente:
- **Archivo TXT**: `resultados_pruebas_YYYYMMDD_HHMMSS.txt` con salida detallada
- **Archivo XML**: `junit_report_YYYYMMDD_HHMMSS.xml` para integración CI/CD

### Ejemplo de Salida de Pruebas
```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-8.4.1, pluggy-1.6.0
collecting ... collected 37 items

test_validador_contraseñas.py::TestValidadorContraseñas::test_contraseña_valida_minima PASSED
test_validador_contraseñas.py::TestValidadorContraseñas::test_contraseña_valida_compleja PASSED
...
============================== 37 passed in 0.08s ==============================
```

## 📁 Estructura del Proyecto

```
contraseñas/
├── README.md                           # Este archivo
├── CLAUDE.md                          # Instrucciones para Claude Code
├── validador_contraseñas.py           # Módulo principal de validación
├── test_validador_contraseñas.py      # Suite de pruebas unitarias
├── Makefile                           # Comandos automatizados
├── pytest.ini                        # Configuración de pytest
├── requirements-test.txt              # Dependencias de desarrollo
├── venv/                             # Entorno virtual (generado)
├── resultados_pruebas_*.txt          # Reportes de pruebas (generados)
├── junit_report_*.xml                # Reportes XML (generados)
└── htmlcov/                          # Reportes HTML de cobertura (generados)
```

## 📝 Detalles de Implementación

### Algoritmo de Validación
La función `validar_contraseña()` implementa las siguientes verificaciones:

1. **Validación de tipo**: Verifica que la entrada sea una cadena de texto
2. **Longitud**: Comprueba que tenga al menos 8 caracteres
3. **Mayúsculas**: Utiliza `any(c.isupper() for c in contraseña)`
4. **Minúsculas**: Utiliza `any(c.islower() for c in contraseña)`
5. **Números**: Utiliza `any(c.isdigit() for c in contraseña)`

### Casos de Prueba Incluidos

#### Pruebas Básicas
- Contraseñas válidas con requisitos mínimos
- Contraseñas inválidas por falta de cada criterio
- Casos límite de longitud

#### Pruebas Parametrizadas
- 16 casos de prueba diferentes
- Validación progresiva de longitud (2-8 caracteres)
- Diversos patrones de fallo

#### Casos Especiales
- Contraseñas con caracteres Unicode
- Manejo de espacios en blanco
- Caracteres de control (saltos de línea, tabulaciones)
- Emojis y caracteres especiales
- Validación de tipos incorrectos

## 🔧 Limpieza

Para limpiar archivos generados:
```bash
make clean
```

Esto elimina:
- Caché de pytest (`.pytest_cache/`)
- Archivos de cobertura (`htmlcov/`, `.coverage`)
- Caché de Python (`__pycache__/`)

## 📊 Ejemplos de Contraseñas

### ✅ Contraseñas Válidas
```python
"Password123"           # Básica válida
"MiContraseña2024"      # Con caracteres especiales
"SuperSecure99!"        # Con símbolos
"Válida123"             # Con acentos
"Test123😀"             # Con emojis
```

### ❌ Contraseñas Inválidas  
```python
"password123"           # Sin mayúsculas
"PASSWORD123"           # Sin minúsculas  
"Password"              # Sin números
"Pass1"                 # Muy corta
"12345678"              # Solo números
```

## 🤝 Contribución

Para contribuir al proyecto:

1. Ejecutar todas las pruebas: `make test`
2. Verificar cobertura: `make coverage`
3. Asegurar que todas las pruebas pasen
4. Documentar nuevas funcionalidades
5. Añadir pruebas para código nuevo

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo los términos que el usuario considere apropiados.

## 🔍 Notas Técnicas

- **Compatibilidad**: Python 3.7+
- **Codificación**: UTF-8 para soporte completo de Unicode
- **Testing**: Basado en pytest con reportes automáticos
- **CI/CD**: Reportes XML compatibles con sistemas de integración continua
- **Documentación**: Docstrings detallados siguiendo convenciones PEP 257

---

**Versión**: 1.0  
**Autor**: Sistema de Validación de Contraseñas  
**Última actualización**: 2025-06-19