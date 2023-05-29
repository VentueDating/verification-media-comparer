import face_recognition
import numpy as np

def compare_selfie_with_images(selfie, images, known_face_encodings=None, threshold=0.8):
    '''
    See if some of the faces in the images match with the selfie
    :param selfie: a 3D array
    :param images: a list of 3D array
    :param known_face_encodings: a list of existing face encodings. Input the encoding pool, if none, this is set to only the selfie
    :param threshold: float number from [0, 1]. if the selfie matches with at least threshold*len(images), then it is a match
    :return: True=match, False=not match
    '''
    selfie_encoding = face_recognition.face_encodings(selfie)[0]
    if known_face_encodings is None:
        known_face_encodings = [selfie_encoding, ]
    results = []
    for image_sub in images:
        res = 0
        image_encodings = face_recognition.face_encodings(image_sub)
        for face_encoding in image_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            if matches[0]:
                res = 1
        results.append(res)
    if np.sum(results) >= threshold * len(images):
        return True
    else:
        return False
