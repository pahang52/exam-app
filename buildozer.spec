[app]
title = Exam App
package.name = examapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,ttf,txt,ttc,otf

version = 1.0

# مهم برای جلوگیری از خطای version regex
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

orientation = portrait
fullscreen = 1

# فایل‌های مورد نیاز پروژه
requirements = python3,kivy,reportlab,python-docx,docx

# فولدر assets (فونت و عکس‌ها)
source.include_patterns = assets/*

# اجازه دسترسی‌ها (اگر لازم داشتی)
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 0

[android]

android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a
