import time
from colors import Colors
import random



def startup_loading_effect():
    """Display a retro Commodore 64-style startup loading animation."""
    messages = [
        "LOADING...",
        "PREPARING LAYOUT...",
        "INITIALIZING INTERFACE...",
        "READY",
    ]
    
    # C64 style: simple, direct, classic colors
    print(f"\n{Colors.BRIGHT_CYAN}{Colors.BOLD}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.BRIGHT_WHITE}{Colors.BOLD}COMMODORE 64 SYSTEM{Colors.RESET}  {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    for msg in messages:
        # Typewriter effect with C64 style
        chars = list(msg)
        display_text = ""
        
        # Print with typewriter effect
        for char in chars:
            display_text += char
            print(f"\r{Colors.BRIGHT_CYAN}{Colors.BOLD}>{Colors.RESET} {Colors.CYAN}{display_text}{Colors.RESET}{Colors.BLACK}█{Colors.RESET}", end='', flush=True)
            time.sleep(0.05)  # Slightly slower for startup
        
        # Add dots animation for non-READY messages
        if msg != "READY":
            for dot_count in range(1, 4):
                dots = "." * dot_count
                print(f"\r{Colors.BRIGHT_CYAN}{Colors.BOLD}>{Colors.RESET} {Colors.CYAN}{msg}{dots}{Colors.RESET}{Colors.BLACK}█{Colors.RESET}", end='', flush=True)
                time.sleep(0.15)
            print(f"\r{Colors.BRIGHT_CYAN}{Colors.BOLD}>{Colors.RESET} {Colors.BRIGHT_GREEN}{msg} ✓{Colors.RESET}")
        else:
            # Special treatment for READY
            print(f"\r{Colors.BRIGHT_CYAN}{Colors.BOLD}>{Colors.RESET} {Colors.BRIGHT_GREEN}{Colors.BOLD}{msg} ✓{Colors.RESET}")
        
        # Delay between messages
        if msg != "READY":
            time.sleep(0.3)
    
    print(f"\n{Colors.BRIGHT_GREEN}{Colors.BOLD}*** SYSTEM READY ***{Colors.RESET}\n")
    time.sleep(0.5)


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