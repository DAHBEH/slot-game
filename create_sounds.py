"""
Generate audio files for slot machine
"""
import wave
import struct
import math
import os

def generate_sine_wave(frequency, duration_ms, amplitude=0.3, sample_rate=44100):
    """Generate a sine wave"""
    num_samples = int(sample_rate * duration_ms / 1000)
    frames = []
    
    for i in range(num_samples):
        t = float(i) / sample_rate
        sample = int(32767 * amplitude * math.sin(2 * math.pi * frequency * t))
        frames.append(struct.pack('<h', sample))
    
    return b''.join(frames)

def create_wav_file(filename, frequencies, durations_ms):
    """Create a WAV file from list of frequencies and durations"""
    audio_data = b''
    sample_rate = 44100
    
    for freq, duration in zip(frequencies, durations_ms):
        audio_data += generate_sine_wave(freq, duration, sample_rate=sample_rate)
    
    # Write WAV file
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_data)
    
    print(f"✓ Created: {filename}")

if __name__ == '__main__':
    sounds_dir = os.path.join(os.path.dirname(__file__), 'frontend', 'sounds')
    os.makedirs(sounds_dir, exist_ok=True)
    
    print("Generating audio files...")
    print("-" * 50)
    
    # Spin sound - descending tones
    spin_file = os.path.join(sounds_dir, 'spin.wav')
    frequencies = [800, 700, 600, 500, 400, 300, 200]
    durations = [100, 100, 100, 100, 100, 100, 150]
    create_wav_file(spin_file, frequencies, durations)
    
    # Win sound - ascending celebration
    win_file = os.path.join(sounds_dir, 'win.wav')
    frequencies = [400, 500, 600, 700, 800, 900, 1000, 1100, 1000, 900]
    durations = [100, 100, 100, 100, 100, 100, 100, 150, 150, 200]
    create_wav_file(win_file, frequencies, durations)
    
    print("-" * 50)
    print("✅ Audio files created successfully!")
