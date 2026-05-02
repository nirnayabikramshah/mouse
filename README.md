# 🖱️ mouse — Control Your Cursor with Gestures

> Control your computer mouse using just your hand and a webcam — no hardware required.  
> **By [nirnayabikramshah](https://github.com/nirnayabikramshah)**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10%2B-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Author](https://img.shields.io/badge/Author-nirnayabikramshah-purple)

---

## ✨ How It Works

This project uses your webcam and Google's **MediaPipe** hand-tracking library to detect the position of your fingers in real time. It maps your **index fingertip** to your screen cursor and triggers a **mouse click** when you pinch your index finger and thumb together.

| Gesture | Action |
|---|---|
| ☝️ Move index finger | Move the cursor |
| 🤏 Pinch index + thumb | Left click |
| `Q` key | Quit the program |

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/nirnayabikramshah/mouse.git
cd mouse
```

### 2. Install dependencies
```bash
pip install opencv-python mediapipe pyautogui
```

> **Note for macOS users:** You may need to grant Terminal/your IDE permission to access the camera and control the mouse under *System Preferences → Privacy & Security*.

> **Note for Linux users:** You may need to install `python3-tk` and `python3-dev` for pyautogui:
> ```bash
> sudo apt-get install python3-tk python3-dev
> ```

---

## 🚀 Usage

```bash
python hand_mouse.py
```

- Hold your hand in front of the camera.
- Move your **index finger** to move the cursor.
- **Pinch** your index finger and thumb together to click.
- Press **`Q`** to exit.

---

## ⚙️ Configuration

You can tweak these constants at the top of `hand_mouse.py`:

| Constant | Default | Description |
|---|---|---|
| `SMOOTH` | `5` | Mouse smoothing factor. Higher = smoother but more lag. Try `3`–`7`. |
| `CLICK_COOLDOWN` | `0.5` | Minimum seconds between clicks. Prevents accidental double-clicks. |
| `min_detection_confidence` | `0.7` | How confident MediaPipe must be before detecting a hand (0–1). |
| `min_tracking_confidence` | `0.7` | Tracking confidence threshold once a hand is detected (0–1). |

---

## 📦 Dependencies

| Library | Purpose |
|---|---|
| [OpenCV](https://opencv.org/) | Webcam capture and drawing landmarks on screen |
| [MediaPipe](https://mediapipe.dev/) | Real-time hand landmark detection (21 points) |
| [PyAutoGUI](https://pyautogui.readthedocs.io/) | Moving the mouse cursor and triggering clicks |

---

## 🗺️ Hand Landmarks Used

MediaPipe tracks **21 landmarks** on each hand. This project uses:

- **Landmark 8** — Index fingertip → cursor position
- **Landmark 4** — Thumb tip → click detection (pinch distance)

```
        8
        |
    7   |
    |   6
    5   |
     \  4 ← Thumb tip
      \ |
       \|
        0
```

---

## 🐛 Known Issues & Tips

- **Jittery cursor?** Increase the `SMOOTH` value (e.g. `7` or `10`).
- **Clicks firing too often?** Increase `CLICK_COOLDOWN` to `0.8` or `1.0`.
- **Hand not detected?** Make sure your hand is well-lit and fully visible in the frame.
- **Cursor stuck at screen edge?** This is handled — `FAILSAFE` is disabled.
- **Slow performance?** Lower the camera resolution or reduce `max_num_hands`.

---

## 🔭 Possible Improvements

- [ ] Right-click support (e.g. two-finger pinch)
- [ ] Scroll gesture (e.g. two fingers up/down)
- [ ] Double-click support
- [ ] On-screen gesture guide overlay
- [ ] Configurable gesture sensitivity via a config file

---



---

## 🎓 Inspiration & Learning Resources

This project was inspired by the wave of AI-powered Python projects and tutorials in the computer vision community. If you want to go deeper, these are great places to start:

### 📺 YouTube Channels
| Channel | What You'll Learn |
|---|---|
| [Murtaza's Workshop](https://www.youtube.com/@murtazasworkshop) | MediaPipe hand tracking, face detection, CV projects |
| [Nicholas Renotte](https://www.youtube.com/@nicholasrenotte) | End-to-end AI/ML Python projects |
| [Tech With Tim](https://www.youtube.com/@TechWithTim) | Python automation, OpenCV tutorials |
| [Sentdex](https://www.youtube.com/@sentdex) | Computer vision, deep learning with Python |
| [1littlecoder](https://www.youtube.com/@1littlecoder) | Quick AI project demos and experiments |

### 🤖 Similar AI-Powered Python Projects to Explore
- **Face Mesh** — Map 468 landmarks on a face in real time using MediaPipe
- **Pose Estimation** — Detect full body keypoints for fitness/game control
- **Eye Blink Detector** — Trigger actions with blinks using facial landmarks
- **Gesture Volume Control** — Control system volume with pinch distance
- **AI Virtual Painter** — Draw on screen by moving your finger in the air
- **Object Detection Mouse** — Move cursor by tracking a physical object with YOLO

### 📚 Useful Docs & References
- [MediaPipe Hand Landmark Docs](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)
- [OpenCV Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [PyAutoGUI Docs](https://pyautogui.readthedocs.io/en/latest/)

---

## 🙏 Acknowledgements

- [Google MediaPipe](https://github.com/google/mediapipe) for the hand tracking model
- [PyAutoGUI](https://github.com/asweigart/pyautogui) for cross-platform mouse control
- Built by [nirnayabikramshah](https://github.com/nirnayabikramshah)
