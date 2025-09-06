
# 🚀 Drowsiness Detection System

## 📌 Overview
This project is a real-time **drowsiness detection system** that monitors eye activity using a webcam and alerts the user when signs of fatigue are detected. It enhances safety in critical situations such as **driving** or **operating machinery**.

---

## ⚡ Features
✅ **Real-time** face and eye detection  
✅ **Eye blink** and drowsiness analysis using facial landmarks  
✅ **Visual feedback**: "Active," "Drowsy," or "Sleeping" state  
✅ **Buzzer alert** if the user is detected as "Sleeping"  

---

## 🛠 Technologies Used
<p align="left">
  <img height="50" width="50" src="https://img.icons8.com/color/48/000000/python.png"/>
  <img height="50" width="50" src="https://img.icons8.com/color/48/000000/opencv.png"/>
  <img height="50" width="50" src="https://img.icons8.com/color/48/000000/numpy.png"/>
  <img height="50" width="50" src="https://img.icons8.com/?size=100&id=54023&format=png&color=000000"/>
</p>

- **Python**: Core logic and detection algorithms  
- **OpenCV**: Video capture and image processing  
- **Dlib**: Face and facial landmark detection  
- **NumPy**: Numerical computations  
- **Pillow**: GUI video feed display  
- **Tkinter**: Graphical user interface  
- **Playsound**: Alert sounds  

---

## 🔍 How It Works
📸 **Face Detection**: Detects the user's face using Dlib’s pre-trained model.  
👀 **Eye Aspect Ratio (EAR)**: Measures eye openness using key facial landmarks.  
⚡ **State Classification:**
  - **Active**: Eyes are open and blinking normally.
  - **Drowsy**: Eyes are slightly closed or blinking slowly.
  - **Sleeping**: Eyes remain closed for **over 7 seconds**.
🔊 **Audio Alert**: A buzzer sound is triggered if the user remains "Sleeping".

---

## ⚙️ Setup Instructions
**1️⃣ Install Dependencies:**
```bash
pip install opencv-python numpy dlib imutils playsound pillow
```

**2️⃣ Download Pre-Trained Model:**
- Download `shape_predictor_68_face_landmarks.dat` from [Dlib’s GitHub](http://dlib.net/) and place it in the project directory.

**3️⃣ Run the Project:**
```bash
python drowsiness_detection.py
```

---

## 📌 Usage Guide
1️⃣ Open the application.  
2️⃣ The **webcam feed** will display in the GUI.  
3️⃣ The system monitors eye activity and updates the state: **"Active," "Drowsy," or "Sleeping"**.  
4️⃣ If "Sleeping" is detected for **over 7 seconds**, an alert will sound.  

---

## 📂 Project Structure
```
Drowsiness Detection/
│
├── drowsiness_detection.py         # Main script
├── buzzer.mp3                      # Audio alert file
├── shape_predictor_68_face_landmarks.dat  # Pre-trained model
└── README.md                       # Project documentation
```

---

## 🚗 Applications
🔹 **Driver Safety**: Prevent drowsy driving accidents.  
🔹 **Workplace Monitoring**: Improve worker alertness in critical environments.  
🔹 **Personal Alertness**: Help individuals stay focused during long tasks.  

---

## 🔮 Future Enhancements
🔹 **Yawning detection** for better accuracy.  
🔹 **Deep learning models** for advanced drowsiness prediction.  
🔹 **Mobile-friendly version** of the application.  
🔹 **Multilingual support** for international users.  

---

## 📜 License
This project is available for **personal or educational use**. Feel free to customize or extend it! 🚀

---

### 🏆 Connect with Me!
<p>
  <a href="https://www.linkedin.com/in/pradeep-m-43aa2427a/">
    <img height="30" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
</p>

🔥 **Stay Alert, Stay Safe!** 🚀
