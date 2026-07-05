[app]
title = Exam Designer
package.name = examdesigner
package.domain = org.nikzad

source.dir = .
source.include_exts = py,ttf,png

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

android.assets = assets/

[buildozer]

log_level = 2
warn_on_root = 1
