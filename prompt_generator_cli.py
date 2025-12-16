#!/usr/bin/env python3
"""
Prompt Generator CLI - Simple tool to generate AI prompts from YAML configuration.
"""

import re
import sys

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


def display_menu(categories):
    """Display category selection menu."""
    print("\nWelcome to Prompt Generator CLI (Student Edition)!\n")
    print("Available categories:")
    
    sorted_categories = sorted(categories, key=lambda x: x['name'])
    for i, category in enumerate(sorted_categories, 1):
        print(f"{i}. {category['name']}")
    print("0. Exit")
    print()


def get_category_choice(categories):
    """Get user's category selection."""
    sorted_categories = sorted(categories, key=lambda x: x['name'])
    
    while True:
        try:
            choice = input("Select a category (number): ").strip()
            if choice == "0":
                return None
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(sorted_categories):
                return sorted_categories[choice_num - 1]
            else:
                print(f"Please enter a number between 1 and {len(sorted_categories)}, or 0 to exit.")
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)


def collect_answers(category):
    """Collect answers for all questions in a category."""
    print(f"\n--- {category['name']} ---\n")
    
    answers = []
    questions = category.get('questions', [])
    
    for i, q in enumerate(questions, 1):
        question_text = q.get('question', '')
        instruction = q.get('instruction', '')
        
        print(f"{i}. {question_text}")
        if instruction:
            print(f"   {instruction}")
        
        user_input = input("   > ").strip()
        
        if not user_input or user_input.lower() == "abort":
            print("\nAborted. Returning to main menu.")
            return None
        
        answers.append({
            'question': question_text,
            'answer': user_input
        })
        print()
    
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

