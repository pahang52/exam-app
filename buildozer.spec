[app]
title = Exam App
package.name = examapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,ttf,txt

version = 1.0

orientation = portrait
fullscreen = 1

requirements = python3,kivy,reportlab,python-docx

android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 0

[android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a
