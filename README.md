# AQUILA-1 – UAV Mission Health Scoring Engine

> **Domain:** UAV Telemetry / Mission Health / Risk Assessment  
> **Level:** Prototype (Student R&D)  
> **Purpose:** Demonstrate a simplified mission health evaluation based on basic telemetry-like inputs

---

## 1. Background & Concept
Autonomous UAV operations require continuous evaluation of mission conditions, reliability of telemetry and flight safety.  
This prototype models a minimal “mission health score” using basic parameters that affect UAV safety and mission feasibility.

The goal is not to simulate a full control system, but to show how decision logic and risk scoring can be derived from telemetry-style data.

---

## 2. What AQUILA-1 Does
The system collects 8 parameters:

- Battery level  
- GPS signal quality  
- Wind intensity  
- Temperature  
- Route stability  
- Motor temperature  
- Altitude accuracy  
- Speed stability  

Each value contributes to a numerical score (0–90). The final mission status is classified as:

- **SAFE** (70+)  
- **RISKY** (40–69)  
- **CRITICAL** (<40)

This represents a minimal example of risk-based mission assessment.

---

## 3. Why This Project Exists
AQUILA-1 was originally written as a beginner Python project.  
However, the idea behind it—**mission health reasoning**—is directly related to UAV safety, telemetry interpretation and autonomous decision processes.

This makes it relevant even as a small beginner prototype.

---

## 4. Technologies Used
- Python (basic)  
- Conditional logic  
- Manual input simulation  
- Terminal output  

No external libraries, no OOP — intentionally simple for learning purposes.

---

## 5. Architecture

- Input: User-provided mission parameters  
- Scoring: Simple rule-based evaluation  
- Output: Mission health classification  

---

## 6. Example Use
```bash
python aquila.py
