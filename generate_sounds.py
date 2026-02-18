"""
Generate simple audio files for slot machine game.
This script creates spin.mp3 and win.mp3 files.
"""

import wave
import struct
import math
import os

def generate_sine_wave(frequency, duration_ms, sample_rate=44100):
    """Generate a sine wave tone."""
    num_samples = int(sample_rate * duration_ms / 1000)
    frames = []
    
    for i in range(num_samples):
        t = float(i) / sample_rate
        sample = int(32767 * 0.8 * math.sin(2 * math.pi * frequency * t))
        frames.append(struct.pack('<h', sample))
    
    return b''.join(frames)

def create_wav_from_sine(filename, frequencies, durations_ms, sample_rate=44100):
    """Create a WAV file from multiple sine wave tones."""
    # Create output directory if needed
    output_dir = os.path.dirname(filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    audio_data = b''
    for freq, duration in zip(frequencies, durations_ms):
        audio_data += generate_sine_wave(freq, duration, sample_rate)
    
    # Create WAV file
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 2 bytes per sample
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_data)
    
    print(f"Created: {filename}")

def generate_spin_sound(output_path):
    """Generate spin sound (descending tones)."""
    frequencies = [800, 700, 600, 500, 400, 300]
    durations = [100, 80, 80, 80, 80, 100]
    create_wav_from_sine(output_path, frequencies, durations)

def generate_win_sound(output_path):
    """Generate win sound (ascending tones with celebration)."""
    frequencies = [400, 500, 600, 700, 800, 900, 800, 900, 1000]
    durations = [100, 100, 100, 100, 100, 150, 150, 150, 200]
    create_wav_from_sine(output_path, frequencies, durations)

if __name__ == '__main__':
    frontend_dir = os.path.join(os.path.dirname(__file__), 'frontend', 'sounds')
    
    print("Generating audio files...")
    print("-" * 40)
    
    # Create spin sound
    spin_file = os.path.join(frontend_dir, 'spin.wav')
    generate_spin_sound(spin_file)
    
    # Create win sound
    win_file = os.path.join(frontend_dir, 'win.wav')
    generate_win_sound(win_file)
    
    print("-" * 40)
    print("✅ Audio files created successfully!")
    print(f"Note: Files are created as WAV format.")
    print(f"To use MP3 format, convert using:")
    print(f"  ffmpeg -i spin.wav spin.mp3")
    print(f"  ffmpeg -i win.wav win.mp3")
    print(f"Or update script.js to use .wav instead of .mp3")
