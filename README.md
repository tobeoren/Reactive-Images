---

### 1. **Introduction**
This is a Python-based sound detection app that listens to audio input from a selected microphone. It processes the audio in real time to detect whether there is sound (based on a set threshold) and updates this status on a web interface. The app uses libraries like `numpy` for processing, `pyaudio` for capturing sound, and `Flask` to serve a web page that displays the sound detection status.

---

### 2. **Features**
- **Microphone Selection**: The app lists all available audio input devices and allows the user to select a preferred microphone.
- **Real-Time Sound Detection**: The app continuously detects whether there is sound based on the threshold you set (adjustable).
- **Web Interface**: The sound status (whether sound is detected or not) is shown on a simple webpage using Flask.
- **Multi-threading**: The sound detection runs in a separate thread, so the web interface remains responsive.

---

### 3. **Getting Started**
**Step 1**: Install the required libraries. Run the following commands in your terminal to install the dependencies:
```bash
pip install numpy pyaudio flask
```

**Step 2**: Run the script. After starting the program, you will be prompted to choose an audio input device. The device list will appear in the terminal, and you can select the microphone by entering the corresponding number.

**Step 3**: Open a web browser. Once the app is running, open your browser and go to `http://127.0.0.1:5000/`. The page will display whether sound is being detected or not.

**Step 4**: Adjust the sensitivity if needed. The variable `THRESHOLD` defines how sensitive the sound detection is. You can increase or decrease this value depending on your needs.

---
