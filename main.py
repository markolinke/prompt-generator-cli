import sys
from Interaction.displayMenu import display_menu
from Interaction.animations import startup_loading_effect, retro_loading_effect
from Interaction.colors import Colors
from Content.categorys import load_categories, get_category_choice
from Prompts.prompt_generator_cli import collect_answers, generate_prompt, display_prompt_and_ask_continue


def main():
    categories = load_categories()
    
    if not categories:
        print("Error: No categories found in configuration file.")
        sys.exit(1)

    """Main application loop."""
    startup_loading_effect()
    
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
        prompt = generate_prompt(category.get('name'), answers)
        
        if not display_prompt_and_ask_continue(prompt):
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)

