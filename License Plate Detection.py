import cv2
from Text_Detection import detect_characters, detect_string, detect_words
import re
from live_recognition import facial_recognition
#
def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

####################################################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("../../Resources/haarcascade_russian_plate_number.xml")
minArea=500
color=(255,0,255)
name=None
# count = 0
state_codes = ['AP', 'AR', 'AS', 'BR', 'CG', 'GA', 'GJ', 'HR', 'HP', 'JH', 'KA', 'KL', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OD', 'PB', 'RJ', 'SK', 'TN', 'TR', 'UP', 'WB', 'TS','ap', 'ar', 'as', 'br', 'cg', 'ga', 'gj', 'hr', 'hp', 'jh', 'ka', 'kl', 'mp', 'mh', 'mn', 'ml', 'mz', 'nl', 'od', 'pb', 'rj', 'sk', 'tn', 'tr', 'up', 'wb', 'ts']
######################################################
# cap = cv2.VideoCapture("C:\\Users\\jaira\\PycharmProjects\\opencv_tutorial\\Resources\\test.mp4")
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
success, img = cap.read()
while success:

    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w*h

        if area  > minArea:
            cv2.rectangle(img=img,pt1=(x,y),pt2=(x+w,y+h),
                          color=color,thickness=2)
            # cv2.putText(img=img,text="Number Plate",org=(x,y-5),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,color=color,fontScale=1,thickness=2)
            imgRoi=img[y:y+h,x:x+w]
            cv2.moveWindow("ROI",40,30)
            cv2.imshow(winname="ROI",mat=imgRoi)

            temp=detect_words(imgRoi)
            for i in state_codes:
                if i in temp:
                    temp2 = ''.join(ch for ch in temp if ch.isalnum() and ch!="." and ch!="_")
                    if temp[-2:].isnumeric() and temp[2:4].isnumeric() and len(temp)==10:
                        cv2.putText(img=img,text=temp,org=(x,y-5),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,color=color,fontScale=1,thickness=2)
                        print(temp)

    if name==None:
        name,face_img=facial_recognition(img)
        cv2.imshow("Face Recognition",face_img)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # except:
    #     break
cv2.destroyAllWindows()