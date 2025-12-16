#!/usr/bin/env python3
"""
Prompt Generator CLI - Simple tool to generate AI prompts from YAML configuration.
"""

import re
import sys
import time
import random

try:
    import pyperclip
    HAS_PYPERCLIP = True
except ImportError:
    HAS_PYPERCLIP = False


# ANSI color codes (no external dependencies)
class Colors:
    """ANSI color codes for terminal output."""
    # Reset
    RESET = '\033[0m'
    
    # Text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'


CONFIG_FILE = "config/categories/student-life-hr.yaml"


def parse_yaml_simple(content):
    """Simple YAML parser for the specific structure used in this project.
    Only handles the categories structure with name and questions.
    """
    categories = []
    lines = content.split('\n')
    i = 0
    
    # Skip until we find "categories:"
    while i < len(lines) and not lines[i].strip().startswith('categories:'):
        i += 1
    
    if i >= len(lines):
        return []
    
    i += 1  # Skip "categories:"
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
        
        # Check for new category (starts with "- name:")
        if line.startswith('- name:'):
            category = {'name': '', 'questions': []}
            # Extract name
            name_match = re.match(r'- name:\s*(.+)', line)
            if name_match:
                category['name'] = name_match.group(1).strip()
            
            i += 1
            
            # Look for questions section
            while i < len(lines):
                line = lines[i].strip()
                
                if not line:
                    i += 1
                    continue
                
                # If we hit a new category, break
                if line.startswith('- name:'):
                    break
                
                # Check for "questions:" line
                if line.startswith('questions:'):
                    i += 1
                    continue
                
                # Check for question entry (starts with "- question:")
                if line.startswith('- question:'):
                    question = {'question': '', 'instruction': ''}
                    # Extract question text
                    q_match = re.match(r'- question:\s*(.+)', line)
                    if q_match:
                        question['question'] = q_match.group(1).strip()
                    
                    i += 1
                    
                    # Look for instruction on next line
                    if i < len(lines):
                        inst_line = lines[i].strip()
                        if inst_line.startswith('instruction:'):
                            inst_match = re.match(r'instruction:\s*(.+)', inst_line)
                            if inst_match:
                                question['instruction'] = inst_match.group(1).strip()
                            i += 1
                    
                    category['questions'].append(question)
                else:
                    i += 1
            
            if category['name']:
                categories.append(category)
        else:
            i += 1
    
    return categories


def load_categories():
    """Load categories from YAML configuration file."""
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            categories = parse_yaml_simple(content)
            return categories
    except FileNotFoundError:
        print(f"Error: Configuration file '{CONFIG_FILE}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Failed to parse configuration file: {e}")
        sys.exit(1)


