
import face_recognition
import os
cwd = os.getcwd()

image_src = os.path.join(cwd,"src/images/p1.png")

image = face_recognition.load_image_file(image_src)
face_landmarks_list = face_recognition.face_landmarks(image)
print(face_landmarks_list)





