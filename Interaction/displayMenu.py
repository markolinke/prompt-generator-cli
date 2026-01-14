from Interaction.colors import Colors

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