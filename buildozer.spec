[app]
title = Exam Designer
package.name = examdesigner
package.domain = org.nikzad

source.dir = .
source.include_exts = py,png,jpg,kv,ttf

version = 1.0

requirements = python3,kivy,reportlab,python-docx

orientation = portrait

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 0
