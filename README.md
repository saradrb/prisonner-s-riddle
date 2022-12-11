# 100 Prisoner Problem Simulation

## Project Members
- Hugo Moulard
- Sara Dorbane
- Céline Ye

## Content
This project contains some programs that can help simulate the 100 prisoner problem:
- a detailed simulation of the random strategy
- a detailed simulation of the follow strategy
- a detailed simulation of the baby-step giant-step strategy
- the possibility to create a histogram
- the possibility, for the follow strategy, to create a permutation graph
- a graphical interface looping a strategy and showing its probability of success in real time

## Installation
This project requires python3 and some of its downlable packages.

If it isn't present, install `pip`, the python package installer.
```bash
sudo apt-get update
sudo apt-get install python3-pip
```

Then run the following commands to install the needed packages.
```bash
sudo apt-get install python3-pandas
pip install networkx 
pip install seaborn
pip install matplotlib
```

## Launch
Launch the project with the following command:
```bash
python3 main.py
```