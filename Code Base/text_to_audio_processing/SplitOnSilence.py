from pydub import AudioSegment
from pydub.silence import split_on_silence

# Load your audio (replace "your_audio.mp3" with your actual file path)
song = AudioSegment.from_wav ("/Path/To/split_on_silence/one_ad_constant_1.wav")

# Split the track where the silence is 2 seconds or more
chunks = split_on_silence(song, min_silence_len=12, silence_thresh=-16)

# Process each chunk
for i, chunk in enumerate(chunks):
    # Add 0.5 seconds of silence at the start and end of each chunk
    silence_chunk = AudioSegment.silent(duration=500)
    audio_chunk = silence_chunk + chunk + silence_chunk

    # Normalize the entire chunk
    normalized_chunk = audio_chunk.set_frame_rate(44100).set_channels(2).set_sample_width(2)

    # Export the audio chunk with a new bitrate
    print(f"Exporting chunk{i}.wav")
    normalized_chunk.export(f"./split_on_silence/chunk{i}.wav", bitrate="192k", format="wav")
