import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Path to the music directory
music_dir = r"H:\music"

# List all music files in the directory
music_files = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]

if not music_files:
    print("No music files found.")
    exit()

def play_song(song_index):
    music_file = os.path.join(music_dir, music_files[song_index])
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    print(f"Playing: {music_files[song_index]}")

# Display the list of music files and prompt the user to select one
def choose_song():
    print("Available songs:")
    for idx, file in enumerate(music_files):
        print(f"{idx + 1}. {file}")

    choice = int(input("Enter the number of the song you want to play: ")) - 1
    return choice

current_song_index = choose_song()
play_song(current_song_index)

print("Press 'p' to pause, 'r' to resume, 's' to stop, 'c' to change the song, or 'q' to quit.")

while True:
    command = input("Command: ").strip().lower()
    if command == 'p':
        pygame.mixer.music.pause()
        print("Music paused.")
    elif command == 'r':
        pygame.mixer.music.unpause()
        print("Music resumed.")
    elif command == 's':
        pygame.mixer.music.stop()
        print("Music stopped.")
    elif command == 'c':
        pygame.mixer.music.stop()
        current_song_index = choose_song()
        play_song(current_song_index)
    elif command == 'q':
        pygame.mixer.music.stop()
        print("Music stopped.")
        break
    else:
        print("Invalid command. Use 'p' to pause, 'r' to resume, 's' to stop, 'c' to change the song, or 'q' to quit.")
