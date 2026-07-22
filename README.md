# 📸 SnapClass – Intelligent AI Attendance System

An AI-powered attendance management system that automates student attendance using **Facial Recognition** and **Voice Recognition** technologies. SnapClass eliminates manual attendance, improves accuracy, and provides a secure, user-friendly platform for teachers and administrators.

---

# 🌐 Live Demo

🚀 Try SnapClass here:
https://snapclass-intelligent-ai-attendance.streamlit.app/

🛬 SnapClass Landing Page:
snap-class-landing-page-ndyxxh3sx-princy-jain.vercel.app

# 🚀 Features

## 👨‍🏫 Teacher Authentication

- Secure teacher registration and login
- Password hashing using **bcrypt**
- Authentication with **Supabase**
- Secure session management

## 📚 Subject Management

- Create and manage subjects
- Generate **QR codes** for student enrollment
- Generate **shareable enrollment links**
- Edit and delete subjects
- View enrolled students for each subject

## 👤 Student Management

- Register new students with facial images
- Enroll in subjects using **QR codes** or **enrollment links**
- Securely store student information and facial embeddings

## 🤖 AI-Based Face Recognition

- Detect faces using **dlib**
- Generate **128-dimensional facial embeddings**
- Recognize multiple students simultaneously
- High-accuracy face matching using **Support Vector Machine (SVM)**

## 🎤 Voice Recognition

- Voice-assisted attendance workflow
- Supports voice commands during attendance

## 📸 Attendance System

- Capture classroom images for attendance
- Automatically recognize enrolled students
- Allow teachers to manually mark attendance when required
- Prevent duplicate attendance entries
- Date and time-stamped attendance records

## 📊 Teacher Dashboard

- View attendance by subject
- Mark and update attendance
- View attendance history
- Manage subjects
- Track enrolled students
- Export attendance records

## ☁️ Cloud Database

Securely stores:

- Teacher information
- Student details
- Subject information
- Enrollment records
- Attendance records
- Facial embeddings

---

# 🛠️ Tech Stack

## Frontend

- Streamlit
- HTML
- CSS

## Backend

- Python

## Database

- Supabase

## AI & Machine Learning

- dlib
- face_recognition_models
- Scikit-learn (SVM)
- NumPy
- Pandas

## Security

- bcrypt

## Deployment

- Streamlit

---

# 📷 How It Works

1. Teachers register and securely log in.
2. Teachers create subjects and generate **QR codes** or **enrollment links**.
3. Students enroll in subjects by scanning the QR code or opening the enrollment link.
4. Students register their facial data, and **128-dimensional face embeddings** are generated and stored securely.
5. During attendance, the teacher captures a classroom image.
6. The system detects faces, generates facial embeddings, and matches them against enrolled students.
7. Attendance is automatically marked and stored in the database.
8. Teachers can review, update, and manage attendance records through the dashboard.

---

# 🧠 AI Workflow

```text
Live Camera
      │
      ▼
Face Detection
      │
      ▼
Face Encoding
(dlib)
      │
      ▼
Feature Matching
      │
      ▼
Identity Prediction
      │
      ▼
Attendance Stored
(Supabase)
```

---

# 🔒 Security Features

- Secure password hashing using **bcrypt**
- Teacher authentication before accessing attendance records
- Secure cloud storage with **Supabase**
- Duplicate attendance prevention
- Protected facial embedding storage
- Subject-based access control

---

# 📈 Future Enhancements

- Face liveness detection
- Multi-classroom and institute support
- Attendance analytics and visualizations
- Email and SMS notifications
- Cloud deployment
- AI-powered attendance insights

---

# 👩‍💻 Author

**Princy Jain**

B.Tech – Computer Science and Engineering


---
