import face_recognition
import glob

dataset_dir = '../pics/'

# Load the jpg files into numpy arrays
selfie = face_recognition.load_image_file("../selfie/IMG_1290.jpeg")
selfie_encoding = face_recognition.face_encodings(selfie)[0]
known_face_encodings = [selfie_encoding, ]
# Or encoding pool
# upload this encoding with name to cloud
# for each face encoding, we can recognize the name

results = []
res = False
for image_path in glob.glob(dataset_dir + '/*'):
    res = False
    name = image_path.split('/')[-1]
    image = face_recognition.load_image_file(image_path)
    image_encodings = face_recognition.face_encodings(image)

    #face_names = []
    face_distances_min = 10e+5
    for face_encoding in image_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        if matches[0] == True:
            res = True
        #name = "Unknown"

        # Or instead, use the known face with the smallest distance to the new face
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)[0]
        if face_distance<face_distances_min:
            face_distances_min=face_distance
        #best_match_index = np.argmin(face_distances)
        #if matches[best_match_index]:
        #    name = known_face_names[best_match_index]

        #face_names.append(name)
    results.append(res)
    print(name, res) #, face_distances_min)


