# Donkey Kong – Python & Pygame

A recreation of **Donkey Kong (1981)**, the classic arcade platformer originally developed by Nintendo. Built using Python and Pygame, this project recreates the original game's platforming mechanics, level design, character movement, and obstacles.

## About the Game

Donkey Kong is a classic arcade platform game in which the player controls Jumpman (later known as Mario), who must climb a series of platforms to rescue Pauline from Donkey Kong.

The original game features vertically structured levels consisting of platforms, ladders, gaps, and various obstacles. Players must navigate these environments while avoiding barrels and other hazards thrown by Donkey Kong.

The objective is to reach the top of each level, overcome obstacles, and rescue Pauline.

This project recreates the core gameplay experience of the original arcade title using Python and Pygame.

## Gameplay Features

- **Platform Navigation:** Move across vertically arranged platforms.
- **Ladder Climbing:** Navigate between different platform levels using ladders.
- **Jump Mechanics:** Jump over obstacles and incoming hazards.
- **Barrel Obstacles:** Avoid barrels rolling across platforms.
- **Collision Detection:** Handle interactions between the player, platforms, ladders, and obstacles.
- **Character Animation:** Sprite-based character movement and animations.
- **Score Tracking:** Track gameplay performance and progress.
- **Arcade Gameplay:** Recreate the mechanics and challenge of the original Donkey Kong.

## Controls

| Key | Action |
|---|---|
| Left Arrow / A | Move Left |
| Right Arrow / D | Move Right |
| Up Arrow / W | Climb Up |
| Down Arrow / S | Climb Down |
| Space | Jump |
| ESC | Quit Game |

*Controls depend on the current implementation.*

## Technology Stack

- **Programming Language:** Python
- **Game Framework:** Pygame
- **Graphics:** 2D Sprite Rendering
- **Animation:** Frame-based Sprite Animation
- **Game Mechanics:** Collision Detection, Platform Physics, and Event Handling

## Project Structure

```text
DonkeyKong/
│
├── assets/
│   ├── player/
│   ├── enemies/
│   ├── platforms/
│   ├── backgrounds/
│   └── sounds/
│
├── main.py
├── player.py
├── enemy.py
├── platform.py
├── settings.py
├── requirements.txt
└── README.md
```
...
## Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/StezX433/DonkeyKong_Ac.git
cd DonkeyKong
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Alternatively, install Pygame directly:

```bash
pip install pygame
```

### 3. Run the Game

```bash
python main.py
```

## Core Concepts

The project involves implementing several fundamental game development concepts:

- Object-Oriented Programming
- Game Loop Architecture
- Sprite Management and Animation
- 2D Coordinate Systems
- Collision Detection and Response
- Platform Movement and Physics
- Keyboard Input and Event Handling
- Game State Management
- Real-Time Rendering

## Project Objective

The objective of this project is to recreate the gameplay experience of one of the most influential arcade games in video game history while exploring the fundamentals of 2D game development.

By implementing the original game's mechanics using Python and Pygame, the project demonstrates practical applications of object-oriented programming, game physics, animation, and interactive system design.

---

**Developed using Python and Pygame.**