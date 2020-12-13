# Face Detection
Face detection is a computer vision technology that helps to locate/visualize human faces in digital images. This technique is a specific use case of object detection technology that deals with detecting instances of semantic objects of a certain class (such as humans, buildings or cars) in digital images and videos. With the advent of technology, face detection has gained a lot of importance especially in fields like photography, security, and marketing.

# Application
**• Facial recognition:** Face detection is used in biometrics, often as a part of (or together with) a facial recognition system. It is also used in video surveillance, human computer interface and image database management.

**• Photography:** Some recent digital cameras use face detection for autofocus.[6] Face detection is also useful for selecting regions of interest in photo slideshows that use a pan-and-scale Ken Burns effect. Modern appliances also use smile detection to take a photograph at an appropriate time.

**• Marketing:** Face detection is gaining the interest of marketers. A webcam can be integrated into a television and detect any face that walks by. The system then calculates the race, gender, and agerange of the face. Once the information is collected, a series of advertisements can be played that is specific toward the detected race/gender/age.

**• Emotional Inference:** Face detection can be used as part of a software implementation of emotional inference. Emotional inference can be used to help people with autism under stand the feelings of people around them.

**• Lip Reading:** Face detection is essential for the process of language inference from visual cues. Automated lip reading has applications to help computers determine who is speaking which is needed when security is important.

# Libraries and Files Used

## OpenCV

OpenCV was started at Intel in the year 1999 by Gary Bradsky. The first release came a little later in the year 2000. OpenCV essentially stands for Open Source Computer Vision Library. Although it is written in optimized C/C++, it has interfaces for Python and Java along with C++. OpenCV boasts of an active user base all over the world with its use increasing day by day due to the surge in computer vision applications.
OpenCV-Python is the python API for OpenCV. You can think of it as a python wrapper around the C++ implementation of OpenCV. OpenCV-Python is not only fast (since the background consists of code written in C/C++) but is also easy to code and deploy(due to the Python wrapper in foreground). This makes it a great choice to perform computationally intensive programs.

OpenCV uses machine learning algorithms to search for faces within a picture. Because faces are so complicated, there isn’t one simple test that will tell you if it found a face or not. Instead, there are thousands of small patterns and features that must be matched. The algorithms break the task of identifying the face into thousands of smaller, bite-sized tasks, each of which is easy to solve. These tasks are also called classifiers.
For something like a face, you might have 6,000 or more classifiers, all of which must match for a face to be detected (within error limits, of course). But therein lies the problem: for face detection, the algorithm starts at the top left of a picture and moves down across small blocks of data, looking at each block, constantly asking, “Is this a face? … Is this a face? … Is this a face?” Since there are 6,000 or more tests per block, you might have millions of calculations to do, which will grind your computer to a halt.

## Haarcascade frontalface default.xml

It is a Haarcascade Classifiers file.We will implement our use case using the Haar Cascade classifier. Haar Cascade classifier is an effective object detection approach which was proposed by Paul Viola and Michael Jones in their paper, “Rapid Object Detection using a Boosted Cascade of Simple Features” in 2001.
So, let’s try to understand what these Haar Cascade Classifiers are.This is basically a machine learning based approach where a cascade function is trained from a lot of images both positive and negative. Based on the training it is then used to detect the objects in the other images.So how this works is they are huge individual .xml files with a lot of feature sets and each xml corresponds to a very specific type of use case.

For Example, if you go to the github page of haarcascade you will see that there is a particular xml file containing the feature set to detect the full body, lower-body, eye, frontal-face and so on.

To understand how the haar cascade classifier work and how will that be used for computer vision

# Requirement-

- Python
- OpenCV

# STEPS TO RUN IT!

- Install python and OpenCV library
- Download the file and then unzip it.
- Run the face_dt file and for 3-4 second and the result is display.
