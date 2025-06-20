# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python password validation utility that validates passwords against security criteria (minimum 8 characters, uppercase, lowercase, and numeric characters). The project includes both a command-line interface and a comprehensive test suite.

## Architecture

- `validador_contraseñas.py`: Core module containing the `validar_contraseña()` function and CLI interface
- `test_validador_contraseñas.py`: Comprehensive test suite with 25+ test cases including edge cases, parametrized tests, and error handling
- Testing infrastructure configured with pytest, coverage reporting, and automated commands via Makefile

## Common Commands

### Setup
```bash
make install-dev          # Install testing dependencies
```

### Testing
```bash
make test                 # Run all tests
make test-verbose         # Run tests with verbose output
make coverage             # Run tests with coverage report
make test-basic           # Run basic validation tests only
make test-edge            # Run edge case tests only
make test-report          # Generate HTML coverage and test reports
```

### Running the Application
```bash
python validador_contraseñas.py    # Interactive password validation
```

### Cleanup
```bash
make clean               # Remove generated test files and cache
```

## Test Structure

The test suite is organized into two main classes:
- `TestValidadorContraseñas`: Core functionality tests including parametrized test cases
- `TestCasosEspeciales`: Edge cases and special character handling

Tests cover positive/negative cases, boundary conditions, type validation, and Unicode support.