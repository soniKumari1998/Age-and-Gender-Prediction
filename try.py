# Library , Modules
from tkinter import *
import sys
import os
import cv2
import math
import argparse
import pafy
import numpy as np

# Implementing event on register button
def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(register_screen, text="REGISTRATION SUCCESSFUL", fg="green", font=("TIMES NEW ROMAN",15,"bold")).pack()

# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("REGISTERATION FORM")
    register_screen.geometry("400x350")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="PLEASE REGISTER FIRST TO LOGIN FIRST TIME",relief=GROOVE, font=("TIMES NEW ROMAN", 15,"bold") ,bg="grey",fg="black").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="USERNAME * ",bg="light green",font=("TIMES NEW ROMAN",10,"bold"))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="PASSWORD * ",bg="light green",font=("TIMES NEW ROMAN",10,"bold"))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="REGISTER", width=10, height=1, bg="light green",fg="black",font=("TIMES NEW ROMAN",10,"bold"), command=register_user).pack()

# Implementing event on login button
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("LOGIN SYSTEM")
    login_screen.geometry("400x350")
    Label(login_screen, text="PLEASE ENTER THE DETAILS",relief=GROOVE, font=("TIMES NEW ROMAN", 15,"bold"),bg="grey").pack()
    Label(login_screen, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="USERNAME * ",bg="light blue",font=("TIMES NEW ROMAN",10,"bold")).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="PASSWORD * ",bg="light blue",font=("TIMES NEW ROMAN",10,"bold")).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="LOGIN", width=10, height=1,bg="light blue", command=login_verify,font=("TIMES NEW ROMAN",10,"bold")).pack()
# code for image or webcam
def imagewebcam():
    root=Tk() #for intializing window
    root.geometry("800x800")
# def close(root):
# root.destroy()
    Label(root,text="  WELCOME TO AGE AND GENDER PREDICTION  ", bg="grey", relief=GROOVE,
          font=("TIMES NEW ROMAN", 20, "bold")).pack(padx=10, pady=10)
    Label(root,text="PLEASE ENTER YOUR CHOICE", bg="black", fg="white", font=("TIMES NEW ROMAN", 15),
          width="30", height="2").pack(padx=10, pady=50)
#Label(root, text='please enter your choice',fg="white",compound="left",relief=GROOVE,font=("TIMES NEW ROMAN", 30,"bold"),bg="brown").grid(row=2,column=4,padx=40,pady=10)
    Button(root,text="WEBCAM", height="2", width="30", bg="light blue",font=("TIMES NEW ROMAN",15,"bold"), command=agegender).pack(padx=20, pady=30)
    Label(text="").pack()
    Button(root,text="YOUTUBE URL", height="2", width="30", bg="light blue",font=("TIMES NEW ROMAN",15,"bold"), command=youtube).pack()
# Button(root, text='URL',bg="light green",font=("TIMES NEW ROMAN", 20,"bold"),command=youtube,).grid(row=3,column=3,padx=80,pady=100)
# Button(root, text='using webcam',bg="light green",font=("TIMES NEW ROMAN", 20,"bold"),command=agegender).grid(row=3,column=4,padx=20,pady=100)
#Button(root, text='EXIT',bg="light green",font=("TIMES NEW ROMAN", 20,"bold")).grid(row=4,column=3,padx=30,pady=50)
    root.mainloop()#this will make window whwnever we want to keep window
# Designing popup for login success
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("SUCCESS")
    login_success_screen.geometry("450x250")
    Label(login_success_screen, text="LOGIN SUCCESS",bg="grey",font=("TIMES NEW ROMAN",15,"bold")).pack
    Button(login_success_screen, text="OK",bg="light blue",command=imagewebcam).pack()

# implementing event on login success
# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("SUCCESS")
    password_not_recog_screen.geometry("250x200")
    Label(password_not_recog_screen, text="INVALID PASSWORD ",font=("TIMES NEW ROMAN",15,"bold")).pack()
    Button(password_not_recog_screen, text="OK", font=("TIMES NEW ROMAN",15,"bold"),command=delete_password_not_recognised).pack()

# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("SUCCESS")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="USER NOT FOUND",bg="light blue",font=("TIMES NEW ROMAN",15,"bold")).pack()
    Button(user_not_found_screen, text="OK",font=("TIMES NEW ROMAN",15,"bold"), command=delete_user_not_found_screen).pack()

# Deleting popups
def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

