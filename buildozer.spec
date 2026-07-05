[app]
title = Exam Designer
package.name = examdesigner
package.domain = org.nikzad

source.dir = .
source.include_exts = py,png,jpg,ttf

version = 1.0.0

requirements = python3,kivy==2.2.1,reportlab,python-docx

orientation = portrait

# مهم: این 3 خط باید اصلاح بشه
android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 0
