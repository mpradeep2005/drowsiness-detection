Drowsiness Detection System

Overview

This project is a real-time drowsiness detection system that monitors eye activity using a webcam and alerts the user when signs of fatigue are detected. The system can be used to improve safety, especially in situations where staying alert is critical, such as driving or operating machinery.

Features

Real-time face and eye detection.

Eye blink and drowsiness analysis using facial landmarks.

Visual feedback indicating the user’s state: Active, Drowsy, or Sleeping.

Buzzer alert to wake the user if they are detected as "Sleeping."

Technologies Used

Python: For implementing the logic and detection algorithms.

OpenCV: For video capture and image processing.

Dlib: For face detection and facial landmark detection.

NumPy: For numerical computations.

Pillow: To display the video feed in the GUI.

Tkinter: For building the graphical user interface.

Playsound: For playing alert sounds.

How It Works

Face Detection: Detects the user's face using Dlib’s pre-trained model.

Eye Aspect Ratio (EAR): Measures eye openness by calculating the aspect ratio of key facial landmarks.

State Classification:

Active: Eyes are open and blinking normally.

Drowsy: Eyes are slightly closed or blinking more slowly.

Sleeping: Eyes remain closed for an extended period (over 7 seconds).

Audio Alert: If the user is in the "Sleeping" state for too long, a buzzer sound is triggered.

Setup Instructions

Clone the Repository:

git clone https://github.com/YOUR-USERNAME/drowsiness-detection.git
cd drowsiness-detection

Install Dependencies: Ensure Python 3.x is installed, then run:

pip install opencv-python numpy dlib imutils playsound pillow

Download the Pre-Trained Model: Download the shape_predictor_68_face_landmarks.dat file from dlib's GitHub repository, extract it, and place it in the project directory.

Run the Project: Start the application with:

python drowsiness_detection.py

Usage

Open the application.

The webcam feed will start displaying in the GUI.

The system monitors the user’s eye activity and updates the status as "Active," "Drowsy," or "Sleeping."

If "Sleeping" is detected for over 7 seconds, a buzzer sound will play.

Project Structure

Drowsiness Detection/
│
├── drowsiness_detection.py         # Main script
├── buzzer.mp3                      # Audio alert file
├── shape_predictor_face_landmarks.dat  # Pre-trained model for face and eye landmarks
└── README.md                       # Project documentation

Applications

Driver Safety: Detect drowsiness in drivers to prevent accidents.

Workplace Monitoring: Improve worker alertness in critical environments.

Personal Alertness: Help individuals stay alert and focused during long tasks.

Future Enhancements

Add yawning detection for better accuracy.

Integrate deep learning models for advanced drowsiness prediction.

Develop a mobile-friendly version of the application.

Provide multilingual support for international users.

License
