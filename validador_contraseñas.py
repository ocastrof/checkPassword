#!/usr/bin/env python3
"""
Validador de Contraseñas - Módulo Principal
==========================================

Este módulo proporciona funcionalidad para validar contraseñas según criterios de seguridad
específicos. Incluye tanto la función de validación como una interfaz de línea de comandos
para uso interactivo.

Autor: Sistema de Validación de Contraseñas
Versión: 1.0
"""

def validar_contraseña(contraseña):
    """
    Valida que una contraseña cumpla con los siguientes criterios:
    - Mínimo 8 caracteres
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un número
    
    Args:
        contraseña (str): La contraseña a validar
        
    Returns:
        bool: True si la contraseña es válida, False en caso contrario
        
    Raises:
        TypeError: Si contraseña no es una cadena de texto
    """
    # Verificación de tipo: Asegurar que el parámetro sea una cadena de texto
    # Esto previene errores al intentar aplicar métodos de string a otros tipos
    if not isinstance(contraseña, str):
        raise TypeError("La contraseña debe ser una cadena de texto")
    
    # Criterio 1: Verificar longitud mínima de 8 caracteres
    # Las contraseñas cortas son más vulnerables a ataques de fuerza bruta
    if len(contraseña) < 8:
        return False
    
    # Criterio 2: Verificar presencia de al menos una letra mayúscula
    # any() devuelve True si al menos un elemento de la secuencia es True
    # c.isupper() verifica si el carácter 'c' es una letra mayúscula
    tiene_mayuscula = any(c.isupper() for c in contraseña)
    
    # Criterio 3: Verificar presencia de al menos una letra minúscula
    # c.islower() verifica si el carácter 'c' es una letra minúscula
    tiene_minuscula = any(c.islower() for c in contraseña)
    
    # Criterio 4: Verificar presencia de al menos un dígito numérico
    # c.isdigit() verifica si el carácter 'c' es un dígito (0-9)
    tiene_numero = any(c.isdigit() for c in contraseña)
    
    # Devolver True solo si todos los criterios se cumplen
    # Usar AND lógico para garantizar que TODOS los requisitos estén presentes
    return tiene_mayuscula and tiene_minuscula and tiene_numero


# Bloque de ejecución principal
# Este código solo se ejecuta cuando el archivo se ejecuta directamente,
# no cuando se importa como módulo
if __name__ == "__main__":
    # Solicitar contraseña al usuario de forma interactiva
    # input() muestra el mensaje y espera la entrada del usuario
    contraseña = input("Ingrese su contraseña: ")
    
    # Llamar a la función de validación y actuar según el resultado
    # La función devuelve True si la contraseña cumple todos los criterios
    if validar_contraseña(contraseña):
        print("La contraseña es correcta")
    else:
        print("La contraseña no es correcta")