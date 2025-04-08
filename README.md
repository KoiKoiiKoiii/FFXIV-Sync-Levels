# Job Pairing Algorithm

This project contains a Python script that generates optimal job pairings based on job levels and roles from a set of predefined data. The goal is to find the best non-overlapping pairs for jobs based on their role compatibility and level difference.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [How to Use](#how-to-use)

## Overview

The script compares different job pairings in a game (presumably Final Fantasy XIV based on job names). It calculates the best combinations of jobs such as "Tank" and "Healer" or "Melee DPS" with other roles, while considering the level differences to ensure balanced pairings. It then outputs a list of recommended job pairings, sorted by rank and level difference.

## Features

- **Optimal Pairing**: The script matches jobs of different roles (Tank, Healer, Melee, etc.) based on their level differences.
- **Sorting**: The pairings are sorted by rank and level difference, ensuring the best combinations are chosen first.
- **Non-overlapping Pairs**: The algorithm ensures that jobs are not paired more than once.
- **Customizable**: You can modify the list of jobs, their levels, and their roles in the script, making it flexible for future changes.

## Requirements

- Python 3.x
- Basic understanding of Python's data structures such as dictionaries, sets, and lists

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/job-pairing.git
    ```
2. Open the script in your preferred Python IDE or text editor.

3. Ensure the jobs, jobsTali, jobsKoi, and jobRoles dictionaries are correctly populated with the job data.

4. Run the script:
  ```bash
  python job_pairing.py
  ```
  The script will output the optimal job pairings based on the data.
  ## Example Output
    ```
    Koi PLD 80 + Tali WHM 80;
    Level difference of: 0

    Koi WAR 70 + Tali SCH 75;
    Level difference of: 5

    ...
    ```
  This output shows the job pairing, their levels, and the level difference between the two jobs.
