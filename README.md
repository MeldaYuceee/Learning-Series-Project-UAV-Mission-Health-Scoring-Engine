# 🛰️ AQUILA-1: UAV Mission Health Scoring Engine

**AQUILA-1** is a beginner-friendly but mission-driven Python project designed to simulate a simplified health-scoring mechanism for UAV (Unmanned Aerial Vehicle) missions.  
The system evaluates several telemetry-like parameters (battery, GPS quality, wind level, temperature, route stability, etc.) and produces an overall **Mission Health Score** along with a final status:

**SAFE — RISKY — CRITICAL**

Although the logic is simple, the concept reflects how real-world flight control and telemetry monitoring systems perform risk evaluation during autonomous missions.

---

## ✨ Why I Originally Built This Project

I created this project **months ago**, when I was just starting to learn Python.  
It was one of the first small systems I built to understand:

- how conditional logic works  
- how numerical scoring models can be designed  
- how telemetry-style decision systems operate in UAV missions  

At the time, it served as my personal **“entry point”** into both Python and mission-analysis thinking.

---

## 🔄 Why I Am Sharing It Now

I decided to publish this project **not because the code is complex**, but because:

### ✔ It reflects where my journey started  
Before advanced AI, UAV simulations, telemetry engines, or defense-tech projects…  
this simple scoring system was my first step into the field.

### ✔ It shows my learning progression clearly  
Recruiters, mentors, or colleagues can now see **how I evolved from basic scoring logic to more advanced autonomous-system work.**

### ✔ It still represents the core idea of mission safety evaluation  
Even though it’s a beginner project, the idea behind it is strongly connected to:

- mission health monitoring  
- risk evaluation  
- autonomous decision logic  
- telemetry reasoning  

These are all crucial in UAV and defense-oriented engineering.

### ✔ It completes my portfolio timeline  
Every engineer’s journey has a **baseline project** —  
**AQUILA-1 is mine.**

---

## 🧠 How the System Works

The system collects **8 UAV-related parameters**:

- Battery level  
- GPS signal quality  
- Wind intensity  
- Temperature  
- Route stability  
- Motor temperature  
- Altitude accuracy  
- Speed stability  

Each parameter contributes to a **total score (0–90)**.  
The mission status is then classified as:

- **SAFE** (70+)  
- **RISKY** (40–69)  
- **CRITICAL** (<40)  

The scoring rules are intentionally simple to keep the project accessible to beginners.

---

## 🧑‍💻 Technologies Used

- Python (basic level)  
- Conditional statements  
- Simple scoring logic  
- Terminal interaction via `input()`  

No external libraries, no OOP — just pure beginner-friendly Python.

---

## 🎯 Future Improvements

Although AQUILA-1 was meant as a starting point, it can be expanded into:

- Automatic parameter simulation  
- Visual mission dashboard  
- Real-time telemetry stream processing  
- Weighted scoring based on real UAV constraints  
- Exporting logs as CSV  
- Risk trend detection  

---

## 📝 Final Thoughts

AQUILA-1 is not a **big** project —  
it is a **foundation stone**.

It marks the moment where my journey into Python, telemetry logic, and UAV-driven engineering truly began.

Publishing it now is a way of saying:  
**“This is where I started. Here is how far I’ve come.”**
