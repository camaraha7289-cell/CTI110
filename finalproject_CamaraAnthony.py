# Anthony Camara-Hernandez
# 5/10/2026
# Final_project Game
# Making a game using Python Libaries 

import random
import time

# ─────────────────────────────────────────────
#  Kingdom Racing 🏰  —  Python Edition
# ─────────────────────────────────────────────

ROLES = ["⚔️  Knight", "🏹 Ranger", "🧙 Wizard", "🐉 Dragon Rider"]

KINGDOM_EVENTS = [
    ("stumbles on a cobblestone",        {"speed": -2, "stamina": -3}),
    ("finds a royal shortcut",           {"speed": +3, "luck":   +2}),
    ("gets cheered by the crowd",        {"morale": +5, "speed": +1}),
    ("loses a horseshoe",               {"speed": -3, "morale": -2}),
    ("drinks a speed potion 🧪",         {"speed": +4, "potions": -1}),
    ("spots an enemy ambush and dodges", {"luck":  +3, "stamina": -2}),
    ("gets distracted by a jester 🤡",   {"speed": -2, "morale": -3}),
    ("leaps over a fallen log",          {"skill": +2, "stamina": -1}),
    ("avoids a mud pit",                 {"luck":  +2, "morale": +2}),
    ("catches a magical tailwind",       {"speed": +5, "stamina": -2}),
    ("earns royal gold 💰",              {"gold":  +10}),
    ("trips on their cape",             {"speed": -3, "morale": -4}),
]

# NEW RANDOM ITEMS FOR LAPS 3 AND 4
RANDOM_ITEMS = [
    ("⚡ Turbo Boots", {"speed": +3}),
    ("🛡️ Shield Charm", {"luck": +2}),
    ("🔥 Dragon Flame", {"skill": +3}),
    ("🍀 Lucky Coin", {"luck": +4}),
    ("💨 Wind Cloak", {"speed": +2}),
]

TOTAL_LAPS = 5

# NPC name pools
NPC_FIRST = ["Sir", "Lady", "Prince", "Duke", "Baron", "Lord", "Dame", "Earl"]
NPC_LAST  = ["Ashford", "Brightmoor", "Crestfall", "Dawnridge", "Embervale",
             "Frostwick", "Goldmane", "Hawkstone", "Ironveil", "Jadewynn"]


# ─────────────────────────────────────────────
#  Create player
# ─────────────────────────────────────────────
def create_character(character_number: int) -> dict:
    """Value-returning function to create the player's kingdom race character."""
    role = ROLES[character_number - 1]
    print(f"\n  {role}")
    name  = input("    Enter your champion's name : ").strip() or "Hero"
    speed = int(input(f"    Enter {name}'s speed  (1-10): "))
    skill = int(input(f"    Enter {name}'s skill  (1-10): "))

    character = {
        "name":       name,
        "role":       role,
        "speed":      max(1, min(10, speed)),
        "skill":      max(1, min(10, skill)),
        "stamina":    random.randint(6, 10),
        "luck":       random.randint(4, 10),
        "morale":     10,
        "potions":    random.randint(1, 3),
        "gold":       random.randint(10, 40),
        "distance":   0.0,
        "finish_lap": None,
        "is_player":  True,
    }
    return character


# ─────────────────────────────────────────────
#  Create NPC
# ─────────────────────────────────────────────
def create_npc(character_number: int) -> dict:
    """Value-returning function to randomly generate an NPC opponent."""
    role = ROLES[character_number - 1]
    name = f"{random.choice(NPC_FIRST)} {random.choice(NPC_LAST)}"

    character = {
        "name":       name,
        "role":       role,
        "speed":      random.randint(4, 10),
        "skill":      random.randint(4, 10),
        "stamina":    random.randint(5, 10),
        "luck":       random.randint(3, 10),
        "morale":     10,
        "potions":    random.randint(0, 3),
        "gold":       random.randint(10, 40),
        "distance":   0.0,
        "finish_lap": None,
        "is_player":  False,
    }
    return character


def display_character(character: dict) -> None:
    """Print the current key:value pairs for a character."""
    print(f"\n  {'─' * 36}")
    print(f"  {character['role']}  —  {character['name']}")
    print(f"  {'─' * 36}")

    skip = {"name", "role", "distance", "finish_lap"}

    for key, value in character.items():
        if key not in skip:
            bar = "█" * value if isinstance(value, int) and value <= 15 else ""
            print(f"  {key:<10} : {value}  {bar}")

    progress = int(character["distance"])
    filled = int(progress / 5)
    track = "█" * filled + "░" * (20 - filled)

    print(f"  {'progress':<10} : {progress}%  [{track}]")
    print(f"  {'─' * 36}")


def apply_event(character: dict) -> str:
    """Apply a random kingdom event and mutate the character's stats."""
    event_text, changes = random.choice(KINGDOM_EVENTS)

    for stat, delta in changes.items():
        if stat in character:
            character[stat] = max(0, character[stat] + delta)

    return event_text


# ─────────────────────────────────────────────
#  PLAYER CHOICES
# ─────────────────────────────────────────────
def player_choice(character: dict, lap: int):
    """Give player a choice on certain laps."""

    if lap == 1:
        print("\n  ⚔️  CHOICE EVENT")
        print("  1. Speed up using a potion (+3 speed)")
        print("  2. Avoid the mud trap (+2 luck)")

        choice = input("  Choose (1 or 2): ")

        if choice == "1":
            character["speed"] += 3
            print(f"  ⚡ {character['name']} used a speed potion!")
        else:
            character["luck"] += 2
            print(f"  🍀 {character['name']} avoided the mud trap!")

    elif lap == 3:
        print("\n  🏰  FINAL CHOICE EVENT")
        print("  1. Sprint forward (+4 speed)")
        print("  2. Take the safe road (+3 stamina)")

        choice = input("  Choose (1 or 2): ")

        if choice == "1":
            character["speed"] += 4
            print(f"  ⚡ {character['name']} sprints ahead!")
        else:
            character["stamina"] += 3
            print(f"  🛡️ {character['name']} takes the safe road!")


