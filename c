"""
Epic Text Adventure Game
------------------------
A longer Python example that shows:

- Game loop
- Player stats, inventory, leveling
- Enemies and combat
- Locations with actions
- Shop system
- Saving and loading game state to a file

Run with:  python adventure_game.py
"""

import json
import os
import random
import sys
from typing import Dict, List, Optional


# ==========================
# Data classes and constants
# ==========================

class Player:
    def __init__(self, name: str):
        self.name = name
        self.max_hp = 30
        self.hp = 30
        self.attack = 5
        self.defense = 2
        self.gold = 10
        self.level = 1
        self.xp = 0
        self.inventory: List[str] = ["Rusty Sword"]
        self.location = "village_square"

    def is_alive(self) -> bool:
        return self.hp > 0

    def add_item(self, item: str) -> None:
        self.inventory.append(item)

    def remove_item(self, item: str) -> None:
        if item in self.inventory:
            self.inventory.remove(item)

    def gain_gold(self, amount: int) -> None:
        self.gold += max(0, amount)

    def spend_gold(self, amount: int) -> bool:
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False

    def gain_xp(self, amount: int) -> None:
        self.xp += amount
        self.check_level_up()

    def check_level_up(self) -> None:
        # Simple level curve:  level up at xp >= level * 20
        needed = self.level * 20
        while self.xp >= needed:
            self.xp -= needed
            self.level += 1
            hp_gain = random.randint(5, 10)
            atk_gain = random.randint(1, 3)
            def_gain = random.randint(0, 2)
            self.max_hp += hp_gain
            self.hp = self.max_hp
            self.attack += atk_gain
            self.defense += def_gain
            print(f"\n*** {self.name} reached level {self.level}! ***")
            print(f"Max HP +{hp_gain}, Attack +{atk_gain}, Defense +{def_gain}")
            needed = self.level * 20

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "max_hp": self.max_hp,
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
            "gold": self.gold,
            "level": self.level,
            "xp": self.xp,
            "inventory": self.inventory,
            "location": self.location,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Player":
        player = cls(data["name"])
        player.max_hp = data["max_hp"]
        player.hp = data["hp"]
        player.attack = data["attack"]
        player.defense = data["defense"]
        player.gold = data["gold"]
        player.level = data["level"]
        player.xp = data["xp"]
        player.inventory = data["inventory"]
        player.location = data["location"]
        return player


class Enemy:
    def __init__(self, name: str, hp: int, attack: int, defense: int,
                 gold_reward: int, xp_reward: int):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.gold_reward = gold_reward
        self.xp_reward = xp_reward

    def is_alive(self) -> bool:
        return self.hp > 0


class Item:
    def __init__(self, name: str, description: str, price: int,
                 hp_restore: int = 0, attack_boost: int = 0, defense_boost: int = 0):
        self.name = name
        self.description = description
        self.price = price
        self.hp_restore = hp_restore
        self.attack_boost = attack_boost
        self.defense_boost = defense_boost


SHOP_ITEMS: Dict[str, Item] = {
    "Small Potion": Item("Small Potion", "Restore 10 HP.", 5, hp_restore=10),
    "Large Potion": Item("Large Potion", "Restore 25 HP.", 12, hp_restore=25),
    "Iron Sword": Item("Iron Sword", "Increase attack by 3.", 20, attack_boost=3),
    "Steel Shield": Item("Steel Shield", "Increase defense by 2.", 18, defense_boost=2),
}

# -------------------------
# Map configuration
# -------------------------

LOCATIONS: Dict[str, Dict] = {
    "village_square": {
        "name": "Village Square",
        "description": "You stand in the bustling village square. A fountain trickles nearby.",
        "paths": {
            "north": "dark_forest",
            "east": "training_grounds",
            "west": "shop",
        },
    },
    "shop": {
        "name": "Old Merchant's Shop",
        "description": "Shelves of dusty items line the walls. The merchant eyes you curiously.",
        "paths": {
            "east": "village_square",
        },
    },
    "training_grounds": {
        "name": "Training Grounds",
        "description": "Wooden dummies and targets are scattered around. You can fight weak foes here.",
        "paths": {
            "west": "village_square",
            "north": "ruined_gate",
        },
    },
    "dark_forest": {
        "name": "Dark Forest",
        "description": "Trees loom overhead, their branches blocking the sunlight.",
        "paths": {
            "south": "village_square",
            "north": "ancient_ruins",
        },
    },
    "ancient_ruins": {
        "name": "Ancient Ruins",
        "description": "Crumbled stone pillars and a sense of old magic surround you.",
        "paths": {
            "south": "dark_forest",
            "east": "ruined_gate",
        },
    },
        "ruined_gate": {
            "name": "Ruined Gate",
            "description": "A broken gate leads into a shadowy keep. A powerful foe is rumored to live here.",
        },
    }
