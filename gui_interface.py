import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk
import cv2
import config  


COLOR_BG_MAIN = "#000000"
COLOR_PANEL   = "#111111"
COLOR_ACCENT  = "#00E5FF"
COLOR_TEXT    = "#FFFFFF"
COLOR_SELECT  = "#FFD700"
COLOR_ACTION  = "#00FF00"

class EyeLinkUI:
    def __init__(self, root):
        self.root = root
        self.menu_frames = [] 
        self.menu_labels = [] 
        
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        self.root.title("Eye-Link System | G26")
        self.root.configure(bg=COLOR_BG_MAIN)
        self.root.state('zoomed')

        self.font_header = tkfont.Font(family="Arial", size=30, weight="bold")
        self.font_btn = tkfont.Font(family="Arial", size=20, weight="bold")
        self.font_big = tkfont.Font(family="Arial", size=40, weight="bold")

    def create_widgets(self):
        header = tk.Frame(self.root, bg=COLOR_BG_MAIN)
        header.pack(fill="x", pady=20)
        
        tk.Label(header, text="EYE-LINK PROJECT", font=self.font_header, 
                 bg=COLOR_BG_MAIN, fg=COLOR_ACCENT).pack()
        
        tk.Label(header, text="Team G26 - SUT", font=("Arial", 12), 
                 bg=COLOR_BG_MAIN, fg="gray").pack()

        self.main_container = tk.Frame(self.root, bg=COLOR_BG_MAIN)
        self.main_container.pack(expand=True, fill="both", padx=20, pady=10)

        self.left_panel = tk.Frame(self.main_container, bg=COLOR_PANEL)
        self.left_panel.pack(side="left", fill="both", expand=True, padx=10)
        
        self.buttons_container = tk.Frame(self.left_panel, bg=COLOR_PANEL)
        self.buttons_container.pack(fill="both", expand=True, pady=20)

        self.right_panel = tk.Frame(self.main_container, bg=COLOR_BG_MAIN)
        self.right_panel.pack(side="right", fill="both", padx=10)

        self.video_border = tk.Frame(self.right_panel, bg=COLOR_ACCENT, padx=4, pady=4)
        self.video_border.pack()
        self.lbl_video = tk.Label(self.video_border, bg="black")
        self.lbl_video.pack()
        
        tk.Label(self.right_panel, text="LIVE TRACKING", bg=COLOR_BG_MAIN, fg="red", font=("Arial", 10, "bold")).pack(pady=5)

        self.overlay_frame = tk.Frame(self.root, bg="black")
        self.lbl_action_title = tk.Label(self.overlay_frame, text="EXECUTING ACTION:", font=("Arial", 20), fg="gray", bg="black")
        self.lbl_action_title.pack(pady=(200, 20))
        
        self.lbl_action_text = tk.Label(self.overlay_frame, text="", font=self.font_big, fg=COLOR_ACTION, bg="black", wraplength=1000)
        self.lbl_action_text.pack(expand=True)

        self.lbl_confirmation = tk.Label(self.overlay_frame, text="", font=self.font_big, fg=COLOR_SELECT, bg="black", wraplength=1000)

        self.lbl_status = tk.Label(self.root, text="System Ready...", font=("Consolas", 14), bg="#222", fg="white", pady=10)
        self.lbl_status.pack(side="bottom", fill="x")

    def update_menu_buttons(self, items, selected_index):
        while len(self.menu_frames) < len(items):
            frame = tk.Frame(self.buttons_container, bg=COLOR_PANEL, bd=2, relief="groove")
            frame.pack(fill="x", pady=10, ipady=10)
            lbl = tk.Label(frame, text="", font=self.font_btn, bg=COLOR_PANEL, fg=COLOR_TEXT)
            lbl.pack(fill="both", expand=True)
            self.menu_frames.append(frame)
            self.menu_labels.append(lbl)

        for i, frame in enumerate(self.menu_frames):
            if i < len(items):
                frame.pack(fill="x", pady=10, ipady=10) 
                lbl = self.menu_labels[i]
                
                if i == selected_index:
                    frame.config(bg=COLOR_SELECT)
                    lbl.config(text=f"▶ {items[i]} ◀", bg=COLOR_SELECT, fg="black")
                else:
                    frame.config(bg=COLOR_PANEL)
                    lbl.config(text=items[i], bg=COLOR_PANEL, fg="gray")
            else:
                frame.pack_forget()

    def show_action_screen(self, text, show=True):
        if show:
            self.overlay_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.lbl_action_text.config(text=text)
            self.overlay_frame.lift()
        else:
            self.overlay_frame.place_forget()
    def show_confirmation_screen(self, text, show=True):
        self.show_action_screen(text, show)

    def update_video_feed(self, frame):
        frame = cv2.resize(frame, (400, 300))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(image=Image.fromarray(frame))
        self.lbl_video.config(image=img)
        self.lbl_video.image = img 

    def set_status(self, text):
        self.lbl_status.config(text=text)