<h1 align="center">👁️ Eye‑Link: Assistive Eye‑Tracking Communication System</h1>

<p align="center">
	Empowering individuals with severe physical disabilities through eye‑controlled communication and smart home interaction.
</p>

<p align="center">
	<a href="https://img.shields.io/badge/Python-3.10%2B-blue"> 
		<img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python 3.10+" />
	</a>
	<a href="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey">
		<img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey" alt="Platforms" />
	</a>
	<a href="https://img.shields.io/badge/License-MIT-green">
		<img src="https://img.shields.io/badge/License-MIT-green" alt="License MIT" />
	</a>
</p>

## Overview

Eye‑Link is a hybrid (software + hardware) assistive technology system that turns natural eye movements into commands for communication and environmental control. Using computer vision (MediaPipe Face Mesh) and a standard webcam, Eye‑Link enables text‑to‑speech communication and controls up to four home appliances via Arduino.

## Table of Contents
- Features
- Tech Stack
- Hardware Requirements
- Installation
- Hardware Setup
- Usage
- Blink Logic
- Screenshots
- Troubleshooting
- Roadmap
- Team (G26)
- License

## Features
- 🗣️ Text‑to‑Speech (TTS): Eye‑selected text is spoken aloud for verbal communication.
- 🏠 Smart Home Control: Operate Light, Fan, Heater, and AC via Arduino + relay module.
- 👁️ Precise Eye Tracking: MediaPipe Face Mesh for iris tracking and blink detection.
- 🧠 Interaction Logic: Simple blink‑based navigation and selection.
- 🖥️ Accessible GUI: High‑contrast, large fonts, dark mode for reduced eye strain.
- 🔊 Multi‑Modal Feedback: LCD, buzzer, and TTS provide immediate visual/audio feedback.

## Tech Stack
- **Language:** Python 3.10+
- **Libraries:** OpenCV, MediaPipe, Tkinter, `pyttsx3`, `pyserial`, `pywin32` (Windows)
- **Microcontroller:** Arduino Uno or Nano

## Hardware Requirements
- Standard USB webcam
- Arduino Uno/Nano
- 4‑Channel Relay Module
- I2C LCD Screen (16x2)
- Active/Passive buzzer or speaker

## Installation

1. Clone the repository

```bash
git clone https://github.com/YourUsername/Eye-Link.git
cd Eye-Link
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

Note: On Windows, ensure `pywin32` is installed for audio stability.

## Hardware Setup

1. Upload firmware
- Flash `EyeLink_Firmware.ino` to your Arduino using the Arduino IDE.

2. Wiring overview
- Relays: Pins `2`, `3`, `4`, `5`
- Buzzer: Pin `6`
- LCD (I2C): `SDA → A4`, `SCL → A5`
- Webcam: Connect to the host PC via USB

3. Verify serial connection
- Ensure the correct COM port is selected and available.

## Usage

Run the main application:

```bash
python main.py
```

Follow on‑screen menus: use blinks to navigate and select items. Selected phrases will be spoken via TTS, and appliance commands will be sent to Arduino.

## Blink Logic
- 1 Blink: Navigate Down ▼
- 2 Blinks: Select / Confirm ✅
- 3 Blinks: Navigate Up ▲

## Screenshots

> Place screenshots of your GUI and hardware setup here.

## Troubleshooting
- Webcam not detected: Check permissions and device selection; try another USB port.
- No audio output: On Windows, install `pywin32`; verify audio devices and `pyttsx3` voices.
- COM port issues: Confirm Arduino is flashed, drivers installed, and the correct port is selected.
- Tracking unstable: Ensure good lighting; position the webcam at eye level; reduce glare.

## Roadmap
- Multi‑language TTS support
- Configurable blink sensitivity and thresholds
- Expanded smart‑home device integrations
- Optional on‑device calibration wizard

## Team (G26)
Developed by students of Elsewedy University of Technology (SUT) – Computer Science Dept.

| Name | Role |
|------|------|
| Youssef Mahmoud Saber | Team Leader & System Architect |
| Hisham Rabe Abdrahman | AI Developer (Core Tracking) |
| Mohamed Walaa Ahmed | AI Developer (Logic Core) |
| Marez Rafaat Lotfy | Data Structures & Menu Logic |
| Adam Said Abdeltawab | Embedded Systems Engineer |
| Madona Khaled Sad | GUI Designer |
| Rami Sameh Abdelaziz | AI Integration Specialist |

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

<p align="center">
	Made with ❤️ by Team G26 — For a better, more accessible world.
</p>