def display_menu(categories):
    """Display category selection menu."""
    print(f"\n{Colors.BRIGHT_CYAN}{Colors.BOLD}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.BRIGHT_WHITE}{Colors.BOLD}Welcome to Prompt Generator CLI (Student Edition)!{Colors.RESET}  {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    print(f"{Colors.BRIGHT_BLUE}{Colors.BOLD}Available categories:{Colors.RESET}")
    
    sorted_categories = sorted(categories, key=lambda x: x['name'])
    for i, category in enumerate(sorted_categories, 1):
        print(f"  {Colors.BRIGHT_GREEN}{Colors.BOLD}{i}.{Colors.RESET} {Colors.GREEN}{category['name']}{Colors.RESET}")
    print(f"  {Colors.BRIGHT_YELLOW}{Colors.BOLD}0.{Colors.RESET} {Colors.YELLOW}Exit{Colors.RESET}")
    print()


def get_category_choice(categories):
    """Get user's category selection."""
    sorted_categories = sorted(categories, key=lambda x: x['name'])
    
    while True:
        try:
            choice = input(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}→{Colors.RESET} {Colors.CYAN}Select a category (number):{Colors.RESET} ").strip()
            if choice == "0":
                return None
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(sorted_categories):
                selected = sorted_categories[choice_num - 1]
                print(f"{Colors.BRIGHT_GREEN}✓ Selected: {Colors.GREEN}{selected['name']}{Colors.RESET}\n")
                return selected
            else:
                print(f"{Colors.BRIGHT_RED}⚠{Colors.RESET} {Colors.RED}Please enter a number between 1 and {len(sorted_categories)}, or 0 to exit.{Colors.RESET}")
        except ValueError:
            print(f"{Colors.BRIGHT_RED}⚠{Colors.RESET} {Colors.RED}Please enter a valid number.{Colors.RESET}")
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Exiting...{Colors.RESET}")
            sys.exit(0)


def collect_answers(category):
    """Collect answers for all questions in a category."""
    print(f"\n{Colors.BRIGHT_CYAN}{Colors.BOLD}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.BRIGHT_WHITE}{Colors.BOLD}{category['name']}{Colors.RESET}  {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    answers = []
    questions = category.get('questions', [])
    
    for i, q in enumerate(questions, 1):
        question_text = q.get('question', '')
        instruction = q.get('instruction', '')
        
        print(f"{Colors.BRIGHT_BLUE}{Colors.BOLD}Question {i}/{len(questions)}:{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}  {question_text}{Colors.RESET}")
        if instruction:
            print(f"{Colors.DIM}{Colors.CYAN}  💡 {instruction}{Colors.RESET}")
        
        user_input = input(f"{Colors.BRIGHT_YELLOW}  →{Colors.RESET} {Colors.YELLOW}Your answer:{Colors.RESET} ").strip()
        
        if not user_input or user_input.lower() == "abort":
            print(f"\n{Colors.YELLOW}⚠ Aborted. Returning to main menu.{Colors.RESET}\n")
            return None
        
        answers.append({
            'question': question_text,
            'answer': user_input
        })
        print(f"{Colors.BRIGHT_GREEN}  ✓ Answer saved{Colors.RESET}\n")
    
    return answers


def retro_loading_effect():
    """Display a retro Commodore 64-style loading animation with flamboyant messages."""
    messages = [
        "COLLECTING USER INPUTS...",
        "ACCESSING CONTROL CENTER DATABASE...",
        "SEEKING ROOT PARTITION...",
        "INITIALIZING NEURAL MATRIX...",
        "REBOOTING QUANTUM PROCESSORS...",
        "SYNCHRONIZING DATA STREAMS...",
        "CALIBRATING RESPONSE ALGORITHMS...",
        "ESTABLISHING SECURE CONNECTION...",
        "PARSING SEMANTIC STRUCTURES...",
        "GENERATING OPTIMAL PROMPT...",
    ]
    
    # Shuffle messages for variety
    shuffled_messages = messages.copy()
    random.shuffle(shuffled_messages)
    
    # Select 3-5 messages to display
    num_messages = random.randint(3, 5)
    selected_messages = shuffled_messages[:num_messages]
    
    # Calculate timing (total up to 10 seconds)
    total_time = random.uniform(4, 10)
    time_per_message = total_time / num_messages
    
    print(f"\n{Colors.BRIGHT_CYAN}{Colors.BOLD}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.BRIGHT_WHITE}{Colors.BOLD}SYSTEM PROCESSING{Colors.RESET}  {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    for i, msg in enumerate(selected_messages):
        # Typewriter effect with C64 style
        chars = list(msg)
        display_text = ""
        
        # Print with typewriter effect
        for char in chars:
            display_text += char
            # Use C64 blue/cyan colors
            print(f"\r{Colors.BRIGHT_CYAN}{Colors.BOLD}>{Colors.RESET} {Colors.CYAN}{display_text}{Colors.RESET}{Colors.BLACK}█{Colors.RESET}", end='', flush=True)
            time.sleep(0.03)  # Fast typing speed
        
        # Add dots animation
        for dot_count in range(1, 4):
            dots = "." * dot_count
            print(f"\r{Colors.BRIGHT_CYAN}{Colors.BOLD}>{Colors.RESET} {Colors.CYAN}{msg}{dots}{Colors.RESET}{Colors.BLACK}█{Colors.RESET}", end='', flush=True)
            time.sleep(0.2)
        
        # Success indicator
        print(f"\r{Colors.BRIGHT_CYAN}{Colors.BOLD}>{Colors.RESET} {Colors.BRIGHT_GREEN}{msg} ✓{Colors.RESET}")
        
        # Random delay between messages (but ensure total time is respected)
        if i < len(selected_messages) - 1:
            remaining_time = time_per_message - (0.03 * len(chars) + 0.6)
            if remaining_time > 0:
                time.sleep(remaining_time)
    
    # Final completion message
    print(f"\n{Colors.BRIGHT_GREEN}{Colors.BOLD}✓ SYSTEM READY{Colors.RESET}\n")


def generate_prompt(category_name, answers):
    """Generate English prompt from category and answers using hard-coded template."""
    prompt = f"""You are a friendly, practical student advisor with extensive experience helping university students navigate their daily challenges and make the most of their academic and personal life.

Context: The student is seeking advice related to: {category_name}

Student Information:
"""
    
    for i, item in enumerate(answers, 1):
        prompt += f"{i}. {item['question']}: {item['answer']}\n"
    
    prompt += """
Please provide comprehensive, actionable advice in Croatian. Structure your response with:
- Clear headings and sections
- Bullet points for easy reading
- Specific, practical steps the student can take
- Empathetic and encouraging tone
- Real-world examples when relevant

Focus on being helpful, realistic, and supportive while addressing the student's specific situation and needs.
"""
    
    return prompt


def copy_to_clipboard(text):
    """Copy text to clipboard if pyperclip is available."""
    if HAS_PYPERCLIP:
        try:
            pyperclip.copy(text)
            print("Prompt copied to clipboard!")
            return True
        except Exception:
            print("Could not copy to clipboard. Please copy manually.")
            return False
    else:
        print("Please copy manually (pyperclip not installed).")
        return False


def main():
    """Main application loop."""
    categories = load_categories()
    
    if not categories:
        print("Error: No categories found in configuration file.")
        sys.exit(1)
    
    while True:
        display_menu(categories)
        category = get_category_choice(categories)
        
        if category is None:
            print("Goodbye!")
            break
        
        answers = collect_answers(category)
        
        if answers is None:
            continue
        
        retro_loading_effect()
        prompt = generate_prompt(category['name'], answers)
        
        print("\nHere is your generated prompt:\n")
        print('"""')
        print(prompt)
        print('"""')
        print()
        
        copy_to_clipboard(prompt)
        print()
        
        while True:
            again = input("Generate another prompt? (y/n): ").strip().lower()
            if again in ['y', 'yes']:
                break
            elif again in ['n', 'no']:
                print("Goodbye!")
                return
            else:
                print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)

