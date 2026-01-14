import sys
from Interaction.colors import Colors
from Utils.parseYAML import parse_yaml_simple


CONFIG_FILE = "config/categories/student-life-hr.yaml"


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