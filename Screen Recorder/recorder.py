import tkinter as tk
import threading
import cv2
import pyautogui
import numpy as np

class ScreenRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Recorder")

        self.recording = False
        self.recording_thread = None

        self.start_button = tk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop Recording", command=self.stop_recording, state="disabled")
        self.stop_button.pack()

    def start_recording(self):
        self.recording = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

        self.recording_thread = threading.Thread(target=self.record_screen)
        self.recording_thread.start()

    def stop_recording(self):
        self.recording = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def record_screen(self):
        screen_width, screen_height = pyautogui.size()
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter("recording.avi", fourcc, 20.0, (screen_width, screen_height))

        while self.recording:
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            out.write(frame)

        out.release()

if __name__ == "__main__":
    root = tk.Tk()
    recorder = ScreenRecorder(root)
    root.mainloop()
