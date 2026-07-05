[app]
title = Exam App
package.name = examapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,ttf

version = 1.0

orientation = portrait
fullscreen = 1

requirements = python3,kivy==2.1.0,reportlab

android.permissions = INTERNET

[buildozer]
log_level = 2

[android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a
