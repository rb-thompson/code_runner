# CODE RUNNER

## Project Overview
- **Game Title**: "Code Runner"
- **Objective**: Navigate a coder avatar through a course filled with obstacles and rewards, with increasing difficulty.


## Phase 1: Planning and Design

**Tasks**:
- **Concept Sketching**: 
    - Sketch out all of the game layout, obstacles, and rewards. Use tools like Adobe XD or Figma.
- **Game Mechanics**: 
    - Define mechanics for movement, collision detection, scoring, and life management.
    - Plan how difficulty increases over time (e.g., more obstacles, faster movement)
- **User Interface (UI) Design**:
    - Design the start menu, game over screen, and high score display.
- **DB Design**: 
    - Decide on a simple SQLite database for storing high scores.

**Resources Needed**:
- Design software.
- A basic understanding of game design principles.

## Phase 2: Development Setup

**Tasks**:
- **Choose Game Engine/Framework**:
    - Pygame for Python due to its simplicity for 2D games.
- **Environment Setup**:
    - Pythono 3.12.1, Pygame 2.6.1, SQLite 3.
- **Version Control**:
    - Hosted on GitHub.

## Phase 3: Core Game Development

**Tasks**:
- **Character and Asset Creation**:
    - Design or source sprite images for the coder avatar, obstacles, and rewards.
- **Game Logic**:
    - Implement movement, obstacle generation, collision detection.
    - Deelop reward mechanics (coffee, likes, coins, experience).
- **Difficulty Scaling**:
    - Code algorithms to increase game speed and obstacle frequency.

**Resources Needed**:
- Image editing software for custom sprites (GIMP or Photoshop)
- Python/Pygame documentation.

## Phase 4: Database Integration

**Tasks**:
- **Database Setup**: 
    - Create a SQLite database to log high scores
- **Database Operations**:
    - Write functions to insert, retrieve, and display high scores.

**Resources**:
- SQLite documentation or a Python SQLite tutorial.

## Phase 5: UI and User Experience

**Tasks**:
- **Menu Screens**:
    - Implement start menu, pause menu, and game over screen with high scores display.
- **User Feedback**:
    - Add sound effects for actions like collecting rewards or hitting obstacles. (Audacity for sound editing).

**Resources**:
- Sound creation or editing tools like Audacity.

## Phase 6: Testing

**Tasks**:
- **Unit Testing**: 
    - Test individual components like collision detection, scoring, etc.
- **Play Testing**:
    - Conduct sessions with friends or online communities for feedback.
    - Iterate based on feedback for bug fixes and gameplay balance.

**Resources**:
- Beta testers or gaming communities.

## Phase 7: Deployment

**Tasks**:
- **Packaging**: 
    - Create an executable for Windows or a setup for other platforms if needed.
- **Documentation**: 
    - Write a README with installation instructions, controls, and game objectives.
- **Distribution**:
    - Host on GitHub for open-source or platforms like itch.io for distribution.

**Resources**:
- PyInstaller for creating standalone executables.

## Phase 8: Maintenance and Updates

**Tasks**: 
- **Bug Fixes**:
    - Address any bugs reported by players.
- **Feature Updates**:
    - Add new levels, obstacles, or rewards based on player feedback.

**Resources**:
- Continuous feedback from the player base.

## Additional Considerations

- **Legal**: Ensure all assets used are either original, free to use, or properly licensed.
- **Community**: Engage with coding or gaming communities for support and feedback.

## Progress

**PHASE 1: PLANNING & DESIGN**
- [x] Concept sketching
- [x] Game mechanics definitions
- [x] UI design
- [x] Database design

**PHASE 2: DEV SETUP**
- [x] Python and Pygame installation 
- [x] Project structure setup
- [x] Version control setup

**PHASE 3: CORE GAME DEV**
- [x] Main menu implementation
- [x] Player avatar placeholder (fixed position)
- [x] Ground place added (dark mode theme)
- [x] Basic game loop with state management (menu to game)
- [x] Error handling and logging integration
- [x] Player movement mechanics
- [ ] Obstacle implementation
- [ ] Reward system
- [ ] Difficulty scaling
- [ ] Collision detection
- [ ] Game over condition

**PHASE 4: DB INTEGRATION**
- [ ] SQLite setup
- [ ] High score saving mechanism
- [ ] High score retrieval and display

**PHASE 5: UI & UX**
- [ ] Main menu screen
- [ ] Game screen UI (health, experience, coins, score)
- [ ] Game over screen
- [ ] Sound effects

**PHASE 6: TESTING**
- [ ] Unit testing of game components
- [ ] Play testing sessions
- [ ] Feedback implementation

**PHASE 7: DEPLOY**
- [ ] Game packaging
- [ ] Ducumentation creation
- [ ] Distribution setup (GitHub, itch.io, etc)

**PHASE 8: MAINT. & UPDATES**
- [ ] Bug fixes
- [ ] Features updates