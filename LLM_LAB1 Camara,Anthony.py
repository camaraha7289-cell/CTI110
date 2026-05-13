"""
Quiz Game Manager
A colorful terminal-based quiz game that lets users manage and play a 5-question quiz.
"""

import json
import os
import random
import time

# ── ANSI color codes ──────────────────────────────────────────────────────────
class Colors:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BG_BLUE = "\033[44m"

C = Colors  # shorthand

# ── Default question bank ─────────────────────────────────────────────────────
DEFAULT_QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C",
        "category": "Geography"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B",
        "category": "Science"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) Jane Austen", "C) Mark Twain", "D) William Shakespeare"],
        "answer": "D",
        "category": "Literature"
    },
    {
        "question": "What is 12 × 12?",
        "options": ["A) 124", "B) 144", "C) 132", "D) 148"],
        "answer": "B",
        "category": "Math"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A) Gold", "B) Osmium", "C) Oxygen", "D) Oganesson"],
        "answer": "C",
        "category": "Science"
    },
    {
        "question": "In what year did World War II end?",
        "options": ["A) 1943", "B) 1944", "C) 1945", "D) 1946"],
        "answer": "C",
        "category": "History"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D",
        "category": "Geography"
    },
    {
        "question": "Which programming language is known as the 'language of the web'?",
        "options": ["A) Python", "B) JavaScript", "C) Java", "D) C++"],
        "answer": "B",
        "category": "Technology"
    },
]

