import tempfile
import sounddevice as sd
import soundfile as sf
import os


def recording():
  # Установите параметры записи
  duration = 10  # Продолжительность записи в секундах
  sample_rate = 44100  # Частота дискретизации

  # Создайте временный файл и получите его путь
  temp_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
  temp_file_path = temp_file.name
  temp_file.close()

  # Запишите звук с микрофона
  #print("Запись началась")
  myrecording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
  sd.wait()  # Ожидание, пока запись завершится
  #print("Запись завершена")

  # Сохраните записанный звук во временный файл
  sf.write(temp_file_path, myrecording, sample_rate)

  #print(f"Файл звука сохранен во временном файле {temp_file_path}")

  return temp_file_path

def delete(path):
  os.remove(path)