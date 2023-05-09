import os
import tempfile
import cv2

def camera():
  temp_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
  temp_file_path = temp_file.name
  temp_file.close()

  camera = cv2.VideoCapture(0)
  #кадр
  ret,frame = camera.read()
  cv2.imwrite(temp_file_path,frame)
  camera.release()

  return temp_file_path

def delete(path):
    os.remove(path)