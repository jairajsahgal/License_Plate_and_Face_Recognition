import cv2
import numpy as np
import face_recognition
import os

def findEncoding(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def facial_recognition(img):
    name=None
    final_img=None
    path = "People"
    images = []
    classNames = []
    myList = os.listdir(path=path)
    # print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    encodeListKnow = findEncoding(images)
    print('Encoding Complete')
    # print(classNames)
    imgS = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    # encode = face_recognition.face_encodings(img)
    facesCurFrame = face_recognition.face_locations(imgS) # top, right, bottom, left
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLocation in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnow,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnow,encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis) # To find minimum

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1,x2,y2,x1 = faceLocation

            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-15),(x2,y2+10),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2+6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
            cv2.imwrite(name+'.jpg',img)
            final_img = img
            break
    return name,img

# path = "People"
# images = []
# classNames = []
# myList = os.listdir(path=path)
# print(myList)
# for cl in myList:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])
# print(classNames)

# def findEncoding(images):
#     encodeList = []
#     for img in images:
#         img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)
#     return encodeList


# encodeListKnow = findEncoding(images)
# print(len('Encoding Complete'))
# cap = cv2.VideoCapture(0)

# while True:
#     success,img = cap.read()
#     # imgS = cv2.resize(img,(0,0),None,0.25,0.25)
#     imgS = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     # encode = face_recognition.face_encodings(img)
#     facesCurFrame = face_recognition.face_locations(imgS) # top, right, bottom, left
#     encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
#
#     for encodeFace,faceLocation in zip(encodesCurFrame,facesCurFrame):
#         matches = face_recognition.compare_faces(encodeListKnow,encodeFace)
#         faceDis = face_recognition.face_distance(encodeListKnow,encodeFace)
#         print(faceDis)
#         matchIndex = np.argmin(faceDis)
#
#         if matches[matchIndex]:
#             name = classNames[matchIndex].upper()
#             print(name)
#             y1,x2,y2,x1 = faceLocation
#
#             cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
#             cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
#             cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
#     cv2.imshow('Webcam',img)
#     cv2.waitKey(1)

# faceLoc = face_recognition.face_locations(imgElon)[0] # top, right, bottom, left
# encodeElon = face_recognition.face_encodings(imgElon)[0]
# cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),thickness=2)
#
# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeElonTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),thickness=2)
