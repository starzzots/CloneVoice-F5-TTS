"https://github.com/swivid/F5-TTS/"
"""f5-tts_infer-gradio"""
"http://127.0.0.1:7860"
from moviepy import VideoFileClip
path = "\\Users\\Kyle\\Documents\\Awillremove\\" # change path for you
# Input and output file paths
input_file = "{path}WIN_20250116_12_31_19_Pro.mp4"
output_file = "{path}output.wav"

# Load video file
video = VideoFileClip(input_file)

# Extract audio from video
audio = video.audio

# Write the audio to a .wav file
audio.write_audiofile(output_file)

print(f"Audio saved to {output_file}")


