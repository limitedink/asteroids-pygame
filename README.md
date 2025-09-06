# Asteroids Game

A modern implementation of the classic Asteroids arcade game built with Python and Pygame, featuring object-oriented design, real-time physics simulation, and advanced collision detection systems.

## 🎮 Features

- **Player Movement System**: Smooth rotation and thrust mechanics with momentum-based physics
- **Dynamic Shooting Mechanics**: Projectile system with cooldown timers and directional firing
- **Asteroid Physics**: Realistic asteroid movement with velocity vectors and collision boundaries
- **Advanced Splitting Algorithm**: Multi-stage asteroid fragmentation with randomized trajectories
- **Real-time Collision Detection**: Efficient circle-based collision system between all game objects
- **Sprite Management**: Organized sprite groups for optimized rendering and updates
- **Game Loop Architecture**: 60 FPS game loop with delta time calculations

## 🕹️ Controls

- **W**: Thrust forward
- **A/S**: Rotate left/right  
- **R**: Thrust backward
- **Spacebar**: Fire bullets

## 🛠️ Technical Implementation

### Architecture
- **Object-Oriented Design**: Modular class hierarchy with `CircleShape` base class
- **Component System**: Separate classes for Player, Asteroid, Shot, and AsteroidField
- **Event-Driven Programming**: Real-time input handling and collision responses

### Key Components
- `CircleShape`: Base class providing collision detection and sprite management
- `Player`: Handles movement, rotation, and shooting mechanics
- `Asteroid`: Implements physics simulation and splitting algorithms  
- `Shot`: Projectile system with velocity calculations
- `AsteroidField`: Procedural asteroid generation and spawning system

### Physics & Mathematics
- Vector-based movement and rotation calculations
- Dynamic velocity scaling and directional transforms
- Randomized splitting angles (20-50 degrees) with momentum conservation
- Real-time position updates using delta time calculations

## 🚀 Installation & Setup

### Prerequisites
- Python 3.11+
- UV package manager (recommended) or pip

### Quick Start
```bash
# Clone the repository
git clone https://github.com/limitedink/asteroids-pygame.git
cd asteroids-pygame

# Install dependencies
uv sync

# Run the game
uv run main.py
```

### Alternative Installation
```bash
# Using pip
pip install pygame==2.6.1
python main.py
```

## 🎯 Gameplay Mechanics

1. **Asteroid Destruction**: Shooting asteroids splits them into smaller fragments
   - Large → Medium (2 pieces)
   - Medium → Small (2 pieces)  
   - Small → Destroyed
2. **Player Collision**: Contact with asteroids results in game over
3. **Continuous Spawning**: New asteroids spawn from screen edges at regular intervals
4. **Physics Simulation**: All objects maintain realistic momentum and trajectories

## 🔧 Development Skills Demonstrated

- **Game Development**: Real-time systems, game loops, and state management
- **Object-Oriented Programming**: Inheritance, polymorphism, and encapsulation
- **Mathematical Programming**: Vector mathematics, collision detection, physics simulation
- **Python Proficiency**: Modern Python practices, package management, and code organization
- **Problem Solving**: Algorithm design for complex game mechanics and interactions

## 📁 Project Structure

```
asteroids-pygame/
├── main.py              # Game loop and initialization
├── player.py            # Player class with movement and shooting
├── asteroid.py          # Asteroid physics and splitting logic
├── asteroidfield.py     # Asteroid spawning system
├── circleshape.py       # Base class with collision detection
├── constants.py         # Game configuration and constants
└── pyproject.toml       # Project dependencies
```

## 🎨 Future Enhancements

- Score tracking and high score persistence
- Power-ups and weapon upgrades
- Sound effects and background music
- Multiple difficulty levels
- Particle effects for explosions
- Menu system and pause functionality

---

*This project was developed to demonstrate proficiency in Python programming, game development concepts, and object-oriented design principles.*
