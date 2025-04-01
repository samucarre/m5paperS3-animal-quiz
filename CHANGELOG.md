# 📘 Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/).

---
## [0.3.0] - 2025-04-01

### ✨ Added
Audio Feedback System:
Positive ascending chime (C-E-G) for correct answers
Negative descending tone (G-E-C) for incorrect answers
Integrated passive buzzer control (GPIO21)
New audio configuration section in documentation

### 🛠 Improved
Optimized response time with shorter sound durations (0.15-0.3s per tone)
Better touch interaction feedback loop
Power management during audio playback

### 🐛 Fixed
Resolved PWM frequency limitations (50-5000Hz range)
Fixed audio initialization sequence
Synchronized audio with UI updates

### 📌 Notes
Audio uses musical notes (C4=262Hz, E4=330Hz, G4=392Hz)
Volume set to 50% duty cycle (512/1023) for clear but comfortable feedback
Sounds automatically mute during shutdown sequence

## [0.2.0] - 2025-03-28
### ✨ Added
- Splash screen shown at startup (image located in `/flash/splash.png`)
- "OFF" button to exit the game and display a shutdown message

### 🛠 Changed
- Repositioned UI elements to make room for the new "OFF" button
- Improved overall user flow from splash to gameplay

### 📌 Notes
- The "OFF" button does not power off the device, but shows a farewell message and halts the game loop.