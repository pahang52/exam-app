[app]
title = ExamApp
package.name = examapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,ttf,json

version = 1.0

requirements = python3,kivy,pillow

orientation = portrait
fullscreen = 1

android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

android.bootstrap = sdl2

android.permissions = INTERNET

source.include_patterns = assets/*

log_level = 2
warn_on_root = 1
