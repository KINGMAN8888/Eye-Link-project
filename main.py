import tkinter as tk
import cv2
import pyttsx3
import threading
import time
import atexit
import pythoncom

import config
import menu_data
from eye_tracker import EyeTracker
from hardware import ArduinoController
from gui_interface import EyeLinkUI 

class EyeLinkApp:
    def __init__(self, root):
        self.root = root
        self.ui = EyeLinkUI(root)
        self.tracker = EyeTracker()
        self.arduino = ArduinoController()
        atexit.register(self.cleanup)

        self.current_menu = "Main Menu"
        self.items = menu_data.get_menu_items(self.current_menu)
        self.selected_index = 0
        self.is_frozen = False 

        self.blink_count_buffer = 0       
        self.last_blink_end_time = 0      
        self.frames_eye_closed = 0        
        self.in_cooldown = False
        
        self.WAIT_WINDOW = 0.8            
        self.MIN_FRAMES_FOR_BLINK = 2     
        self.COOLDOWN_TIME = 2000         

        self.cap = cv2.VideoCapture(config.CAMERA_ID)
        self.update_loop(root)

    def speak_sequence(self, text, repeat=3):
        
        if self.arduino:
            self.arduino.send_command(f"MSG:{text}")

        def _speak():
            try:
                pythoncom.CoInitialize() 
                temp_engine = pyttsx3.init()
                
                try:
                    voices = temp_engine.getProperty('voices')
                    for voice in voices:
                        if "David" in voice.name or "English" in voice.name:
                            temp_engine.setProperty('voice', voice.id)
                            break
                    
                    temp_engine.setProperty('rate', 130)
                    temp_engine.setProperty('volume', 1.0)
                except: pass

                for i in range(repeat):
                    if not self.is_frozen: break
                    
                    print(f"[Speaker] Saying ({i+1}/{repeat}): {text}")
                    temp_engine.say(text)
                    temp_engine.runAndWait()
                    time.sleep(0.5)
                
                temp_engine.stop()
                
            except Exception as e:
                print(f"TTS Error: {e}")

            try:
                pythoncom.CoUninitialize()
            except: pass

            self.root.after(100, self.reset_to_main)
            
        threading.Thread(target=_speak, daemon=True).start()

    def reset_to_main(self):
        self.is_frozen = False
        self.ui.show_action_screen("", show=False)
        self.current_menu = "Main Menu"
        self.items = menu_data.get_menu_items("Main Menu")
        self.selected_index = 0
        self.ui.update_menu_buttons(self.items, 0)
        self.ui.set_status("System Ready.")
        
        if self.arduino:
            self.arduino.send_command("MSG:System Ready")
        
        self.activate_cooldown()

    def activate_cooldown(self):
        self.in_cooldown = True
        self.blink_count_buffer = 0
        self.frames_eye_closed = 0
        self.ui.set_status("... Processing (Relax) ...")
        self.root.after(self.COOLDOWN_TIME, self.deactivate_cooldown)

    def deactivate_cooldown(self):
        self.in_cooldown = False
        self.ui.set_status("Ready.")

    def execute_logic(self):
        count = self.blink_count_buffer
        self.blink_count_buffer = 0 
        
        if count == 1:
            self.selected_index = (self.selected_index + 1) % len(self.items)
            self.ui.update_menu_buttons(self.items, self.selected_index)
            self.ui.set_status("▼ DOWN")
            self.activate_cooldown()

        elif count == 2:
            self.ui.set_status("✅ SELECT")
            self.confirm_selection()

        elif count >= 3:
            self.selected_index = (self.selected_index - 1) % len(self.items)
            self.ui.update_menu_buttons(self.items, self.selected_index)
            self.ui.set_status("▲ UP")
            self.activate_cooldown()

    def confirm_selection(self):
        selected_text = self.items[self.selected_index]
        self.is_frozen = True

        self.ui.show_action_screen(selected_text, show=True)

        if selected_text == "Back":
            self.reset_to_main() 
            return

        if selected_text in menu_data.communication_board and self.current_menu == "Main Menu":
            self.is_frozen = False
            self.ui.show_action_screen("", show=False)
            self.current_menu = selected_text
            self.items = menu_data.get_menu_items(selected_text)
            self.selected_index = 0
            self.ui.update_menu_buttons(self.items, 0)
            self.ui.set_status(f"Entered: {selected_text}")
            self.activate_cooldown()
            return

        cmd = menu_data.get_arduino_command(self.current_menu, selected_text)
        if cmd: 
            if self.arduino:
                self.arduino.send_command(cmd)
            self.speak_sequence(selected_text, repeat=3)
        else:
            self.speak_sequence(selected_text, repeat=3)

    def cleanup(self):
        print("[System] Cleaning up resources...")
        if self.arduino:
            self.arduino.close()
        if self.cap:
            self.cap.release()

    def update_loop(self, root):
        if self.is_frozen:
            root.after(50, lambda: self.update_loop(root))
            return

        ret, frame = self.cap.read()
        if ret:
            is_blink_signal, landmarks, ear_value = self.tracker.process_frame(frame)
            
            if landmarks:
                for (x, y) in landmarks:
                    cv2.circle(frame, (x, y), 1, (0, 255, 255), -1)
            
            if self.in_cooldown:
                cv2.putText(frame, "WAIT", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            else:
                if self.blink_count_buffer > 0:
                    cv2.putText(frame, f"Count: {self.blink_count_buffer}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

            if not self.in_cooldown:
                is_eye_closed_now = (ear_value < config.BLINK_THRESHOLD)

                if is_eye_closed_now:
                    self.frames_eye_closed += 1
                else:
                    if self.frames_eye_closed >= self.MIN_FRAMES_FOR_BLINK:
                        self.blink_count_buffer += 1
                        self.last_blink_end_time = time.time()
                        self.ui.set_status(f"Blink! ({self.blink_count_buffer})")
                    
                    self.frames_eye_closed = 0

                current_time = time.time()
                if self.blink_count_buffer > 0 and (current_time - self.last_blink_end_time > self.WAIT_WINDOW) and not is_eye_closed_now:
                    self.execute_logic()

            self.ui.update_video_feed(frame)

        root.after(30, lambda: self.update_loop(root))

if __name__ == "__main__":
    root = tk.Tk()
    app = EyeLinkApp(root)
    root.mainloop()