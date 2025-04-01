# 🐾 M5PaperS3 Animal Quiz Game  – M5Paper S3 (v0.3)

An educational image-based quiz game designed for children, built for the **M5Paper S3** using **MicroPython (UIFlow 2.0)**.

Touch the correct animal that matches the given name. Tracks correct and incorrect answers, and shows battery status too!
---
## 📸 Screenshot

<img src="Sources/Readme/v0.2/screen2_01.png" alt="Screenshot" width="250"/> <img src="Sources/Readme/v0.2/screen2_02.png" alt="Screenshot" width="250"/><img src="Sources/Readme/v0.2/screen2_03.png" alt="Screenshot" width="250"/>
---

## 🚧 Version

**Current Version: v0.3**

🆕 New in Version 0.3: Audio Feedback

Multisensory Learning Experience:

Immediate audio reinforcement for learning
Positive sound (C-E-G triad) rewards correct answers
Gentle negative tone guides incorrect attempts
Non-intrusive, pedagogically appropriate feedback

---

## 🖼️ Features

- Touchscreen-based animal guessing game
- Clean layout with three large animal images
- Score tracking (✅ correct / ❌ wrong)
- Battery level indicator
- Designed for vertical layout on M5Paper S3
- Fully offline — loads images from `/flash`

---

## 🧠 How it works

1. The device displays a random animal name.
2. The child touches one of the three animal images shown.
3. If correct, score increases and the game reloads.
4. If wrong, it encourages to "Try again".
5. Battery and score are always visible.

---

## 📂 File Structure

```
/flash/
├── Bear.png
├── Dog.png
├── Elephant.png
└── … (all your animal images)
m5paperS3-animal-quiz.py
```

---

## 🔧 Requirements

- M5Paper S3 with **UIFlow 2.2.4-hotfix firmware**
- MicroPython (v1.24+)
- Images preloaded in `/flash` (upload via UIFlow or Thonny)

---

## 📥 Upload Instructions

- Use **Thonny IDE** or **UIFlow 2.0 Web IDE**
- Upload your `m5paperS3-animal-quiz.py` to `/flash/`
- Upload your animal images (`*.png`) to `/flash/`
- Reboot the device and play!

---

## 🔥 Install via M5Burner

You can easily install this game using [M5Burner](https://shop.m5stack.com/pages/download).  
The `.bin` firmware file is already uploaded to the M5Burner firmware list and can be installed automatically.

1. Open **M5Burner** on your computer.  
2. Select **m5paperS3-animal-quiz** from the firmware list.  
3. Connect your **M5Paper S3** via USB.  
4. Click **Burn** to flash the firmware.  
5. Once installed, the game will launch automatically.

> 💡 No need to manually upload code or images — everything is already embedded in the firmware.

---

## 👶 Perfect For

- Montessori-style animal recognition
- Toddlers learning English vocabulary
- Interactive, offline learning activities

---


## 🚧 Future Plans & Collaboration

This project is just the beginning!
I would love to expand this animal quiz into a broader educational game, including:
	•	More animals, sounds, and animations
	•	Categories (e.g., farm animals, wild animals, sea creatures)
	•	Support for multiple languages
	•	Quizzes based on sounds or silhouettes
	•	A “learn” mode before quizzing

If you’d like to help — especially by finding or creating images, suggesting features, or testing on devices — feel free to reach out!
Contact: samuelcarre@mac.com

Contributions and ideas are always welcome 💡

---

## 📄 License

MIT License — free to use, learn, and adapt.
