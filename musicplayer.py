import os
import pygame
import tkinter as tk
from tkinter import filedialog

pygame.mixer.init()

def load_and_play():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        current_song.set(os.path.basename(file_path))


def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()
    
    
# GUI
root = tk.Tk()
root.title("Music Player")
root.geometry("600x250") 
root.configure(bg="#e8f5e9")

current_song = tk.StringVar()

top_frame = tk.Frame(root, bg="#e8f5e9")
top_frame.pack(pady=10)

bottom_frame = tk.Frame(root, bg="#e8f5e9")
bottom_frame.pack(pady=10)

tk.Label(top_frame, text="Now Playing:", bg="#e8f5e9").pack()
tk.Label(top_frame, textvariable=current_song, bg="#e8f5e9").pack()

# Style 
button_style = {
    "font": ("Arial", 9),
    "width": 16,
    "height": 2,
    "bg": "#81c784",
    "activebackground": "#66bb6a"
}

tk.Button(bottom_frame, text="Load and Play", command=load_and_play, **button_style).pack(side=tk.LEFT, padx=5)
tk.Button(bottom_frame, text="Pause", command=pause_music, **button_style).pack(side=tk.LEFT, padx=5)
tk.Button(bottom_frame, text="Unpause", command=unpause_music, **button_style).pack(side=tk.LEFT, padx=5)
tk.Button(bottom_frame, text="Stop", command=stop_music, **button_style).pack(side=tk.LEFT, padx=5)

root.mainloop()