import cv2

#load pre-trained data from opencv
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose image to detect face in
#img = cv2.imread('test.jfif')
# sizedimg = cv2.resize(img, (780, 540), 
#                interpolation = cv2.INTER_NEAREST)

#capture video from webcam
webcam = cv2.VideoCapture(0)

#iterate over frames
while True:
    successful_frame_read, frame = webcam.read()

    # covert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    #draw rectangles around the faces
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('Face Detector App',frame)
    key = cv2.waitKey(1)

    #stop if Q key is pressed
    if key==81 or key==113:
        break

#release webcam images
webcam.release()

"""
#detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#draw rectangles around the faces
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)

# print(face_coordinates)

cv2.imshow('Face Detector App',img)
cv2.waitKey()
"""
print("Code Completed")
