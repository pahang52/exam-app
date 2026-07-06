[app]
title = Exam Designer Pro
package.name = examdesigner
package.domain = org.nikzad

source.dir = .
source.include_exts = py,png,jpg,kv,ttf,json

version = 1.0

requirements = python3,kivy,pillow,fpdf

orientation = portrait

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

fullscreen = 1
log_level = 2
