import cv2   #opencv Lib
#import Adafruit_DHT
import pickle #lib to save students information for further verification 
import numpy as np #lib for array manipulation [image]
import face_recognition #recognition lib
import os # lib for directory manipulation
from datetime import *  #date
import datetime         #date
from datetime import datetime   #date     
from datetime import date               #date
from student import * #import the class [student.py]
import mysql.connector #mysql library for sending queries

#*******************************************************************************************
def GetTemp():                                                                      #*******      
    sensor=Adafruit_DHT.DHT11                                                       #*******
    gpio=17                                                                         #*******
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)                   #*******
    if humidity is not None and temperature is not None:                            #*******
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))  #*******
    else:                                                                           #*******
        print('Failed to get reading. Try again!')                                  #*******
#*******************************************************************************************


#****************************
def OpenDoor():            #*
    pass                   #*
#****************************


today=str(datetime.now())  # getting date as a string
with open("studentlist.dat", "rb") as fp:  # openening the student data file
        SavedList = pickle.load(fp)        #saving the file in a variable named SavedList
x=0     
path = 'images'                         #Student images folder to scan and 
path2= 'people'                         #path for saving unknown people
images = []                             #create an array named images   
classNames = []                         #create an array names classNames
myList = os.listdir(path)               #list the images folder and save the data in mylist varialbe --> it will contain all the images names {'barack obama.jpg','joe biden.jpg'}
for cl in myList:                       # for each image name in the list we listed before
    curImg = cv2.imread(f'{path}/{cl}') #read the first image
    images.append(curImg)               #add the image to the images array
    classNames.append(os.path.splitext(cl)[0])      #then add the added image name to the classnames but remove the .jpg
print(classNames)                                   #printing the result
def findEncodings(images):                          #creating a method you pass to it an image List and it will return its encoding as a List
    encodeList = []                                 #image encoding List
    for img in images:                              #for each image in images list {refer to Line 44 and 49}
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #adapt the image color to match opencv requirment
        encode = face_recognition.face_encodings(img)[0] #get the images encoding (which is used to compare 2 people and get if they are the same person or not) and save it in the variable encoding
        encodeList.append(encode)                        #add the encoding we just got to the encoding list   
    return encodeList                                    # return the  encoding list when done
encodeListKnown = findEncodings(images)                    # create a list of known people to compare with video feed
cap = cv2.VideoCapture(0)                               #initilize the camera for video capture
while True:                                             #loop until we break
    success, img = cap.read()                           #read 2 value from the camera , success for being capturing and img for the frame/image captured from the image
    scale_percent = 120
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    imgS = cv2.resize(img,dim,None,0.25,0.25)         #resize the captured image for faster processing
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)        #change its color to match the saved images colors refer to line 55
    facesCurFrame = face_recognition.face_locations(imgS)   #get the location of the face to draw around it a bounding box later
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)   # if found a face get the encoding of it to compare with the list of known people
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):           #for each face encoding and face location in the captured frame
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)    #compare the list of known people with the captured frame
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)    #if found a face ,compare the distance of the face from the frame with the known people list 
        matchIndex = np.argmin(faceDis)                                         # get the best value of the face distance
        y1,x2,y2,x1 = faceLoc                                                  #equation to draw a box around the face
        y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4                                    #
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)                          # drawing the box
        if matches[matchIndex]:
            name = classNames[matchIndex]                                       #get the name for that person
            rn=datetime.now().strftime('%Y-%m-%d__%H_%M_%S')                    #get current time with seconds
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),1)                   #Draw a rectangle around the image
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),1) #write a text with the recognized name
            for i in SavedList:                     #for each student saved check if he's attending 
                if(i.first + " "+i.last ==name):    #if the recognized face is saved in the studentList (Using the GUI) 
                 cv2.putText(img,"Attendance Was taken For "+name,(20,99),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),1)      #add text "attendance taken to + name of recognized person"
        else:
            cv2.putText(img,"Student not in database !",(40,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2) #if student is not registered show this text " student not in database"
    cv2.putText(img,"Press Q to exit",(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)   # putting a text " press q to exit"
    cv2.imshow('Webcam',imgS)        # shows the camera window
    if cv2.waitKey(1) & 0xFF == ord('q'):       # if 'Q' is pressed , break and quit the program
        cap.release()   # release the video ( stop the camera)
        cv2.destroyAllWindows()
