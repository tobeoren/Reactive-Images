import numpy as np
import pyaudio
from flask import Flask, render_template, jsonify
import threading

app = Flask(__name__)
CHUNK = 1024
RATE = 44100
THRESHOLD = 1000  # Sensitivitas suara

# Inisialisasi PyAudio
p = pyaudio.PyAudio()

# Daftar perangkat input audio
def list_audio_devices():
    info = p.get_host_api_info_by_index(0)
    num_devices = info.get('deviceCount')
    devices = []
    for i in range(0, num_devices):
        device_info = p.get_device_info_by_host_api_device_index(0, i)
        if device_info.get('maxInputChannels') > 0:  # Perangkat input audio
            devices.append((i, device_info.get('name')))
    return devices

# Memilih perangkat input audio
def pilih_mic_device():
    devices = list_audio_devices()
    print("Pilih perangkat input suara:")
    for idx, (device_id, device_name) in enumerate(devices):
        print(f"{idx}: {device_name}")
    choice = int(input("Masukkan nomor perangkat: "))
    return devices[choice][0]

mic_device_index = pilih_mic_device()

# Membuka stream dengan perangkat input audio yang dipilih
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, 
                input_device_index=mic_device_index, frames_per_buffer=CHUNK)

status_suara = False  # False berarti tidak ada suara, True berarti ada suara

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status_suara')
def get_status_suara():
    return jsonify({'status_suara': bool(status_suara)})

def deteksi_suara():
    global status_suara
    while True:
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        volume = np.linalg.norm(data)
        status_suara = volume > THRESHOLD

if __name__ == '__main__':
    # Menjalankan deteksi suara di thread terpisah
    thread = threading.Thread(target=deteksi_suara)
    thread.start()
    
    app.run(debug=True)
