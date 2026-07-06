[app]
title = ExamApp
package.name = examapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,ttf,json

version = 1.0

# 🔥 خیلی مهم: فقط همین
# version.regex حذف شده

requirements = python3,kivy==2.2.1,pillow,reportlab

orientation = portrait
fullscreen = 1

# اندروید
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# مهم برای جلوگیری از error های buildozer
android.bootstrap = sdl2

# دسترسی‌ها
android.permissions = INTERNET

# assets
source.include_patterns = assets/*

log_level = 2
warn_on_root = 1
