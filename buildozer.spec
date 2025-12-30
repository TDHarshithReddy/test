[app]

# Application title
title = Dental Practice Manager

# Package name
package.name = dentalapp

# Package domain (needed for android/ios packaging)
package.domain = com.dental

# Source code directory
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,atlas,json

# Application version
version = 1.0.0

# Application requirements
requirements = python3,kivy==2.3.0

# Supported orientations
orientation = portrait

# Enable fullscreen
fullscreen = 0

# Presplash background color
presplash.color = #FFFFFF

# Icon for the application
#icon.filename = %(source.dir)s/data/icon.png

# Presplash image
#presplash.filename = %(source.dir)s/data/presplash.png

# Android specific
[app:android]

# Permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android API to use
android.api = 31

# Minimum API required
android.minapi = 21

# Android SDK version
android.sdk = 31

# Android NDK version
android.ndk = 25b

# Android architecture
android.archs = arm64-v8a,armeabi-v7a

# Allow backup
android.allow_backup = True

[buildozer]

# Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# Display warning if buildozer is run as root
warn_on_root = 1
