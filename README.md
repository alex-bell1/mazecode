
# 🕹️ Two-Player Maze Race Game (Pygame)

A **two-player competitive maze game** built with **Python and Pygame**. Two players race through a maze filled with obstacles. The goal is to reach the finish area in the **shortest time possible**.

---

## 🎮 Game Overview

* Two players move simultaneously on the same map
* Each player has independent controls
* Moving obstacles change size and position over time
* Collision detection prevents players from passing through walls
* Timers track how long each player takes to reach the finish

---

## 🧍 Player Controls

### Player 1

* **W** – Move up
* **S** – Move down
* **A** – Move left
* **D** – Move right

### Player 2

* **↑ Arrow** – Move up
* **↓ Arrow** – Move down
* **← Arrow** – Move left
* **→ Arrow** – Move right

---

## ⏱️ Timer System

* Each player has an individual timer
* The timer starts when the game begins
* When a player reaches the finish square, their time is recorded
* Players are reset after reaching the finish

---

## 🧱 Obstacles & Map

* Static walls block player movement
* Animated obstacles change size using **multithreading**
* Collision detection ensures fair gameplay
* Players cannot pass through obstacles or walls

---

## 🛠️ Requirements

* Python 3.x
* Pygame

Install Pygame with:

```bash
pip install pygame
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/pygame-maze-race.git
```

2. Navigate to the project folder:

```bash
cd pygame-maze-race
```

3. Make sure the image files are in the same directory:

* `player1-removebg-preview (1).png`
* `player2-removebg-preview.png`

4. Run the game:

```bash
python main.py
```

---

## 🖼️ Assets

* Player sprites loaded as PNG images
* Images are scaled smoothly for better visuals

---

## 🚀 Future Improvements

* Add a win screen
* Add sound effects
* Add AI player mode
* Improve obstacle randomness
* Add a restart button

---

## 📚 Learning Objectives

This project is great for learning:

* Pygame basics
* Game loops and events
* Collision detection
* Multithreading in games
* Timers and performance tracking

---

## 📜 License

This project is open-source and intended for educational use.

---

⭐ If you enjoy this project, feel free to star the repository!
