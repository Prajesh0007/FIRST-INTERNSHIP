import sounddevice as sd
from scipy.io.wavfile import write
import pyttsx3
import speech_recognition as sr
import os

def record_audio(filename="recorded.mp3", duration=5, fs=44100):
    """Records audio from the microphone and saves it as an MP3 file."""
    temp_wav = "temp_recorded.wav"
    print("Recording...")
    recorded_audio = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished
    write(temp_wav, fs, recorded_audio)
    os.rename(temp_wav, filename)  # Rename WAV to MP3 extension
    print(f"Recording saved as {filename}")

def text_to_speech(text, filename="output.mp3"):
    """Converts text to speech and saves it as an MP3 file."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speaking rate
    engine.setProperty('volume', 1.0)  # Set volume to maximum
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"Text-to-Speech audio saved as {filename}")

def speech_to_text(audio_file):
    """Converts speech from an audio file to text."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        print("Processing audio for speech recognition...")
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            print("Recognized Text:")
            print(text)
            return text
        except sr.UnknownValueError:
            print("Speech Recognition could not understand the audio.")
        except sr.RequestError:
            print("Could not request results, please check your internet connection.")
    return None

def clear_screen():
    """Clears the console screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    while True:
        clear_screen()
        print("\n===== AI Audio Processing Tool =====")
        print("\nChoose an option:")
        print("1. Record Audio (MP3)")
        print("2. Convert Text to Speech")
        print("3. Convert Speech to Text")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            while True:
                filename = input("Enter filename to save (default: recorded.mp3): ") or "recorded.mp3"
                duration = int(input("Enter duration (seconds, default: 5): ") or 5)
                record_audio(filename, duration)
                repeat = input("Record again? (yes/no): ").lower()
                if repeat != "yes":
                    break
        elif choice == "2":
            while True:
                text = input("Enter text to convert to speech: ")
                filename = input("Enter filename to save (default: output.mp3): ") or "output.mp3"
                text_to_speech(text, filename)
                repeat = input("Convert another text? (yes/no): ").lower()
                if repeat != "yes":
                    break
        elif choice == "3":
            while True:
                filename = input("Enter audio filename to transcribe (default: recorded.mp3): ") or "recorded.mp3"
                speech_to_text(filename)
                repeat = input("Transcribe another file? (yes/no): ").lower()
                if repeat != "yes":
                    break
        elif choice == "4":
            print("Exiting... Thank you for using the AI Audio Processing Tool!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
