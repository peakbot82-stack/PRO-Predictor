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

# (str) Correo del autor
author.email = predictor@email.com

# (str) URL de la app
# author.url = https://propredictor.com

# (list) Dependencias de Python
requirements = python3,kivy,requests,plyer

# (str) Archivo principal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf,txt

# (list) Archivos a excluir
# source.exclude_exts = spec,log

# (list) Permisos de Android
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (bool) Pantalla completa
fullscreen = 0

# (str) Orientación (portrait, landscape, sensor, user)
orientation = portrait

# (bool) Mostrar u ocultar el log de Android (debug)
android.logcat_filters = *:S python:D

# (str) Icono de la aplicación (opcional)
# icon.filename = %(source.dir)s/data/icon.png

# (str) Splash screen (pantalla de carga)
# presplash.filename = %(source.dir)s/data/presplash.png

# (int) API mínima de Android
android.minapi = 21

# (int) API objetivo de Android
android.targetapi = 33

# (list) Bibliotecas adicionales
# android.add_libs_armeabi_v7a =

# (list) Archivos de recursos adicionales
# android.add_src =

# (str) Gradle dependencies
# android.gradle_dependencies =

# (bool) Usar AndroidX
android.use_androidx = True

# (bool) Usar SDK de Android
android.sdk = 33

# (str) Carpeta de salida
# android.arch = armeabi-v7a

# (list) Aplicaciones de servicios
# android.services =

# (bool) Habilitar Windows
# windows = False

# (bool) Habilitar iOS
# ios = False

# (bool) Habilitar macOS
# osx = False

[buildozer]

# (int) Nivel de log (0-3)
log_level = 2

# (bool) Forzar compilación (limpiar caché)
warn_on_root = 1

# (bool) Usar caché de compilación
cache = True

# (str) Carpeta de caché
# cache_dir = .buildozer_cache