# Gender and Age Detection program
def agegender():
        def highlightFace(net, frame, conf_threshold=0.7):
            frameOpencvDnn = frame.copy()
            frameHeight = frameOpencvDnn.shape[0]
            frameWidth = frameOpencvDnn.shape[1]
            blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], False, False)  # first false was true
            net.setInput(blob)
            detections = net.forward()
            faceBoxes = []
            for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > conf_threshold:
                    x1 = int(detections[0, 0, i, 3] * frameWidth)
                    y1 = int(detections[0, 0, i, 4] * frameHeight)
                    x2 = int(detections[0, 0, i, 5] * frameWidth)
                    y2 = int(detections[0, 0, i, 6] * frameHeight)
                    faceBoxes.append([x1, y1, x2, y2])
                    cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 150)), 8)
            return frameOpencvDnn, faceBoxes
        parser = argparse.ArgumentParser()
        parser.add_argument('--image')
        args = parser.parse_args()
        faceProto = "opencv_face_detector.pbtxt"
        faceModel = "opencv_face_detector_uint8.pb"
        ageProto = "age_deploy.prototxt"
        ageModel = "age_net.caffemodel"
        genderProto = "gender_deploy.prototxt"
        genderModel = "gender_net.caffemodel"
        MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
        ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(21-28)', '(30-40)', '(42-50)', '(60-100)']
        genderList = ['MALE', 'FEMALE']
        faceNet = cv2.dnn.readNet(faceModel, faceProto)
        ageNet = cv2.dnn.readNet(ageModel, ageProto)
        genderNet = cv2.dnn.readNet(genderModel, genderProto)
        video = cv2.VideoCapture(args.image if args.image else 0)
        padding = 20
        while cv2.waitKey(1) < 0:
            hasFrame, frame = video.read()
            if not hasFrame:
                cv2.waitKey()
                break
            resultImg, faceBoxes = highlightFace(faceNet, frame)
            if not faceBoxes:
                print("NO FACE DETECTED")
            for faceBox in faceBoxes:
                face = frame[max(0, faceBox[1] - padding):
                             min(faceBox[3] + padding, frame.shape[0] - 1), max(0, faceBox[0] - padding)
                                                                            :min(faceBox[2] + padding, frame.shape[1] - 1)]
                blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
                genderNet.setInput(blob)
                genderPreds = genderNet.forward()
                gender = genderList[genderPreds[0].argmax()]
                print(f'Gender: {gender}')
                ageNet.setInput(blob)
                agePreds = ageNet.forward()
                age = ageList[agePreds[0].argmax()]
                print(f'Age: {age[1:-1]} years')
                cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                            (0, 255, 255), 2, cv2.LINE_AA)
                cv2.imshow("Detecting age and gender", resultImg)

# url of the video to predict Age and gender
def youtube():
                url = 'https://www.youtube.com/watch?v=Lum-D1dK4YY&t=54s&feature=youtu.be'
                vPafy = pafy.new(url)
                play = vPafy.getbest(preftype="mp4")
                cap = cv2.VideoCapture(play.url)
                cap.set(3, 480)  # set width of the frame
                cap.set(4, 640)  # set height of the frame
                MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
                age_list = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)', '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']
                gender_list = ['Male', 'Female']
                age_net = cv2.dnn.readNetFromCaffe('age_deploy.prototxt', 'age_net.caffemodel')
                gender_net = cv2.dnn.readNetFromCaffe('gender_deploy.prototxt', 'gender_net.caffemodel')
                def load_caffe_models():
                    age_net = cv2.dnn.readNetFromCaffe('age_deploy.prototxt', 'age_net.caffemodel')
                    gender_net = cv2.dnn.readNetFromCaffe('gender_deploy.prototxt', 'gender_net.caffemodel')
                    return (age_net, gender_net)
                def video_detector(age_net, gender_net):
                    font = cv2.FONT_HERSHEY_SIMPLEX
                while True:
                    ret, image = cap.read()
                    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
                    if (len(faces) > 0):
                        print("Found {} faces".format(str(len(faces))))
                    for (x, y, w, h) in faces:
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
# Get Face
                        face_img = image[y:y + h, h:h + w].copy()
                        blob = cv2.dnn.blobFromImage(face_img, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
                        load_caffe_models()
# Predict Gender
                        gender_net.setInput(blob)
                        gender_preds = gender_net.forward()
                        gender = gender_list[gender_preds[0].argmax()]
                        print("GENDER : " + gender)
# Predict Age
                        age_net.setInput(blob)
                        age_preds = age_net.forward()
                        age = age_list[age_preds[0].argmax()]
                        print("AGE RANGE: " + age)
                        overlay_text = "%s %s" % (gender, age)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.putText(image, overlay_text, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
                        cv2.imshow('frame', image)
                        
# 0xFF is a hexadecimal constant which is 11111111 in binary.
                        if cv2.waitKey(1) & 0xFF == ord('q'): break
                        if __name__ == "__main__":
                            age_net, gender_net = load_caffe_models()
                        video_detector(age_net, gender_net)

# Designing Main(first) window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1000x700")
    main_screen.title("ACCOUNT LOGIN")
    Label(text="  WELCOME TO AGE AND GENDER PREDICTION  ", bg="grey",relief=GROOVE, font=("TIMES NEW ROMAN", 25,"bold")).pack(padx=10,pady=10)
    Label(text="PLEASE REGISTER BEFORE FIRST TIME LOGIN",bg="black",fg="white",font=("TIMES NEW ROMAN" ,15),width="40",height="2").pack(padx=10,pady=50)
    Button(text="LOGIN", height="2", width="30", bg="light blue",font=("TIMES NEW ROMAN" ,15,"bold"),command = login).pack(padx=20,pady=30)
    Label(text="").pack()
    Button(text="REGISTER", height="2", width="30",bg="light blue",font=("TIMES NEW ROMAN" ,15,"bold"), command=register).pack()
    main_screen.mainloop()
main_account_screen()

