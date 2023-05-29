import face_recognition
import cv2
import numpy as np

import glob

dataset_dir = '../pics/'
save_dir = '../detected_faces/'

for image_path in glob.glob(dataset_dir + '/*'):
    name = image_path.split('/')[-1]
    image = cv2.imread(image_path)
    small_frame = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    #face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Display the results
    for top, right, bottom, left in face_locations:
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        #cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #font = cv2.FONT_HERSHEY_DUPLEX
        #cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    #cv2.imshow('Video', image)
    #cv2.waitKey(0)
    cv2.imwrite(save_dir+name, image)

