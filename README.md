# Hand-Gestures-Control-Over-Presentation-
AI-based hand gesture recognition system to control presentation slides using a webcam. Detects gestures in real time with Computer Vision and Machine Learning, enabling touchless navigation for seamless, interactive presentations without extra devices like clickers or gloves.

---

## 🚀 Features
- **Touchless Slide Control** – Navigate presentations with hand gestures.
- **Real-Time Gesture Detection** – Powered by OpenCV and Mediapipe.
- **Markerless Operation** – No gloves, sensors, or external devices needed.
- **Bidirectional Navigation** – Move forward and backward through slides.
- **Cross-Platform** – Works on Windows, macOS, and Linux.
- **Lightweight & Efficient** – Runs smoothly on standard laptops.

---

## 🛠 Tech Stack

**Programming Language:**  
- Python

**Libraries & Tools:**  
- OpenCV – Image processing & real-time video capture  
- Mediapipe – Hand tracking and landmark detection  
- PyAutoGUI – Simulate keyboard controls  
- NumPy – Numerical computations  
- Webcam / Laptop Camera  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/hand-gesture-presentation-control.git
cd hand-gesture-presentation-control

---
2️⃣ Create & Activate Virtual Environment
bash
Copy
Edit
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

---

3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
(If requirements.txt is missing, install manually and create it:)

bash
Copy
Edit
pip install opencv-python mediapipe pyautogui numpy
pip freeze > requirements.txt
4️⃣ Run the Application
bash
Copy
Edit
python main.py
