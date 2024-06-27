If you want to create audio files in different tones using Python, you can utilize libraries like pydub or librosa for audio processing and numpy for generating the tone. Below is a simple example using pydub:

python
Copy code
from pydub import AudioSegment
import numpy as np

def generate_tone(duration, frequency):
    # Generate time array
    t = np.linspace(0, duration, int(duration * 44100), endpoint=False)

    # Generate tone
    tone = 10000 * np.sin(2 * np.pi * frequency * t)

    # Normalize to 16-bit range
    tone = np.int16(tone * (2**15 - 1))

    return tone

def save_audio(filename, audio_data, sample_rate=44100):
    sound = AudioSegment(
        audio_data.tobytes(),
        frame_rate=sample_rate,
        sample_width=audio_data.dtype.itemsize,
        channels=1
    )
    sound.export(filename, format="wav")

# Example usage
tone_duration = 5  # seconds
tones = [100, 200, 300, 400]  # frequencies in Hz

for idx, freq in enumerate(tones):
    tone = generate_tone(tone_duration, freq)
    save_audio(f"tone_{freq}.wav", tone)
This script generates tones with different frequencies (100 Hz, 200 Hz, 300 Hz, 400 Hz) and saves them as WAV audio files. Adjust the tones list to include the frequencies you desire. This script creates tones of 5 seconds duration each. You can adjust the tone_duration variable to change the duration of the tones as needed.