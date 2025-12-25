👁️ Eye-Link: Assistive Eye-Tracking Communication System

Eye-Link is an innovative hybrid (Software + Hardware) assistive technology system designed to empower individuals with severe physical disabilities, such as Quadriplegia or Locked-in Syndrome. By utilizing computer vision and a standard webcam, it transforms eye movements into a powerful tool for communication and environmental control.

🚀 Features

🗣️ Verbal Communication: Converts eye-selected text into audible speech using Text-to-Speech (TTS).

🏠 Smart Home Control: Controls 4 physical appliances (Light, Fan, Heater, AC) via Arduino & Relays.

👁️ Precise Eye Tracking: Uses MediaPipe Face Mesh for accurate iris tracking and blink detection.

🧠 Smart Logic:

1 Blink: Navigate Down ▼

2 Blinks: Select / Confirm ✅

3 Blinks: Navigate Up ▲

🖥️ High-Contrast GUI: Designed specifically for accessibility with a dark mode interface to reduce eye strain.

🔊 Visual & Audio Feedback: Provides immediate feedback via LCD screen, Buzzer, and TTS.

🛠️ Tech Stack & Hardware

Software

Language: Python 3.10+

Libraries: OpenCV, MediaPipe, Tkinter, pyttsx3, pyserial, pywin32.

Hardware

Microcontroller: Arduino Uno (or Nano).

Sensors/Modules:

4-Channel Relay Module.

I2C LCD Screen (16x2).

Active/Passive Buzzer or Speaker.

Standard USB Webcam.

⚙️ Installation

1. Clone the Repository

git clone [https://github.com/YourUsername/Eye-Link.git](https://github.com/YourUsername/Eye-Link.git)
cd Eye-Link


2. Install Dependencies

pip install -r requirements.txt


(Note: If you are on Windows, ensure pywin32 is installed for audio stability).

3. Hardware Setup

Upload the EyeLink_Firmware.ino code to your Arduino.

Connect the components as follows:

Relays: Pins 2, 3, 4, 5

Buzzer: Pin 6

LCD: SDA -> A4, SCL -> A5

4. Run the System

python main.py


📸 Screenshots & Demo

Main Interface

(Place a screenshot of your GUI here)

The interface is designed with large fonts and high contrast for easy visibility.

Hardware Circuit

(Place a photo of your Arduino circuit here)

The system integrates seamlessly with home appliances.

👥 The Team (G26)

Developed by students of Elsewedy University of Technology (SUT) - Computer Science Dept.

Name

Role

Youssef Mahmoud Saber

Team Leader & System Architect

Hisham Rabe Abdrahman

AI Developer (Core Tracking)

Mohamed Walaa Ahmed

AI Developer (Logic Core)

Marez Rafaat Lotfy

Data Structures & Menu Logic

Adam Said Abdeltawab

Embedded Systems Engineer

Madona Khaled Sad

GUI Designer

Rami Sameh Abdelaziz

AI Integration Specialist

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

<p align="center">
Made with ❤️ by Team G26 




For a better, more accessible world.
</p>
