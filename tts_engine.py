from gtts import gTTS
import os
import pygame


class TTSEngine:
    def __init__(self, output_dir="audio"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def text_to_speech(self, text, filename="output.mp3"):
        filepath = os.path.join(self.output_dir, filename)
        tts = gTTS(text=text, lang='en')
        tts.save(filepath)
        return filepath
    
    def play_audio(self, filepath):
        self.play_sound(filepath)
    
    def play_sound(self, file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)