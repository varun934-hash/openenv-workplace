---
title: Workplace Decision Engine
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---
# 🏢 Workplace Decision Engine (OpenEnv)

## 🚀 Overview
This project simulates a real-world workplace where an AI agent processes incoming tasks (emails), prioritizes them, and takes appropriate actions.

---

## 🔁 Workflow
Email → Task → Priority → Action → Response → Reward → Score

---

## 🎯 Tasks
- Easy: Basic request handling
- Medium: Scheduling tasks
- Hard: High-priority issue resolution

---

## ⚙️ Action Space
- complete
- schedule
- escalate
- respond

---

## 👁️ Observation Space
List of tasks with:
- description
- priority
- status

---

## 💰 Reward Design
- High priority completion → high reward
- Wrong action → penalty
- Pending tasks → penalty

---

## 📊 Baseline Performance
Final Score: **1.0**

---

## 🧠 Key Features
- Real-world simulation
- AI + fallback system
- Dynamic task generation
- Robust reward system

---

## 🛠️ Run
```bash
docker build -t openenv .
docker run openenv