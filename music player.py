import pygame
from tkinter import Tk, Button, filedialog

# Initialize pygame
pygame.init()
global selected_music


# Function to play selected music file
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load(selected_music)
    pygame.mixer.music.play()


# Function to stop music playback
def stop_music():
    pygame.mixer.music.stop()


# Function to select a music file
def select_music():
    global selected_music
    selected_music = filedialog.askopenfilename(initialdir="/", title="Select A Song",
                                                filetypes=(("MP3 files", ".mp3"), ("all files", ".*")))
    play_music()


# Create Tkinter window
root = Tk()
root.title("Music Player")

# Set background color
root.configure(background='#6495ED')

# Set button size and font style
button_width = 20
button_height = 2
font_style = ('Helvetica', 14)

root.geometry("500x350+500+200")

# Create buttons with modified appearance
select_button = Button(root, text="Select Music", command=select_music, border=0, width=button_width,
                       height=button_height, font=font_style, background='#FFD700')
play_button = Button(root, text="Play", command=play_music, border=0, width=button_width, height=button_height,
                     font=font_style, background='#FF4500', fg='white')
stop_button = Button(root, text="Stop", command=stop_music, border=0, width=button_width, height=button_height,
                     font=font_style, background='#32CD32', fg='white')

# Place buttons in the window
select_button.pack(pady=20)
play_button.pack(pady=10)
stop_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()