[app]
title = SnakeGameVN
package.name = snakegame
package.domain = org.binhnt.snake
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.permissions = INTERNET
android.archs = arm64-v8a,armeabi-v7a
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.private_storage = 1
