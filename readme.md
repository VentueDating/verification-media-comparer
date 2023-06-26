Dependency:

    pip3 install face_recognition


To play with face detection and face comparison,
you need to first put several images under ./pics and put one image under ./selfie/
then run examples/face_detection.py, you can see processed images with rectangles under ./detected_faces

    python3 examples/face_detection.py
or run examples/face_comparison.py, you can see the matching results from console

    python3 examples/face_comparison.py

All the APIs are under ./api:
1) face_compare.py: output True/False given a selfie image and a set of images
2) liveness_check_random.py: dummpy implementation of liveness check. Will be changed in the future.