# ── Helpers ───────────────────────────────────────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(f"""
{C.CYAN}{C.BOLD}
  ██████╗ ██╗   ██╗██╗███████╗    ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗
 ██╔═══██╗██║   ██║██║╚══███╔╝    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
 ██║   ██║██║   ██║██║  ███╔╝     ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
 ██║▄▄ ██║██║   ██║██║ ███╔╝      ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
 ╚██████╔╝╚██████╔╝██║███████╗    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
  ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
{C.RESET}""")

def divider(char="─", width=65, color=C.DIM):
    print(f"{color}{char * width}{C.RESET}")

def prompt(msg, color=C.YELLOW):
    return input(f"{color}{msg}{C.RESET}").strip()

def pause():
    input(f"\n{C.DIM}Press Enter to continue...{C.RESET}")

def score_bar(score, total=5):
    filled = int((score / total) * 20)
    bar = "█" * filled + "░" * (20 - filled)
    pct = score / total
    color = C.GREEN if pct >= 0.8 else C.YELLOW if pct >= 0.5 else C.RED
    return f"{color}[{bar}] {score}/{total}{C.RESET}"

# ── Quiz logic ────────────────────────────────────────────────────────────────
def run_quiz(questions: list):
    """Run a 5-question quiz session and return the score."""
    clear()
    banner()
    print(f"{C.BOLD}{C.WHITE}  🎯  Get ready! 5 questions await you.{C.RESET}\n")
    divider()
    time.sleep(1)

    score = 0
    results = []

    for i, q in enumerate(questions, 1):
        clear()
        print(f"\n{C.CYAN}{C.BOLD}  Question {i} of 5  {C.DIM}[{q['category']}]{C.RESET}")
        divider()
        print(f"\n  {C.WHITE}{C.BOLD}{q['question']}{C.RESET}\n")
        for opt in q["options"]:
            print(f"    {C.BLUE}{opt}{C.RESET}")
        print()

        while True:
            answer = prompt("  Your answer (A/B/C/D): ").upper()
            if answer in ("A", "B", "C", "D"):
                break
            print(f"  {C.RED}Please enter A, B, C, or D.{C.RESET}")

        correct = answer == q["answer"]
        if correct:
            score += 1
            print(f"\n  {C.GREEN}{C.BOLD}✔  Correct!{C.RESET}")
        else:
            correct_opt = next(o for o in q["options"] if o.startswith(q["answer"]))
            print(f"\n  {C.RED}{C.BOLD}✘  Wrong!{C.RESET}  The answer was: {C.GREEN}{correct_opt}{C.RESET}")

        results.append({"question": q["question"], "your_answer": answer,
                        "correct_answer": q["answer"], "correct": correct})
        time.sleep(1.2)

    # ── Final score screen ────────────────────────────────────────────────────
    clear()
    banner()
    divider("═", color=C.CYAN)
    print(f"\n  {C.BOLD}{C.WHITE}Quiz Complete!{C.RESET}\n")
    print(f"  Score: {score_bar(score)}\n")
    divider()

    pct = score / 5
    if pct == 1.0:
        grade = f"{C.GREEN}🏆 Perfect! Incredible!{C.RESET}"
    elif pct >= 0.8:
        grade = f"{C.GREEN}🌟 Excellent work!{C.RESET}"
    elif pct >= 0.6:
        grade = f"{C.YELLOW}👍 Good job!{C.RESET}"
    elif pct >= 0.4:
        grade = f"{C.YELLOW}📚 Keep studying!{C.RESET}"
    else:
        grade = f"{C.RED}💪 Better luck next time!{C.RESET}"

    print(f"  {grade}\n")
    divider()
    print(f"\n  {C.BOLD}Review:{C.RESET}")
    for r in results:
        icon = f"{C.GREEN}✔{C.RESET}" if r["correct"] else f"{C.RED}✘{C.RESET}"
        print(f"   {icon}  {r['question'][:55]:<55}  "
              f"You: {C.CYAN}{r['your_answer']}{C.RESET}  "
              f"Ans: {C.GREEN}{r['correct_answer']}{C.RESET}")
    print()
    pause()
    return score

# ── Question management ───────────────────────────────────────────────────────
def list_questions(questions):
    clear()
    print(f"\n{C.BOLD}{C.CYAN}  📋  Question Bank  ({len(questions)} questions){C.RESET}\n")
    divider()
    for i, q in enumerate(questions, 1):
        print(f"  {C.YELLOW}{i:>2}.{C.RESET} [{C.MAGENTA}{q['category']:<12}{C.RESET}] {q['question']}")
    print()
    pause()

def add_question(questions):
    clear()
    print(f"\n{C.BOLD}{C.CYAN}  ➕  Add New Question{C.RESET}\n")
    divider()

    question_text = prompt("  Question text: ")
    if not question_text:
        print(f"{C.RED}  Question cannot be empty.{C.RESET}")
        pause()
        return

    options = []
    labels = ["A", "B", "C", "D"]
    print(f"\n  {C.DIM}Enter 4 answer options:{C.RESET}")
    for label in labels:
        opt = prompt(f"  Option {label}: ")
        options.append(f"{label}) {opt}")

    while True:
        answer = prompt("\n  Correct answer (A/B/C/D): ").upper()
        if answer in labels:
            break
        print(f"  {C.RED}Must be A, B, C, or D.{C.RESET}")

    category = prompt("  Category (e.g. Science, History): ") or "General"

    questions.append({"question": question_text, "options": options,
                      "answer": answer, "category": category})
    print(f"\n  {C.GREEN}✔  Question added!{C.RESET}")
    pause()

def remove_question(questions):
    clear()
    print(f"\n{C.BOLD}{C.CYAN}  🗑️  Remove a Question{C.RESET}\n")
    divider()
    for i, q in enumerate(questions, 1):
        print(f"  {C.YELLOW}{i}.{C.RESET} {q['question']}")
    print(f"  {C.DIM}0. Cancel{C.RESET}\n")

    choice = prompt("  Enter question number to remove: ")
    if choice == "0":
        return
    if choice.isdigit() and 1 <= int(choice) <= len(questions):
        removed = questions.pop(int(choice) - 1)
        print(f"\n  {C.GREEN}✔  Removed: {removed['question']}{C.RESET}")
    else:
        print(f"  {C.RED}Invalid selection.{C.RESET}")
    pause()

def select_questions(questions):
    """Pick exactly 5 questions (random if pool is large)."""
    if len(questions) < 5:
        print(f"\n{C.RED}  ⚠  You need at least 5 questions in the bank to play!{C.RESET}")
        pause()
        return None
    pool = random.sample(questions, 5)
    return pool

# ── Save / Load ───────────────────────────────────────────────────────────────
SAVE_FILE = "quiz_questions.json"

def save_questions(questions):
    with open(SAVE_FILE, "w") as f:
        json.dump(questions, f, indent=2)
    print(f"\n  {C.GREEN}✔  Questions saved to {SAVE_FILE}{C.RESET}")
    pause()

def load_questions():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE) as f:
            return json.load(f)
    return DEFAULT_QUESTIONS.copy()

# ── Main menu ─────────────────────────────────────────────────────────────────
def main():
    questions = load_questions()

    while True:
        clear()
        banner()
        divider("═", color=C.CYAN)
        print(f"\n  {C.BOLD}MAIN MENU{C.RESET}  {C.DIM}({len(questions)} questions in bank){C.RESET}\n")
        print(f"  {C.GREEN}1.{C.RESET}  ▶  Play Quiz")
        print(f"  {C.BLUE}2.{C.RESET}  📋  View All Questions")
        print(f"  {C.YELLOW}3.{C.RESET}  ➕  Add a Question")
        print(f"  {C.RED}4.{C.RESET}  🗑️  Remove a Question")
        print(f"  {C.MAGENTA}5.{C.RESET}  💾  Save Questions")
        print(f"  {C.DIM}6.{C.RESET}  🚪  Quit\n")
        divider("═", color=C.CYAN)

        choice = prompt("\n  Choose an option: ")

        if choice == "1":
            selected = select_questions(questions)
            if selected:
                run_quiz(selected)
        elif choice == "2":
            list_questions(questions)
        elif choice == "3":
            add_question(questions)
        elif choice == "4":
            remove_question(questions)
        elif choice == "5":
            save_questions(questions)
        elif choice == "6":
            clear()
            print(f"\n{C.CYAN}{C.BOLD}  Thanks for playing! Goodbye! 👋{C.RESET}\n")
            break
        else:
            print(f"\n  {C.RED}Invalid option. Please choose 1–6.{C.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()