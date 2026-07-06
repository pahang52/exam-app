[app]
title = ExamApp
package.name = examapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,ttf,otf,txt,json

version = 1.0

# ❌ مهم: این خط باید وجود نداشته باشد
# version.regex =

requirements = python3,kivy,reportlab,python-docx

orientation = portrait
fullscreen = 1

android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

# فونت‌ها / assets
source.include_patterns = assets/*

# اگر از webview یا permission استفاده کردی:
android.permissions = INTERNET

# build settings
log_level = 2
warn_on_root = 1
