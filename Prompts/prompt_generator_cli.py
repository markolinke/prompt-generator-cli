#!/usr/bin/env python3
"""
Prompt Generator CLI - Simple tool to generate AI prompts from YAML configuration.
"""

from Interaction.displayMenu import display_menu
from Interaction.animations import startup_loading_effect, retro_loading_effect
from Interaction.colors import Colors
from Content.categorys import load_categories, get_category_choice


try:
    import pyperclip
    HAS_PYPERCLIP = True
except ImportError:
    HAS_PYPERCLIP = False


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
