# Court_Collusion
Court Collusion is a grand strategy-inspired AI simulation, heavily influenced by games like Crusader Kings III. The project explores how NPCs in grand strategy games could adapt Reinforcement Learning (RL) to optimize their decision-making over time. The game simulates a medieval feudal system, where Knights, Dukes, and a King maneuver through intrigue, resource accumulation, assassinations, and coups to climb the political hierarchy.

While traditional grand strategy AI often follows hardcoded behavior trees, this experiment tests how an RL-driven agent can learn and outperform standard NPCs over time. By introducing a learning agent, the simulation examines whether an AI-controlled knight can develop superior strategies for wealth accumulation, power growth, and political takeovers compared to standard rule-based NPCs.

This repository contains the core game code, as well as two analytical scripts that generate performance graphs comparing a reinforcement learning-driven knight to regular NPCs in terms of gold and power accumulation, assassination attempts, and strategic decision-making.

# Files & Descriptions
1. CC_base_code.ipynb
The base simulation code for Court Collusion.
Implements the full feudal system with hierarchical decision-making.
Simulates Knights and Dukes as they take actions to gather resources, duel, assassinate, and attempt coups.
2. CC_RL_gold&power_accumulation_analysis.ipynb
Analyzes gold and power accumulation over time.
Compares normal NPC knights vs. RL-controlled knight in terms of how efficiently they collect resources.
Generates graphs showing the progress of each knight, with RL knight’s performance plotted as a solid line and normal NPCs as dotted lines.
3. CC_RL_assassinations_over_time.ipynb
Analyzes assassination attempts over time.
Compares how often normal NPC knights attempt assassinations vs. how quickly an RL-trained knight learns to optimize assassination attempts.
Generates a graph tracking assassination attempts over multiple turns, with RL knight’s progress compared to normal knights.

# How to Use

Open the .ipynb files in Notebook and copy to Google Colab.
Run the scripts in Google Colab (recommended for smooth execution).
If the graphs appear weird, inconsistent, or illogical, re-run the script until the RL training stabilizes and produces meaningful results.

# Work in Progress

This project is still in development and subject to refinement.
The RL agent sometimes requires multiple runs to exhibit proper learning behavior.
Future updates may include improved learning stability, balancing tweaks, and expanded AI behaviors.
# Contributions & Feedback
This project is open to feedback, improvements, and suggestions! If you have ideas for refining the RL implementation or balancing the game mechanics, feel free to contribute.
