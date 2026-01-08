#!/usr/bin/env python3
"""
Prompt Generator CLI - Simple tool to generate AI prompts from YAML configuration.
"""

import re
import sys
import time
from animations import startup_loading_effect, retro_loading_effect, display_menu
from colors import Colors

try:
    import pyperclip
    HAS_PYPERCLIP = True
except ImportError:
    HAS_PYPERCLIP = False





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
            print(f"{Colors.BRIGHT_GREEN}✓ Prompt copied to clipboard!{Colors.RESET}")
            return True
        except Exception:
            print(f"{Colors.BRIGHT_YELLOW}⚠ Could not copy to clipboard. Please copy manually.{Colors.RESET}")
            return False
    else:
        print(f"{Colors.YELLOW}ℹ Please copy manually (pyperclip not installed).{Colors.RESET}")
        return False


def display_prompt_and_ask_continue(prompt):
    """Display the generated prompt and ask if user wants to generate another.
    
    Returns:
        True if user wants to continue, False if user wants to exit
    """
    print(f"\n{Colors.BRIGHT_CYAN}{Colors.BOLD}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.BRIGHT_WHITE}{Colors.BOLD}GENERATED PROMPT{Colors.RESET}  {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    print(f"{Colors.BRIGHT_BLUE}{Colors.BOLD}Prompt:{Colors.RESET}\n")
    triple_quotes = '"""'
    print(f"{Colors.CYAN}{Colors.BOLD}{triple_quotes}{Colors.RESET}")
    print(f"{Colors.WHITE}{prompt}{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}{triple_quotes}{Colors.RESET}")
    print()
    
    copy_to_clipboard(prompt)
    print()
    
    while True:
        again = input(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}→{Colors.RESET} {Colors.CYAN}Generate another prompt? (y/n):{Colors.RESET} ").strip().lower()
        if again in ['y', 'yes']:
            print(f"{Colors.BRIGHT_GREEN}✓ Starting new prompt generation...{Colors.RESET}\n")
            return True
        elif again in ['n', 'no']:
            print(f"\n{Colors.BRIGHT_YELLOW}{Colors.BOLD}Goodbye!{Colors.RESET}\n")
            return False
        else:
            print(f"{Colors.BRIGHT_RED}⚠{Colors.RESET} {Colors.RED}Please enter 'y' or 'n'.{Colors.RESET}")


def main():
    """Main application loop."""
    startup_loading_effect()
    categories = load_categories()
    
    if not categories:
        print("Error: No categories found in configuration file.")
        sys.exit(1)
    
    while True:
        display_menu(categories)
        category = get_category_choice(categories)
        
        if category is None:
            print(f"\n{Colors.BRIGHT_YELLOW}{Colors.BOLD}Goodbye!{Colors.RESET}\n")
            break
        
        answers = collect_answers(category)
        
        if answers is None:
            continue
        
        retro_loading_effect()
        prompt = generate_prompt(category['name'], answers)
        
        if not display_prompt_and_ask_continue(prompt):
            return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)

