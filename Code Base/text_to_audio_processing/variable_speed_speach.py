from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def text_to_speech_with_variable_speed(text, speeds, output_file):
    words = text.split()
    if len(words) != len(speeds):
        raise ValueError("The number of words and speeds must be the same")

    # Generate TTS for each word
    audio_segments = []
    for word, speed in zip(words, speeds):
        tts = gTTS(word)
        temp_file = "temp_word.mp3"
        tts.save(temp_file)

        # Load the audio file and change its speed
        audio = AudioSegment.from_file(temp_file)
        audio = audio.speedup(playback_speed=speed)
        audio_segments.append(audio)

        # Clean up temporary file
        os.remove(temp_file)

    # Concatenate all audio segments
    combined = AudioSegment.silent(duration=0)
    for segment in audio_segments:
        combined += segment + AudioSegment.silent(duration=200)  # Adding a short pause between words

    # Export the final audio file
    combined.export(output_file, format="mp3")

# Example usage
text = "Hello world this is a test"
speeds = [1.2, 1.2, 1.2, 1.5, 0.9, 1.3]  # Different speeds for each word
output_file = "output_speech.mp3"
text_to_speech_with_variable_speed(text, speeds, output_file)











'''import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Set the rate (speed) of speech (default is 200)
engine.setProperty('rate', 150)  # Adjust as needed
def say_with_custom_speed(text, word_speeds):
    engine = pyttsx3.init()
    for word in text.split():
        rate = word_speeds.get(word.lower(), 150)  # Default rate: 150
        engine.setProperty('rate', rate)
        engine.say(word)
    engine.runAndWait()

# Example usage
custom_speeds = {
    'python': 200,  # Faster for the word 'Python'
    'explore': 100,  # Slower for the word 'explore'
}
input_text = "Python is amazing! Let's explore its power."
say_with_custom_speed(input_text, custom_speeds)
'''