# ─────────────────────────────────────────────
#  RANDOM ITEMS
# ─────────────────────────────────────────────
def give_random_item(character: dict):
    """Give random items during laps 3 and 4."""

    item_name, boosts = random.choice(RANDOM_ITEMS)

    print(f"\n  🎁 {character['name']} found {item_name}!")

    for stat, amount in boosts.items():
        character[stat] += amount
        print(f"     +{amount} {stat}")


def race_lap(characters: list) -> list[str]:
    """
    Simulate one lap of the race.
    Returns a list of event strings for logging.
    """
    log_lines = []

    for char in characters:
        if char["finish_lap"] is not None:
            continue

        base_move  = (char["speed"] / 2) + random.uniform(-1, 2)
        luck_bonus = random.uniform(0, 2) if char["luck"] > 6 else 0
        move       = max(0.5, base_move + luck_bonus)

        char["distance"] = min(100.0, char["distance"] + move * 4)

        event = apply_event(char)

        log_lines.append(
            f"  {char['role'].split()[0]} {char['name']:<16} {event}"
        )

    return log_lines


def display_track(characters: list, lap: int) -> None:
    """Print ASCII race track for all characters."""

    sorted_chars = sorted(characters, key=lambda c: c["distance"], reverse=True)

    print(f"\n  🏁  Lap {lap}/{TOTAL_LAPS}")
    print(f"  {'─' * 56}")

    for char in sorted_chars:
        dist    = int(char["distance"])
        filled  = int(dist / 5)
        track   = "█" * filled + "░" * (20 - filled)
        marker  = "🏅" if char["finish_lap"] else "  "
        name    = char["name"][:14].ljust(14)

        print(f"  {marker} {name} [{track}] {dist:>3}%")

    print(f"  {'─' * 56}")


def determine_results(characters: list) -> list:
    """Sort characters by finish order, then by distance."""

    return sorted(
        characters,
        key=lambda c: (c["finish_lap"] or TOTAL_LAPS + 1, -c["distance"])
    )


def display_podium(results: list) -> None:
    """Show final podium."""

    medals = ["🥇 1st", "🥈 2nd", "🥉 3rd", "   4th"]

    print("\n")
    print("  ╔══════════════════════════════════╗")
    print("  ║        🏆  RACE RESULTS  🏆       ║")
    print("  ╠══════════════════════════════════╣")

    for i, char in enumerate(results):
        lap_info = (
            f"(finished lap {char['finish_lap']})"
            if char["finish_lap"]
            else f"({int(char['distance'])}% done)"
        )

        print(f"  ║  {medals[i]}  {char['name']:<16} {lap_info:<12} ║")

    print("  ╚══════════════════════════════════╝")


# ─────────────────────────────────────────────
#  MAIN FUNCTION
# ─────────────────────────────────────────────
def main() -> None:

    print("=" * 56)
    print("        🏰  KINGDOM RACING  🏰")
    print("  Four champions race for glory across the realm!")
    print("=" * 56)

    # CREATE CHARACTERS
    characters = []

    print("\n  Create YOUR champion:\n")

    player = create_character(1)
    characters.append(player)

    print("\n  Generating your opponents...\n")

    for i in range(2, 5):
        npc = create_npc(i)

        print(f"  Opponent {i-1}: {npc['role']}  —  {npc['name']}")

        characters.append(npc)

    print("\n\n  ─── Starting line-up ───")

    for char in characters:
        tag = " 👤 YOU" if char.get("is_player") else " 🤖 NPC"

        print(f"\n  {tag}")
        display_character(char)

    input("\n  Press Enter to start the race... 🏁\n")

    # RACE LOOP
    for lap in range(1, TOTAL_LAPS + 1):

        # PLAYER CHOICES ON LAP 1 AND 3
        player_choice(player, lap)

        # RANDOM ITEMS ON LAP 3 AND 4
        if lap == 3 or lap == 4:
            print("\n  🎁 RANDOM ITEM ROUND!")

            for char in characters:
                give_random_item(char)

        log = race_lap(characters)

        display_track(characters, lap)

        # MARK FINISHERS
        for char in characters:
            if char["distance"] >= 100 and char["finish_lap"] is None:
                char["finish_lap"] = lap

                print(
                    f"\n  🎉  {char['name']} crosses the finish line on lap {lap}!"
                )

        # LAP EVENTS
        print("\n  Kingdom events this lap:")

        for line in log:
            print(line)

        # LIVE LEADER STATS
        leader = max(characters, key=lambda c: c["distance"])

        print(f"\n  📊  Live stats — leader {leader['name']}:")
        display_character(leader)

        # CHECK FINISH
        if all(c["finish_lap"] is not None for c in characters):
            print("\n  All champions have finished!")
            break

        if lap < TOTAL_LAPS:
            cont = input("\n  Press Enter for next lap (or 'q' to quit): ")

            if cont.lower() == "q":
                break

        time.sleep(0.2)

    # RESULTS
    results = determine_results(characters)

    display_podium(results)

    # WINNER STATS
    winner = results[0]

    print(f"\n  👑  Final stats for champion {winner['name']}:")
    display_character(winner)

    print("\n  Thanks for playing Kingdom Racing! 🏰\n")


# ─────────────────────────────────────────────
#  START GAME
# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()  
