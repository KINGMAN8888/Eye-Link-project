import serial
import time
import config

class ArduinoController:
    def __init__(self):
        self.ser = None
        try:
            print(f"[Hardware] Connecting to {config.SERIAL_PORT}...")
            self.ser = serial.Serial(config.SERIAL_PORT, config.BAUD_RATE, timeout=1, write_timeout=1)
            
            time.sleep(3) 
            
            print(f"[Hardware] ✅ Connected Successfully to {config.SERIAL_PORT}")
            self.send_command("MSG:App Connected")
            
        except Exception as e:
            print(f"[Hardware] ❌ Warning: Arduino not connected. ({e})")
            print("[Hardware] Running in Simulation Mode.")

    def send_command(self, command):
        if self.ser and self.ser.is_open and command:
            try:
                full_command = command + '\n'
                self.ser.write(full_command.encode('utf-8'))
                print(f"[Hardware] Sent: {command}")
            except Exception as e:
                print(f"[Hardware] Error sending data: {e}")
        else:
            if command:
                print(f"[Hardware Simulation] Would send: {command}")

    def close(self):
        if self.ser and self.ser.is_open:
            print("[Hardware] Closing Serial Connection...")
            self.ser.close()