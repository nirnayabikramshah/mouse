# 🖱️ Hand Mouse — Control Your Cursor with Gestures

> Control your computer mouse using just your hand and a webcam — no hardware required.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10%2B-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

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
git clone https://github.com/your-username/hand-mouse.git
cd hand-mouse
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

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- [Google MediaPipe](https://github.com/google/mediapipe) for the hand tracking model
- [PyAutoGUI](https://github.com/asweigart/pyautogui) for cross-platform mouse control
