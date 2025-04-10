[app]
title = SnakeGameVN
package.name = snakegame
package.domain = org.binhnt.snake
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a
minapi = 21
sdk = 31
