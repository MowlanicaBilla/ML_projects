
import whisper
model = whisper.load_model("base")
result = model.transcribe("test_audio_file.mp3")
print(result["text"])