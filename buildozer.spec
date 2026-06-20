[app]

# (str) Título de la aplicación
title = PRO Predictor

# (str) Nombre del paquete (solo minúsculas y números)
package.name = propredictor

# (str) Dominio del paquete (formato inverso)
package.domain = com.propredictor

# (str) Versión
version = 1.0

# (str) Descripción
description = App de predicción para trading con IA

# (str) Autor
author = Predictor Pro

# (list) Dependencias de Python
requirements = python3,kivy,requests,plyer

# (str) Archivo principal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf,txt

# (list) Permisos de Android
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (bool) Pantalla completa
fullscreen = 0

# (str) Orientación
orientation = portrait

# (bool) Mostrar log de Android
android.logcat_filters = *:S python:D

# (int) API mínima de Android
android.minapi = 21

# (int) API objetivo de Android
android.targetapi = 33

# (bool) Usar AndroidX
android.use_androidx = True

# (str) Versión de build-tools
android.build_tools = 33.0.2

[buildozer]

# (int) Nivel de log
log_level = 2

# (bool) Forzar compilación
warn_on_root = 1

# (bool) Usar caché
cache = True
