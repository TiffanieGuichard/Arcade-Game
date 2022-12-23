import time
from replit import audio


def end_game_sound():
  source = audio.play_file("Sound_Folder/sound/1realwinner.wav")
  while time.sleep(1):
	  pass

def game_point_sound():
  source = audio.play_file("Sound_Folder/sound/1game_point_sound.wav")
  while time.sleep(1):
    pass

def tie_sound():
  source = audio.play_file("Sound_Folder/sound/1tie_sound.wav")
  while time.sleep(1):
    pass


