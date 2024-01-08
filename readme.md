# Tetris-Ornament  

A lightweight implementation of tetris designed to be displayed on a small led matrix and ran on a raspberry pi. A genetic algorithm will run showing each generations best attempt in real time, making the ornament slowly better at playing tetris. 

## Heuristics

1. Penalise large tower height
2. Penalise gaps
3. Promote high score ( by association high scores should reflect multi-line elimination and duration of run )