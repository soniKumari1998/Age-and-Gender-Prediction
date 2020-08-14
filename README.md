# Age-and-Gender-Prediction
Automatic age and gender prediction using python
Gender-and-Age-Detection
Objective :
It is the GUI based project which is used To build a gender and age detector that can approximately guess the gender and age of the person (face) in a picture or through webcam and through Youtube url.


About the Project :
In this Python Project, I had used Deep Learning to accurately identify the gender and age of a person.The predicted gender may be one of ‘Male’ and ‘Female’, and the predicted age may be one of the following ranges- (0 – 2), (4 – 6), (8 – 12), (15 – 20), (25 – 32), (38 – 43), (48 – 53), (60 – 100) (8 nodes in the final softmax layer). It is very difficult to accurately guess an exact age because of factors like makeup, lighting, obstructions, and facial expressions.


Dataset :
For this python project, I had used the Adience dataset; the dataset is available in the public domain and you can find it here. This dataset serves as a benchmark for face photos and is inclusive of various real-world imaging conditions like noise, lighting, pose, and appearance. The images have been collected from Flickr albums and distributed under the Creative Commons (CC) license. It has a total of 26,580 photos of 2,284 subjects in eight age ranges (as mentioned above) and is about 1GB in size. The models I used had been trained on this dataset.


Additional Python Libraries Required :
OpenCV
   pip install opencv-python
argparse
   pip install argparse
youtube-dl
   pip install youtube-dl
tensorflow
   pip install tensorflow
pafy
   pip install pafy

The contents of this Project :
opencv_face_detector.pbtxt
opencv_face_detector_uint8.pb
age_deploy.prototxt
age_net.caffemodel
gender_deploy.prototxt
gender_net.caffemodel
haarcascade_frontalface_alt.xml
_config.yml
a few pictures to try the project on
try.py
For face detection, we have a .pb file- this is a protobuf file (protocol buffer); it holds the graph definition and the trained weights of the model. We can use this to run the trained model. And while a .pb file holds the protobuf in binary format, one with the .pbtxt extension holds it in text format. These are TensorFlow files. For age and gender, the .prototxt files describe the network configuration and the .caffemodel file defines the internal states of the parameters of the layers.


Usage :
Download my Repository
Open your Command Prompt or Terminal and change directory to the folder where all the files are present.
Detecting Gender and Age of face in Image Use Command :
  python try.py --image <image_name>
Note: The Image should be present in same folder where all the files are present

Opening the Home Panel , Use Command :
  python try.py
Press Ctrl + C to stop the program execution.

