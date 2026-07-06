[app]

title = Exam Designer Pro

package.name = examdesigner
package.domain = ir.nikzad

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,ttf,db

version = 1.0

requirements = python3,kivy,reportlab,pillow

orientation = portrait

fullscreen = 0

icon.filename = assets/icon.png
presplash.filename = assets/splash.png

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a

android.accept_sdk_license = True

android.allow_backup = True

android.logcat_filters = *:S python:D

log_level = 2

warn_on_root = 0


[buildozer]

log_level = 2
