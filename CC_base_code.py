# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q8IYHydi2ARdY0dPzKyf2yoN855DTrEQ
"""

import random
import pandas as pd
import matplotlib.pyplot as plt

# --- CHARACTER CLASSES ---
class Knight:
    def __init__(self, name, duke):
        self.name = name
        self.gold = 1
        self.power = 2
        self.training_boost = False
        self.current_action = None
        self.action_turns_left = 0
        self.duke = duke  # Assigned to a specific Duke
        self.assassination_attempted = False  # Track if assassination is attempted
        self.equipment_purchased = False  # Limit equipment purchases

    def take_action(self):
        if self.action_turns_left > 0:
            self.action_turns_left -= 1
            return f"⏳ Still on {self.current_action} ({self.action_turns_left} turns left)"

        # Log current status
        print(f"{self.name}: Gold={self.gold}, Power={self.power}, Training={self.training_boost}")
        print(f"DEBUG: {self.name} evaluating actions")

        # Adjusted assassination criteria to be more frequent
        if self.gold >= 15 and self.power >= 12 and not self.assassination_attempted:
            if random.random() < 0.7:  # 70% chance of attempting assassination
                print(f"🔪 DEBUG: {self.name} meets assassination criteria!")
                self.assassination_attempted = True  # Prevent multiple attempts

                # Knight replaces the Duke
                self.duke.eliminated = True
                self.duke.name = f"Duke_{self.name}"  # Promote the Knight to Duke
                self.duke.gold = max(10, int(self.gold * 0.75))  # Inherit 75% of Knight's gold
                self.duke.power = max(10, int(self.power * 0.75))  # Inherit 75% of Knight's power
                self.duke.vassals = []  # Reset vassals for new Duke

                print(f"🔪 {self.name} successfully assassinated a Duke and took their place as {self.duke.name}!")
                return "🔪 Assassination SUCCESS"
            else:
                print(f"❌ {self.name} failed the assassination attempt!")
                return "❌ Assassination FAILED"

        available_actions = ["Duel", "Train", "Mission", "Steal Gold"]

        if self.gold >= 8 and not self.equipment_purchased:
            available_actions.append("Buy Equipment")
        if self.training_boost:
            available_actions.extend(["Duel", "Mission"])
        else:
            available_actions.extend(["Duel", "Mission", "Train"])

        # Ensure aggressive knights engage more
        if self.power > 8:
            available_actions.extend(["Duel"] * 3)  # Weight dueling even higher

        action = random.choice(available_actions)
        print(f"DEBUG: {self.name} chose action {action}")  # Log chosen action

        if action == "Duel":
            opponent = random.choice(knights)
            if opponent != self:
                duel_success = random.random() < (0.55 + 0.3 * self.training_boost)
                if duel_success:
                    self.power += 3  # Increased power gain from dueling
                    return f"⚔️ Won duel against {opponent.name} (+3 Power)"
                else:
                    return f"⚔️ Lost duel against {opponent.name}"

        elif action == "Train":
            self.training_boost = True
            return "🏋️ Training (boosts next mission/duel by +30%)"

        elif action == "Mission":
            self.current_action = "Mission"
            self.action_turns_left = 3
            success = random.random() < (0.75 + 0.3 * self.training_boost)
            self.training_boost = False
            if success:
                self.gold += 14
                self.power += 2
                return "🎯 Mission SUCCESS (+14 Gold, +2 Power)"
            else:
                return "❌ Mission FAILED"

        elif action == "Steal Gold":
            target = random.choice(knights)
            if target.gold >= 3:
                self.gold += 5
                target.gold -= 5
                return f"💰 Stole 5 Gold from {target.name}"
            else:
                return "❌ Steal Gold FAILED (target too poor)"

        elif action == "Buy Equipment":
            self.gold -= 8
            self.equipment_purchased = True
            return "🛡️ Bought Equipment (+10% success chance for duels/missions)"

        return "❌ No valid action selected"

class Duke:
    def __init__(self, name):
        self.name = name
        self.gold = 10
        self.power = 5
        self.vassals = []
        self.eliminated = False

    def take_action(self):
        if self.eliminated:
            return "🚫 Duke Eliminated"

        actions = ["Steal Gold", "Steal Power", "Adjust Taxes"]
        if self.gold >= 20 and self.power >= 15 and random.random() < 0.4:  # 40% chance to attempt coup
            print(f"⚔️ {self.name} is attempting a Coup!")
            return "SUCCESSFUL Coup!"

        action = random.choice(actions)

        if action == "Steal Gold":
            self.gold += 6
            return "💰 Stole Gold (+6 Gold)"
        elif action == "Steal Power":
            self.power += 2
            return "🔥 Stole Power (+2 Power)"
        elif action == "Adjust Taxes":
            return "💰 Adjusted Taxes"

        return "❌ No valid action selected"

# --- RUN FINAL TEST SIMULATION WITH VERIFIED TRACKING ---

coup_success_count = 0
assassination_success_count = 0
turns_to_throne = []

for simulation_run in range(50):
    print(f"=== Simulation Run {simulation_run + 1} ===")
    dukes = [Duke(f"Duke_{i+1}") for i in range(6)]
    knights = [Knight(f"Knight_{i+1}", random.choice(dukes)) for i in range(12)]
    for knight in knights:
        knight.duke.vassals.append(knight)

    turn_counter = 0
    game_over = False

    while turn_counter < 50 and not game_over:
        turn_counter += 1
        print(f"--- TURN {turn_counter} ---")

        for knight in knights:
            action_result = knight.take_action()
            if action_result:
                print(f"{knight.name}: {action_result}")
                if "Assassination SUCCESS" in action_result:
                    assassination_success_count += 1

        for duke in dukes:
            action_result = duke.take_action()
            if action_result:
                print(f"{duke.name}: {action_result}")
                if "SUCCESSFUL Coup!" in action_result:
                    coup_success_count += 1
                    turns_to_throne.append(turn_counter)
                    game_over = True

print(f"Total Coup Successes: {coup_success_count}")
print(f"Total Assassination Successes: {assassination_success_count}")