[app]

title = Exam Designer Pro

package.name = examdesigner
package.domain = ir.nikzad

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,json,txt,ttf,db

version = 1.0

requirements = python3,kivy==2.3.1,kivymd,pillow,python-bidi,arabic-reshaper,fpdf2

orientation = portrait
fullscreen = 0

icon.filename = assets/icon.png
presplash.filename = assets/splash.png

android.permissions = INTERNET

android.api = 33
android.minapi = 21

android.archs = arm64-v8a

android.accept_sdk_license = True

log_level = 2

warn_on_root = 0

[buildozer]

log_level = 2
